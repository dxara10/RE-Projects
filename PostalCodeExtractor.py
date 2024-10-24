import re

# Expressão regular para extrair códigos postais no formato "12345-678"
padrao_cep = r'\b\d{5}-\d{3}\b'

# Texto de exemplo com códigos postais
texto = "O CEP da minha casa é 12345-678 e o CEP da minha empresa é 98765-432."

# Use re.findall() para encontrar códigos postais no texto
ceps_encontrados = re.findall(padrao_cep, texto)

print("Códigos postais encontrados:")
for cep in ceps_encontrados:
    print(cep)
