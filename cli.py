import typer
from core.openai_handler import get_movie_insights
from rich import print_json
from storage.db_handler import init_db

app = typer.Typer()

@app.command()
def filme(titulo: str):
    """
    Consulta a IA com o título do filme e imprime as informações.
    """
    init_db()
    typer.echo(f"🎬 Consultando IA para o filme: {titulo}")
    resultado = get_movie_insights(titulo)
    print_json(data=resultado)

if __name__ == "__main__":
    app()
