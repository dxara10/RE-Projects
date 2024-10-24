import re

def extrair_dominio(url):
    # Padrão para extrair o domínio de uma URL
    padrao = r'^(https?|ftp)://([^\s/$.?#].[^\s]*)'
    match = re.match(padrao, url)
    if match:
        return match.group(2)
    else:
        return None

if __name__ == "__main__":
    url = input("Digite a URL para extrair o domínio: ")
    dominio = extrair_dominio(url)
    if dominio:
        print(f"Domínio extraído: {dominio}")
    else:
        print("URL inválida.")
