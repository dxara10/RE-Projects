import re

def extrair_urls(texto):
    # Expressão regular para extrair URLs
    padrao = r'https?://\S+'

    return re.findall(padrao, texto)

# Exemplo de uso
texto = "Acesse o nosso site em https://www.example.com para obter mais informações. Visite também http://www.test.com."
urls = extrair_urls(texto)
print("URLs encontradas:")
for url in urls:
    print(url)
