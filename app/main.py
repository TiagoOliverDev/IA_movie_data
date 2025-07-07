import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.openai_handler import get_movie_insights

if __name__ == "__main__":
    titulo = input("Digite o título do filme: ")
    resultado = get_movie_insights(titulo)
    print("\nResposta:\n")
    print(resultado)
