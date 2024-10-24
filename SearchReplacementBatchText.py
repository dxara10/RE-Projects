import os
import re

# Diretório onde os arquivos .txt estão localizados
diretorio = "caminho/para/seu/diretorio"

# Palavra a ser substituída
palavra_antiga = "palavra_antiga"
palavra_nova = "palavra_nova"

# Expressão regular para encontrar a palavra antiga
padrao = re.compile(r'\b' + re.escape(palavra_antiga) + r'\b')

# Percorre todos os arquivos .txt no diretório
for root, _, files in os.walk(diretorio):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)

            # Abre o arquivo, lê seu conteúdo e substitui a palavra
            with open(file_path, 'r') as f:
                conteudo = f.read()
                conteudo_modificado = re.sub(padrao, palavra_nova, conteudo)

            # Escreve o conteúdo modificado de volta no arquivo
            with open(file_path, 'w') as f:
                f.write(conteudo_modificado)

print("Substituição de texto em lote concluída.")
