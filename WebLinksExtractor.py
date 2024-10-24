import re
import requests

def extrair_links_pagina(url):
    try:
        resposta = requests.get(url)
        conteudo = resposta.text
        links = re.findall(r'href=["\'](https?://.*?)(?=["\'])', conteudo)
        return links
    except Exception as e:
        print(f"Erro ao extrair links: {str(e)}")
        return []

if __name__ == "__main__":
    url = input("Digite a URL da página da web para extrair links: ")
    links = extrair_links_pagina(url)

    if links:
        print("Links encontrados:")
        for link in links:
            print(link)
    else:
        print("Nenhum link encontrado.")
