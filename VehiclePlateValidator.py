import re

# Função para validar uma lista de placas de veículo brasileiras (padrão Mercosul)
def validar_placas(placas):
    # Expressão regular para validar uma placa de veículo no novo padrão brasileiro (Mercosul)
    padrao_placa = r'^[A-Z]{3}\d[A-Z]\d{2}$'

    placas_validas = []
    placas_invalidas = []

    for placa in placas:
        if re.match(padrao_placa, placa):
            placas_validas.append(placa)
        else:
            placas_invalidas.append(placa)

    return placas_validas, placas_invalidas

# Lista de placas de exemplo a serem validadas
placas_exemplo = ["AAA1A11", "XYZ2B22", "1234CDE", "MNO5F55"]

# Validar as placas
placas_validas, placas_invalidas = validar_placas(placas_exemplo)

print("Placas válidas:")
for placa in placas_validas:
    print(placa)

print("\nPlacas inválidas:")
for placa in placas_invalidas:
    print(placa)
