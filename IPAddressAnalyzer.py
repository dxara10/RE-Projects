import re

def analisar_enderecos_ip(texto):
    # Expressão regular para encontrar endereços IP
    padrao = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    
    enderecos = re.findall(padrao, texto)
    
    categorias = {
        'IPv4': [],
        'IPv6': [],
    }
    
    for endereco in enderecos:
        if '.' in endereco:
            categorias['IPv4'].append(endereco)
        else:
            categorias['IPv6'].append(endereco)
    
    return categorias

# Exemplo de uso
texto = "Endereços IP válidos na rede: 192.168.1.1, 2001:0db8:85a3:0000:0000:8a2e:0370:7334."
resultados = analisar_enderecos_ip(texto)
print("Endereços IPv4 encontrados:")
print(resultados['IPv4'])
print("Endereços IPv6 encontrados:")
print(resultados['IPv6'])
