import re

# Expressão regular para encontrar números de telefone no formato (123) 456-7890
padrao_telefone = r'\(\d{3}\) \d{3}-\d{4}'

# Texto de exemplo com números de telefone
texto = "Entre em contato conosco pelo telefone (123) 456-7890 ou visite nosso site."

# Use re.findall() para encontrar números de telefone no texto
numeros_telefone = re.findall(padrao_telefone, texto)

print("Números de telefone encontrados:")
for numero in numeros_telefone:
    print(numero)
