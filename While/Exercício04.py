numero_total = 0

while True:
    numero = int(input("Digite um número: "))
    numero_total += numero
    if numero == 0:
        print(f"Soma dos números = {numero_total}")