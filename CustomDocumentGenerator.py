import re

# Modelo de documento com espaços reservados
modelo_documento = "Olá [NOME], seu número de telefone é [TELEFONE]."

# Dicionário de informações para preencher no documento
informacoes = {
    "NOME": "João da Silva",
    "TELEFONE": "123-456-7890"
}

# Função para preencher o modelo de documento com informações
def preencher_documento(modelo, informacoes):
    for chave, valor in informacoes.items():
        modelo = re.sub(r'\[' + chave + r'\]', valor, modelo)
    return modelo

# Preencher o modelo de documento com informações
documento_preenchido = preencher_documento(modelo_documento, informacoes)

print("Documento personalizado:")
print(documento_preenchido)
