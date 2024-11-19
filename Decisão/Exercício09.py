print("\nÉ maior menor ou igual a 10")
num1 = int(input("Digite um número: "))

if num1 < 10:
    print(f"{num1} é menor que 10")
elif num1 == 10:
    print(f"{num1} é igual a 10")
elif num1 > 10:
    print(f"{num1} é maior que 10")

print("\nÉ igual ou diferente")
num2 = int(input("Digite um número: "))
num3 = int(input("Digite outro número: "))

if num2 == num3:
    print(f"{num2} e {num3} são iguais")
elif num2 != num3:
    print(f"{num2} e {num3} são diferentes")

print("\nÉ ímpar ou par")
num4 = int(input("Digite um número: "))

if num4 % 2 == 1:
    print(f"{num4} é ímpar")
elif num4 % 2 == 0:
    print(f"{num4} é par")

print("\nÉ divisível ou não")
num5 = int(input("Digite um número: "))
num6 = int(input("Digite outro número: "))

if num6 == 0:
    print(f"É impossível dividir {num5} por {num6}")
elif num5 == 0:
    print(f"{num5} é divisível por {num6}")
elif (num5 % num6 == 1) or (num6 % num5 == 1):
    print(f"{num5} não é divisível por {num6}")
elif (num5 % num6 == 0) or (num6 % num5 == 0):
    print(f"{num5} é divisível por {num6}")