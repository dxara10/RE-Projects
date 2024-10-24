from bs4 import BeautifulSoup
import requests
import re

# URL da página da web de exemplo
url = "https://example.com"

# Realize uma solicitação HTTP para obter o conteúdo da página
response = requests.get(url)
html = response.text

# Use BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontre todos os links na página usando expressões regulares
links = soup.find_all('a', href=re.compile(r'https://example\.com/.*'))

# Extraia e imprima os títulos e URLs dos links
for link in links:
    title = link.text
    url = link['href']
    print(f"Link Title: {title}, URL: {url}")
