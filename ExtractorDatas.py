import re

def extrair_datas(texto):
    # Expressão regular para extrair datas no formato DD/MM/AAAA
    padrao = r'\b(\d{2}/\d{2}/\d{4})\b'
    
    return re.findall(padrao, texto)

# Exemplo de uso
texto = "A reunião está marcada para o dia 18/09/2023. Não esqueça da data 22/10/2023."
datas = extrair_datas(texto)
print("Datas encontradas:")
for data in datas:
    print(data)
