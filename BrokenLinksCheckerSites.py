import requests
from bs4 import BeautifulSoup
import re

# URL do site a ser verificado
url = "https://example.com"

# Realize uma solicitação HTTP para obter o conteúdo da página
response = requests.get(url)
html = response.text

# Use BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontre todos os links na página
links = soup.find_all('a', href=True)

for link in links:
    link_url = link['href']
    if not re.match(r'http', link_url):  # Verifique se o link é relativo
        link_url = url + link_url  # Converta para um URL absoluto

    try:
        # Faça uma solicitação HEAD para verificar se o link está ativo
        response = requests.head(link_url)
        if response.status_code == 200:
            print(f"Link válido: {link_url}")
        else:
            print(f"Link quebrado: {link_url}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao verificar o link: {link_url}")
