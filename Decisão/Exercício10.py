"""
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"{num1} é maior!")
else:
    print(f"{num2} é maior!")

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo\nM ou F:").upper()

pesoIdeal_M = 72.7 * altura - 58
pesoIdeal_F = 62.1 * altura - 44.7

if sexo == "M":
    print(f"{altura} {sexo} - Peso ideal: {pesoIdeal_M:.1f}kg")
elif sexo == "F":
    print(f"{altura} {sexo} - Peso ideal: {pesoIdeal_F:.1f}kg")
else:
    print("Erro!")

idade = int(input("Digite sua idade: "))

if (idade >= 1) and (idade <= 13):
    print(f"{idade}: Criança")
elif (idade > 13) and (idade <= 20):
    print(f"{idade}: Adolescente")
elif (idade > 20) and (idade <= 50):
    print(f"{idade}: Adulto(a)")
elif idade > 50:
    print(f"{idade}: Idoso(a)")
else:
    print("Idade inválida!")
"""