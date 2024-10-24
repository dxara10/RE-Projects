import re

def extrair_numeros_telefone(texto):
    padrao = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    numeros = re.findall(padrao, texto)
    return numeros

if __name__ == "__main__":
    texto = input("Digite o texto no qual você deseja encontrar números de telefone: ")
    numeros = extrair_numeros_telefone(texto)

    if numeros:
        print("Números de telefone encontrados:")
        for numero in numeros:
            print(numero)
    else:
        print("Nenhum número de telefone encontrado.")
