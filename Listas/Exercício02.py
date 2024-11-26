numeros = []

while len(numeros) < 10:
  numero = float(input("Digite um número: "))
  numeros.append(numero)

numeros.reverse()

for i in numeros:
  print(i)