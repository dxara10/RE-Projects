import re

# Expressão regular para extrair códigos de cupons promocionais
padrao_cupom = r'[A-Z0-9]{6}-[A-Z0-9]{6}'

# Texto de exemplo com códigos de cupons
texto = "Use o código promocional ABC123-DEF456 para obter um desconto de 20%. Válido até XYZ789-UVW123."

# Use re.findall() para encontrar códigos de cupons no texto
cupons = re.findall(padrao_cupom, texto)

print("Códigos de cupons encontrados:")
for cupom in cupons:
    print(cupom)
