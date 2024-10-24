import re

# Função para validar um endereço residencial
def validar_endereco(endereco):
    # Expressão regular para validar um endereço residencial
    padrao_endereco = r'^\d+\s\w+\s\w+'

    if re.match(padrao_endereco, endereco):
        return True
    else:
        return False

# Endereço de exemplo a ser validado
endereco_exemplo = "123 Rua da Amostra"

# Validar o endereço
if validar_endereco(endereco_exemplo):
    print("O endereço é válido.")
else:
    print("O endereço não é válido.")
