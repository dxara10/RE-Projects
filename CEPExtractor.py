import re

def extrair_cep(texto):
    # Padrão para encontrar CEPs no formato XXXXX-XXX ou XXXXXXXX
    padrao = r'\b\d{5}-\d{3}|\d{8}\b'
    ceps = re.findall(padrao, texto)
    return ceps

if __name__ == "__main__":
    texto = input("Digite o texto no qual você deseja encontrar CEPs: ")
    ceps_encontrados = extrair_cep(texto)

    if ceps_encontrados:
        print("CEPs encontrados:")
        for cep in ceps_encontrados:
            print(cep)
    else:
        print("Nenhum CEP encontrado.")
