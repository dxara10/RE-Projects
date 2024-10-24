import re

# Função para analisar um arquivo de código fonte
def analisar_codigo_fonte(arquivo):
    with open(arquivo, 'r') as f:
        codigo = f.read()
    
    # Encontrar variáveis no código
    variaveis = re.findall(r'\w+\s*=\s*.+', codigo)
    
    # Encontrar funções no código
    funcoes = re.findall(r'def\s+\w+\s*\(', codigo)
    
    # Encontrar comentários no código
    comentarios = re.findall(r'#.*', codigo)
    
    # Imprimir as informações encontradas
    print("Variáveis encontradas:")
    for variavel in variaveis:
        print(variavel)
    
    print("\nFunções encontradas:")
    for funcao in funcoes:
        print(funcao)
    
    print("\nComentários encontrados:")
    for comentario in comentarios:
        print(comentario)

# Nome do arquivo de código fonte a ser analisado
arquivo_codigo_fonte = "codigo_fonte.py"

# Executar a análise do código fonte
analisar_codigo_fonte(arquivo_codigo_fonte)
