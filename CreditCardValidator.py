import re

def validar_cartao_credito(numero):
    # Expressão regular para validar números de cartão de crédito
    padrao = re.compile(r'^\d{4}-\d{4}-\d{4}-\d{4}$|^\d{16}$')
    
    if re.match(padrao, numero):
        return True
    else:
        return False

# Exemplo de uso
numero_cartao = input("Digite um número de cartão de crédito (no formato XXXX-XXXX-XXXX-XXXX ou XXXXXXXXXXXXXXXX): ")
if validar_cartao_credito(numero_cartao):
    print("Número de cartão de crédito válido.")
else:
    print("Número de cartão de crédito inválido. Digite no formato XXXX-XXXX-XXXX-XXXX ou XXXXXXXXXXXXXXXX.")
