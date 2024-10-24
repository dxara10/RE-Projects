import re

def validar_email(email):
    # Expressão regular para validar e-mails
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(padrao, email):
        return True
    else:
        return False

# Exemplo de uso
email = input("Digite um endereço de e-mail: ")
if validar_email(email):
    print("E-mail válido.")
else:
    print("E-mail inválido.")
