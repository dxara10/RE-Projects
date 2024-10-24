import re

def filtrar_dados(texto, padrao):
    return re.findall(padrao, texto)

# Exemplo de uso
texto = "Lorem ipsum 42 dolor sit amet, consectetur adipiscing elit. Fusce 12345 euismod 6789."
padrao = r'\d+'
resultados = filtrar_dados(texto, padrao)
print("Números encontrados:")
for resultado in resultados:
    print(resultado)
