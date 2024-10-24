import re

def processar_texto_com_marcacao(texto):
    # Expressões regulares para encontrar marcações e aplicar formatação
    negrito = re.compile(r'\*\*(.*?)\*\*')
    italico = re.compile(r'_(.*?)_')
    
    # Aplicar formatação para negrito e itálico
    texto_formatado = negrito.sub(r'<b>\1</b>', texto)
    texto_formatado = italico.sub(r'<i>\1</i>', texto_formatado)
    
    return texto_formatado

# Exemplo de uso
texto_original = "Este é um exemplo **de texto** com _marcações_."
texto_formatado = processar_texto_com_marcacao(texto_original)
print(texto_formatado)
