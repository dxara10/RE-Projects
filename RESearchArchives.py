import re
import os

def pesquisar_em_arquivos(padrao, diretorio):
    resultados = []

    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(raiz, arquivo)
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                correspondencias = re.findall(padrao, conteudo)
                if correspondencias:
                    resultados.append((caminho_arquivo, correspondencias))

    return resultados

# Exemplo de uso
padrao = r'\bexpressao_regular\b'
diretorio = '.'  # Diretório atual, você pode especificar um diretório diferente
resultados = pesquisar_em_arquivos(padrao, diretorio)

if resultados:
    print("Correspondências encontradas:")
    for caminho_arquivo, correspondencias in resultados:
        print(f"Arquivo: {caminho_arquivo}")
        for correspondencia in correspondencias:
            print(f"  - {correspondencia}")
else:
    print("Nenhuma correspondência encontrada.")
