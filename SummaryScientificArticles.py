import re

# Expressões regulares para extrair informações de um artigo científico
padrao_autores = r'Autores: (.*)'
padrao_data = r'Data de Publicação: (\d{2}/\d{2}/\d{4})'
padrao_resultados = r'Resultados: (.*)'

# Texto de exemplo de um artigo científico
artigo = """
Título: Descoberta de um Novo Medicamento

Autores: John Doe, Jane Smith

Data de Publicação: 15/09/2022

Resumo: Este artigo descreve a pesquisa e os resultados da descoberta de um novo medicamento para tratar doenças.

Resultados: O medicamento mostrou eficácia em 95% dos casos testados.
"""

# Extrair informações do artigo usando expressões regulares
autores = re.search(padrao_autores, artigo).group(1)
data_publicacao = re.search(padrao_data, artigo).group(1)
resultados = re.search(padrao_resultados, artigo).group(1)

# Imprimir as informações extraídas
print(f"Autores: {autores}")
print(f"Data de Publicação: {data_publicacao}")
print(f"Resultados: {resultados}")
