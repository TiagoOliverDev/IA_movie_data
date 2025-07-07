import json
from openai import OpenAI
from config.config import OPENAI_API_KEY, OPENAI_MODEL
from utils.logger import logger

client = OpenAI(api_key=OPENAI_API_KEY)


def get_movie_insights(title: str) -> dict:
    """
    Consulta a OpenAI para obter informações sobre um filme.

    Parâmetros:
        title (str): Título do filme.

    Retorno:
        dict: Contendo data de lançamento, bilheteria e sinopse,
              ou mensagem de erro caso não encontre ou falhe.
    """
    logger.info(f"Iniciando consulta para o filme: {title}")

    try:
        prompt = (
            f"Você é um assistente de cinema. Responda apenas em JSON com as seguintes informações "
            f"sobre o filme '{title}': data de lançamento, bilheteria aproximada em dólares, "
            f"e uma sinopse curta. O JSON deve ter os campos: data_lancamento, bilheteria, sinopse. "
            f"Se não encontrar informações sobre o filme, responda com o seguinte JSON: "
            f'{{"erro": "Filme não encontrado"}}'
        )

        logger.debug(f"Prompt enviado para OpenAI: {prompt}")

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            max_tokens=300,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        resposta_texto = response.choices[0].message.content.strip()
        logger.debug(f"Resposta bruta da OpenAI: {resposta_texto}")

        try:
            resultado = json.loads(resposta_texto)
        except json.JSONDecodeError:
            logger.warning("Resposta da OpenAI não está em formato JSON válido.")
            return {"erro": "Resposta inválida da IA. Tente novamente."}

        if "erro" in resultado:
            logger.warning(f"Filme não encontrado: {title}")
            return {"erro": "Filme não encontrado. Verifique o título e tente novamente."}

        campos_esperados = {"data_lancamento", "bilheteria", "sinopse"}
        if not campos_esperados.issubset(resultado.keys()):
            logger.warning("Resposta incompleta da IA.")
            return {"erro": "Informações incompletas retornadas. Tente novamente."}

        logger.info(f"Consulta bem-sucedida para o filme '{title}'")
        return resultado

    except Exception as e:
        logger.error(f"Erro inesperado ao consultar informações do filme '{title}': {str(e)}", exc_info=True)
        return {"erro": f"Erro ao consultar informações: {str(e)}"}