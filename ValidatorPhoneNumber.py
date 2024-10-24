import re

def validar_numero_telefone(numero):
    # Expressão regular para validar números de telefone no formato (XX) XXXXX-XXXX ou XXXXX-XXXX
    padrao = re.compile(r'^\((\d{2})\)\s?(\d{5}-\d{4}|\d{4}-\d{4})$')
    
    if re.match(padrao, numero):
        return True
    else:
        return False

# Exemplo de uso
numero_telefone = input("Digite um número de telefone (no formato (XX) XXXXX-XXXX ou XXXXX-XXXX): ")
if validar_numero_telefone(numero_telefone):
    print("Número de telefone válido.")
else:
    print("Número de telefone inválido. Digite no formato (XX) XXXXX-XXXX ou XXXXX-XXXX.")
