import re

# Texto de exemplo contendo endereços IP
texto = "Este é um exemplo de texto contendo endereços IP como 192.168.1.1, 10.0.0.1 e 172.16.254.1."

# Expressão regular para encontrar endereços IP
padrao_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# Encontrar todos os endereços IP no texto
ips_encontrados = re.findall(padrao_ip, texto)

# Imprimir os endereços IP encontrados
print("Endereços IP encontrados:")
for ip in ips_encontrados:
    print(ip)
