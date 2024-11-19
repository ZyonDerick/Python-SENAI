numeros = int(input("Digite a quantidade de números: "))
soma_numero = 0

for i in range(numeros):
    numero = int(input(f"Qual o valor do número {i+1}: "))
    soma_numero += numero
print(f"A média dos números digitados é: {soma_numero / numeros}")