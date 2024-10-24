import re

def validar_senha_forte(senha):
    # A senha deve ter pelo menos 8 caracteres, incluindo letras maiúsculas,
    # minúsculas, números e caracteres especiais.
    padrao = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(padrao, senha))

if __name__ == "__main__":
    senha = input("Digite a senha a ser validada: ")
    if validar_senha_forte(senha):
        print("Senha forte válida.")
    else:
        print("Senha fraca ou inválida.")
