import re

def validar_cep(cep):
    # Expressão regular para validar CEP no formato XXXXX-XXX ou XXXXXXXX
    padrao = re.compile(r'^\d{5}-\d{3}$|^\d{8}$')
    
    if re.match(padrao, cep):
        return True
    else:
        return False

# Exemplo de uso
cep = input("Digite um CEP (no formato XXXXX-XXX ou XXXXXXXX): ")
if validar_cep(cep):
    print("CEP válido.")
else:
    print("CEP inválido. Digite no formato XXXXX-XXX ou XXXXXXXX.")
