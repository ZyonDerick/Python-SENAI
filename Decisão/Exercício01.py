n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(f"{n1} é o maior número e {n2} é o menor número.")
elif n1 < n2:
    print(f"{n2} é o maior número e {n1} é o menor número.")
else:
    print(f"O número {n1} e o número {n2} tem os mesmos valores.")