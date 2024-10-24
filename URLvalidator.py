import re

def validar_url(url):
    # Padrão para validar URLs simples
    padrao = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    return bool(re.match(padrao, url))

if __name__ == "__main__":
    url = input("Digite a URL a ser validada: ")
    if validar_url(url):
        print("URL válida.")
    else:
        print("URL inválida.")
