def romano_para_arabico(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabico = 0
    anterior = 0

    for algarismo in romano[::-1]:
        valor = valores[algarismo]
        if valor < anterior:
            arabico -= valor
        else:
            arabico += valor
        anterior = valor

    return arabico

if __name__ == "__main__":
    numero_romano = input("Digite um número em algarismos romanos: ")
    numero_arabico = romano_para_arabico(numero_romano.upper())
    print(f"O número em algarismos arábicos é: {numero_arabico}")
