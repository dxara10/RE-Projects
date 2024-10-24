import os

def buscar_em_arquivos(diretorio, padrao):
    resultados = []

    for pasta_raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            with open(caminho_completo, 'r', encoding='utf-8') as file:
                linhas = file.readlines()
                for numero_linha, linha in enumerate(linhas, start=1):
                    if re.search(padrao, linha):
                        resultados.append(f'{caminho_completo} - Linha {numero_linha}: {linha.strip()}')

    return resultados

if __name__ == "__main__":
    diretorio = input("Digite o diretório para busca: ")
    padrao = input("Digite o padrão de busca (expressão regular): ")

    resultados = buscar_em_arquivos(diretorio, padrao)

    if resultados:
        print("Resultados encontrados:")
        for resultado in resultados:
            print(resultado)
    else:
        print("Nenhum resultado encontrado.")
