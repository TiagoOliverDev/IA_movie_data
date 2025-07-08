import json
from pydantic import ValidationError
from openai import OpenAI
from config.config import OPENAI_API_KEY, OPENAI_MODEL
from utils.logger import logger
from schemas.movie_info import MovieInfo
from storage.db_handler import save_search_history, consult_history_by_title

client = OpenAI(api_key=OPENAI_API_KEY)


functions = [
    {
        "name": "obter_detalhes_filme",
        "description": "Retorna detalhes de um filme a partir do título.",
        "parameters": {
            "type": "object",
            "properties": {
                "data_lancamento": {"type": "string", "description": "Data de lançamento do filme."},
                "bilheteria": {"type": "string", "description": "Bilheteria aproximada em dólares."},
                "sinopse": {"type": "string", "description": "Sinopse curta do filme."},
                "erro": {"type": "string", "description": "Mensagem de erro, caso o filme não seja encontrado."},
            },
            "required": []
        }
    }
]

def get_movie_insights(title: str, max_retries: int = 2) -> dict:
    """
    Consulta a OpenAI utilizando function calling para obter informações estruturadas sobre um filme.

    - Se os dados já estiverem armazenados no banco (histórico), retorna-os diretamente sem consultar a OpenAI.
    - Se não, envia um prompt à OpenAI solicitando data de lançamento, bilheteria e sinopse.
    - Valida a resposta com Pydantic, e persiste no banco se for válida.
    - Em caso de erro de validação, tenta novamente até o limite de tentativas.
    - Retorna mensagens de erro apropriadas em caso de falha, título inválido ou filme não encontrado.

    Parâmetros:
        title (str): Título do filme a ser consultado.
        max_retries (int): Quantidade máxima de tentativas em caso de falha de validação.

    Retorno:
        dict: Dados estruturados do filme ou mensagem de erro.
    """
    
    if not title.strip():
        raise ValueError("O título do filme não pode estar vazio.")
    
    logger.info(f"Iniciando consulta para o filme: {title}")
    
    historico = consult_history_by_title(title)
    if historico:
        logger.info(f"Resultado encontrado no histórico salvo no banco de dados para o filme '{title}'")
        return historico

    prompt = (
        f"Você é um assistente de cinema. Responda apenas em JSON com as seguintes informações "
        f"sobre o filme '{title}': data de lançamento, bilheteria aproximada em dólares, "
        f"e uma sinopse curta. Caso não saiba alguma dessas informações, coloque \"Desconhecido\" no campo. "
        f"Se o filme não existir, retorne o seguinte JSON: {{\"erro\": \"Filme não encontrado\"}}."
    )

    for attempt in range(1, max_retries + 1):
        try:
            response = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                functions=functions,
                function_call={"name": "obter_detalhes_filme"},
                temperature=0.7,
                max_tokens=400
            )

            message = response.choices[0].message

            if not (message.function_call and message.function_call.arguments):
                logger.warning("Nenhuma função chamada detectada na resposta da OpenAI.")
                return {"erro": "Não foi possível obter informações estruturadas da IA."}

            try:
                dados = json.loads(message.function_call.arguments)
            except json.JSONDecodeError:
                logger.warning(f"Tentativa {attempt}: Resposta da OpenAI não está em JSON válido.")
                if attempt == max_retries:
                    return {"erro": "Resposta inválida da IA. Tente novamente."}
                continue  

            try:
                if "erro" in dados:
                    logger.warning(f"Filme não encontrado: {title}")
                    return {"erro": "Filme não encontrado. Verifique o título e tente novamente."}
                
                movie_info = MovieInfo(**dados)

                logger.info(f"Consulta bem-sucedida para o filme '{title}'")
                
                save_search_history(
                    titulo=title,
                    data_lancamento=movie_info.data_lancamento,
                    bilheteria=movie_info.bilheteria,
                    sinopse=movie_info.sinopse
                )
                
                return movie_info.dict()

            except ValidationError as ve:
                logger.warning(f"Tentativa {attempt}: Erro de validação: {ve}")
                if attempt == max_retries:
                    return {"erro": "Resposta da IA não passou na validação. Tente novamente."}
                continue  

        except Exception as e:
            logger.error(f"Erro inesperado na tentativa {attempt} para filme '{title}': {str(e)}", exc_info=True)
            if attempt == max_retries:
                return {"erro": f"Erro ao consultar informações: {str(e)}"}

    return {"erro": "Falha desconhecida."}