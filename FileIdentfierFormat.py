import re

def identificar_formato_arquivo(arquivo):
    # Dicionário de padrões de assinaturas binárias para formatos de arquivo conhecidos
    padroes_formatos = {
        "JPEG": b'\xFF\xD8\xFF',
        "PNG": b'\x89\x50\x4E\x47',
        "PDF": b'\x25\x50\x44\x46\x2D',
        # Adicione mais formatos conforme necessário
    }
    
    with open(arquivo, 'rb') as f:
        dados = f.read(4)
        for formato, padrao in padroes_formatos.items():
            if dados.startswith(padrao):
                return formato
    
    return "Formato desconhecido"

# Exemplo de uso
arquivo = "exemplo.jpg"  # Substitua pelo nome do seu arquivo
formato = identificar_formato_arquivo(arquivo)
print(f"O formato do arquivo '{arquivo}' é: {formato}")
