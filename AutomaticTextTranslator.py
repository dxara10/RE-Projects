import re

# Dicionário de tradução de palavras-chave
traducoes = {
    "hello": "olá",
    "world": "mundo",
    "example": "exemplo"
}

# Função para traduzir texto com base no dicionário
def traduzir_texto(texto):
    padrao = re.compile(r'\b(' + '|'.join(map(re.escape, traducoes.keys())) + r')\b')
    resultado = padrao.sub(lambda x: traducoes[x.group()], texto)
    return resultado

# Texto de exemplo a ser traduzido
texto = "Hello, world! This is an example of text translation."

# Traduzir o texto
texto_traduzido = traduzir_texto(texto)

print("Texto original:", texto)
print("Texto traduzido:", texto_traduzido)
