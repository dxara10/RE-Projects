import re

# Exemplo de um log de servidor
log = """
192.168.1.1 - - [10/Mar/2023:10:45:32] "GET /page1 HTTP/1.1" 200 3402
192.168.1.2 - - [10/Mar/2023:10:46:20] "GET /page2 HTTP/1.1" 404 1234
192.168.1.3 - - [10/Mar/2023:10:47:15] "GET /page1 HTTP/1.1" 200 6543
"""

# Expressão regular para extrair endereços IP e URLs do log
pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(GET|POST) (.*?) HTTP/1.1" (\d+) (\d+)'

matches = re.findall(pattern, log)
for match in matches:
    ip, timestamp, method, url, status, bytes_sent = match
    print(f"IP: {ip}, Timestamp: {timestamp}, Method: {method}, URL: {url}, Status: {status}, Bytes Sent: {bytes_sent}")
