import requests
import omdb

def buscar_filme_por_titulo(titulo):
    #Chave da API.
    api_key = "d2929aeb"

    #url base da API OMDB de filmes
    base_url = "http://www.omdbapi.com/"

    #parametros da consulta
    params = {
        "apikey": api_key,
        "t": titulo
    }

    #solicitação a api
    response = requests.get(base_url, params=params)

    #verf da solicit
    if response.status_code == 200:
        filme = response.json()
        if filme["Response"] == "True":
            #print dos dados do filme
            print(f"** Dados do Filme **")
            print(f"Título: {filme['Title']}")
            print(f"Ano de Lançamento: {filme['Year']}")
            print(f"Classificação Indicativa: {filme['Rated']}")
            print(f"Gênero: {filme['Genre']}")
            print(f"Diretor: {filme['Director']}")
            print(f"Resumo/Sinopse: {filme['Plot']}")
        else:
            print("Filme não encontrado.")
    else:
        print("Erro na solicitação a API.")

if __name__ == "__main__":
    titulo = input("Digite o título do filme que deseja pesquisar: ")
    buscar_filme_por_titulo(titulo)
