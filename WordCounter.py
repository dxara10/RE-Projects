import re

def contar_palavras_chave(texto, palavra_chave):
    # Expressão regular para encontrar a palavra-chave
    padrao = re.compile(r'\b' + re.escape(palavra_chave) + r'\b', re.IGNORECASE)
    
    ocorrencias = len(re.findall(padrao, texto))
    return ocorrencias

# Exemplo de uso
texto = "Python é uma linguagem de programação. Programar em python é fácil e Python é popular."
palavra_chave = "Python"
ocorrencias = contar_palavras_chave(texto, palavra_chave)
print(f"A palavra-chave '{palavra_chave}' ocorre {ocorrencias} vezes no texto.")
