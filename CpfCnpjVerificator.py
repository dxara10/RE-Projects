import re

def validar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador do CPF
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 == 10 or digito1 == 11:
        digito1 = 0

    # Verifica o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador do CPF
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 == 10 or digito2 == 11:
        digito2 = 0

    # Verifica o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False

    return True

def validar_cnpj(cnpj):
    # Remove caracteres não numéricos do CNPJ
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    
    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False

    # Calcula o primeiro dígito verificador do CNPJ
    soma = 0
    for i in range(4):
        soma += int(cnpj[i]) * (5 - i)
    for i in range(8, 12):
        soma += int(cnpj[i]) * (13 - i)
    digito1 = 11 - (soma % 11)
    if digito1 == 10 or digito1 == 11:
        digito1 = 0

    # Verifica o primeiro dígito verificador
    if digito1 != int(cnpj[12]):
        return False

    # Calcula o segundo dígito verificador do CNPJ
    soma = 0
    for i in range(5):
        soma += int(cnpj[i]) * (6 - i)
    for i in range(8, 13):
        soma += int(cnpj[i]) * (14 - i)
    digito2 = 11 - (soma % 11)
    if digito2 == 10 or digito2 == 11:
        digito2 = 0

    # Verifica o segundo dígito verificador
    if digito2 != int(cnpj[13]):
        return False

    return True

# Teste de validação de CPF e CNPJ
cpf_valido = validar_cpf("123.456.789-09")
cnpj_valido = validar_cnpj("12.345.678/0001-01")

if cpf_valido:
    print("CPF válido.")
else:
    print("CPF inválido.")

if cnpj_valido:
    print("CNPJ válido.")
else:
    print("CNPJ inválido.")
