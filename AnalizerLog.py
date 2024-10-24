import re

def analisar_log(log, padrao):
    return re.findall(padrao, log)

# Exemplo de uso
log = "2023-09-18 08:30:45 - Erro: Ocorreu um erro inesperado no servidor."
padrao = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
resultados = analisar_log(log, padrao)
print("Datas encontradas:")
for resultado in resultados:
    print(resultado)
