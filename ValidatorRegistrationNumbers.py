import re

def validar_numero_registro_nacional(registro):
    # Expressão regular para validar números de registro nacional (por exemplo, RG no Brasil)
    padrao = re.compile(r'^\d{1,10}$')
    
    if re.match(padrao, registro):
        return True
    else:
        return False

# Exemplo de uso
registro = input("Digite um número de registro nacional (por exemplo, RG): ")
if validar_numero_registro_nacional(registro):
    print("Número de registro nacional válido.")
else:
    print("Número de registro nacional inválido. Digite no formato numérico.")
