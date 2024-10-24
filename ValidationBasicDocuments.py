import re

# Função para validar CPF
def validar_cpf(cpf):
    # Expressão regular para CPF
    cpf_regex = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    return bool(cpf_regex.match(cpf))

# Função para validar CNPJ
def validar_cnpj(cnpj):
    # Expressão regular para CNPJ
    cnpj_regex = re.compile(r'^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$')
    return bool(cnpj_regex.match(cnpj))

# Função para validar RG
def validar_rg(rg):
    # Expressão regular para RG (formato: XX.XXX.XXX-X)
    rg_regex = re.compile(r'^\d{2}\.\d{3}\.\d{3}-\d{1}$')
    return bool(rg_regex.match(rg))

# Função para validar número de telefone
def validar_telefone(telefone):
    # Expressão regular para número de telefone (formato: (XX) XXXXX-XXXX)
    telefone_regex = re.compile(r'^\(\d{2}\) \d{5}-\d{4}$')
    return bool(telefone_regex.match(telefone))

# Solicitar ao usuário o tipo de documento e o documento
tipo_documento = input("Escolha o tipo de documento (CPF, CNPJ, RG, Telefone): ").upper()
documento = input("Insira o documento: ")

if tipo_documento == 'CPF':
    if validar_cpf(documento):
        print("CPF válido.")
    else:
        print("CPF inválido.")
elif tipo_documento == 'CNPJ':
    if validar_cnpj(documento):
        print("CNPJ válido.")
    else:
        print("CNPJ inválido.")
elif tipo_documento == 'RG':
    if validar_rg(documento):
        print("RG válido.")
    else:
        print("RG inválido.")
elif tipo_documento == 'TELEFONE':
    if validar_telefone(documento):
        print("Número de telefone válido.")
    else:
        print("Número de telefone inválido.")
else:
    print("Tipo de documento não suportado.")
