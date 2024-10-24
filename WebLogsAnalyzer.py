import re

def analisar_log_web(log, padrao):
    return re.findall(padrao, log)

# Exemplo de uso
log = "192.168.1.1 - - [18/Sep/2023:08:30:45 -0400] 'GET /page HTTP/1.1' 200 1234"
padrao = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b|\[([^\[\]]+)\]|\b\d{3}\b'
resultados = analisar_log_web(log, padrao)
print("Informações encontradas:")
for resultado in resultados:
    print(resultado)
