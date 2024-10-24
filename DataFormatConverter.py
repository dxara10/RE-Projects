import re

# Expressão regular para encontrar datas no formato "dd/mm/aaaa"
data_pattern = r'(\d{2})/(\d{2})/(\d{4})'

# Função para substituir o formato da data
def converter_data(match):
    dia, mes, ano = match.groups()
    nova_data = f"{ano}-{mes}-{dia}"
    return nova_data

# Texto de exemplo com datas no formato "dd/mm/aaaa"
texto = "A data de nascimento é 25/12/1990 e o evento ocorreu em 30/04/2022."

# Use re.sub() com a função de substituição para converter as datas
texto_convertido = re.sub(data_pattern, converter_data, texto)

print(texto_convertido)
