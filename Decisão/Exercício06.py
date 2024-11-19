n1 = float(input("Digite um número: "))
n2 = float(input("Digite o outro número: "))
operação = input("Qual operação você deseja fazer?: ").upper()

if operação == "SOMA":
    print(f"A soma dos números é {n1 + n2}")
elif operação == "SUBTRAÇÃO":
    print(f"A subtração dos números é {n1 - n2}")
elif operação == "MULTIPLICAÇÃO":
    print(f"A multiplicação dos números é {n1 * n2}")
elif operação == "DIVISÃO":
    print(f"A divisão dos números é {n1 / n2}")
else:
    print("Operação inválida, tente novamente.")