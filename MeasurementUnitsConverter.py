import re

# Função para converter unidades de medida
def converter_unidades(texto):
    # Expressões regulares para identificar unidades de medida
    padrao_metros = r'(\d+)\s*metros?'
    padrao_pes = r'(\d+)\s*pés?'
    
    # Converter metros para pés
    texto = re.sub(padrao_metros, lambda x: f'{float(x.group(1)) * 3.28084:.2f} pés', texto)
    
    # Converter pés para metros
    texto = re.sub(padrao_pes, lambda x: f'{float(x.group(1)) / 3.28084:.2f} metros', texto)
    
    return texto

# Texto de exemplo com unidades de medida
texto_com_medidas = "A sala tem 5 metros de comprimento e 10 pés de largura."

# Converter unidades de medida no texto
texto_convertido = converter_unidades(texto_com_medidas)

print("Texto original:", texto_com_medidas)
print("Texto convertido:", texto_convertido)
