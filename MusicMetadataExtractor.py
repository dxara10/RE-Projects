import re

# Expressões regulares para extrair metadados de música
padrao_titulo = r'Título: (.*)'
padrao_artista = r'Artista: (.*)'
padrao_album = r'Álbum: (.*)'
padrao_ano = r'Ano de Lançamento: (\d{4})'

# Texto de exemplo com metadados de música
metadados_musica = """
Título: Música de Exemplo
Artista: Artista da Música
Álbum: Álbum de Exemplo
Ano de Lançamento: 2022
"""

# Extrair metadados da música usando expressões regulares
titulo = re.search(padrao_titulo, metadados_musica).group(1)
artista = re.search(padrao_artista, metadados_musica).group(1)
album = re.search(padrao_album, metadados_musica).group(1)
ano = re.search(padrao_ano, metadados_musica).group(1)

# Imprimir os metadados extraídos
print(f"Título: {titulo}")
print(f"Artista: {artista}")
print(f"Álbum: {album}")
print(f"Ano de Lançamento: {ano}")
