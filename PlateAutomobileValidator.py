import re

def extrair_numeros_telefone_internacionais(texto):
    # Expressão regular para extrair números de telefone internacionais
    padrao = r'\+\d{1,3}\s?\d{1,4}[-\s]?\d{1,12}'
    
    return re.findall(padrao, texto)

# Exemplo de uso
texto = "Entre em contato conosco no +1 123-456-7890 ou +44 20 1234 5678."
numeros = extrair_numeros_telefone_internacionais(texto)
print("Números de telefone internacionais encontrados:")
for numero in numeros:
    print(numero)
