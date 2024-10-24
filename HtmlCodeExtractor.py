import re

def extrair_codigo_fonte_html(texto):
    # Padrão para encontrar código HTML em um texto
    padrao = r'<.*?>'
    codigo_fonte = re.sub(padrao, '', texto)
    return codigo_fonte

if __name__ == "__main__":
    texto = input("Digite o texto contendo código HTML: ")
    codigo_fonte_html = extrair_codigo_fonte_html(texto)
    print("Código Fonte HTML Extraído:")
    print(codigo_fonte_html)
