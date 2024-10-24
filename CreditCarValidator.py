import re

# Expressão regular para validar números de cartões de crédito
padrao_cartao = r'^\d{13,19}$'

# Função para validar números de cartão de crédito usando o algoritmo de Luhn
def validar_cartao(numero):
    numero = list(map(int, numero[::-1]))
    total = sum(numero[0::2]) + sum(sum(divmod(d * 2, 10)) for d in numero[1::2])
    return total % 10 == 0

# Números de cartão de crédito de exemplo
cartoes = ["4532015112830366", "6011000990139424", "378282246310005", "1234567890123456"]

for cartao in cartoes:
    if re.match(padrao_cartao, cartao) and validar_cartao(cartao):
        print(f"Cartão válido: {cartao}")
    else:
        print(f"Cartão inválido: {cartao}")
