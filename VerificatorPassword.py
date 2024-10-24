import re

def verificar_senha_forte(senha):
    # Expressão regular para verificar senhas fortes
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if re.match(padrao, senha):
        return True
    else:
        return False

# Exemplo de uso
senha = input("Digite uma senha: ")
if verificar_senha_forte(senha):
    print("Senha forte.")
else:
    print("Senha fraca. A senha deve conter pelo menos 8 caracteres, incluindo maiúsculas, minúsculas, números e caracteres especiais.")
