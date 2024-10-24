import re

# Função para limpar um texto
def limpar_texto(texto):
    # Remover caracteres especiais e números
    texto = re.sub(r'[^a-zA-Z\s]', '', texto)
    
    # Remover espaços em excesso
    texto = re.sub(r'\s+', ' ', texto)
    
    # Converter para letras minúsculas
    texto = texto.lower()
    
    return texto

# Texto de exemplo a ser limpo
texto_exemplo = "Este é um exemplo de  texto, com vários caracteres especiais, números e   espaços em excesso!"

# Limpar o texto
texto_limpo = limpar_texto(texto_exemplo)

print("Texto original:", texto_exemplo)
print("Texto limpo:", texto_limpo)
