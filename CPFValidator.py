import re

def validar_cpf(cpf):
    # Expressão regular para validar CPF
    padrao = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$')
    
    if re.match(padrao, cpf):
        return True
    else:
        return False

# Exemplo de uso
cpf = input("Digite um CPF (no formato XXX.XXX.XXX-XX ou XXXXXXXXXXX): ")
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido. Digite no formato XXX.XXX.XXX-XX ou XXXXXXXXXXX.")
