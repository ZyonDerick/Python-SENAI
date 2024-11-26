numeros = []
impar = []
par = []
contador = 0

while contador < 20:
    numero_digitado = int(input("Digite um numero: "))
    numeros.append(numero_digitado)
    contador += 1
for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f"Números digitados: {numeros}\nNúmeros pares: {par}\nNúmeros ímpares: {impar}")