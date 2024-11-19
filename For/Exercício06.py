import time

print("Bem-vindo as eleições!")

eleitores = int(input("Digite a quantidade de eleitores: "))
thomas_Shelby = 0
zyon_Derick = 0
harry_Potter = 0

for eleitor in range(eleitores):
    time.sleep(1)
    print("=" * 100)
    print("Escolha um dos candidatos abaixo!\n\n\n")
    print("Thomas Shelby (22)           Zyon Derick (15)           Harry Potter (18)\n\n\n")
    print("=" * 100)
    voto = int(input("Digite o número do candidato: "))

    if voto == 22:
        thomas_Shelby += 1
    elif voto == 15:
        zyon_Derick += 1
    elif voto == 18:
        harry_Potter += 1

    print("=" * 100)
    print("\n\n\n VOTO CONFIRMADO! \n\n\n")
    print("=" * 100)
    time.sleep(3)

def imprimir_podio():

    eleitores = [
        ("Thomas Shelby", thomas_Shelby),
        ("Harry Potter", harry_Potter),
        ("Zyon Derick", zyon_Derick)
    ]
    
    eleitores.sort(key=lambda x: x[1], reverse=True)

    print("=" * 100)
    print("\n\n\nAPURAÇÃO DOS VOTOS!\n\n")
    for eleitor, votos in eleitores:
        print(f"{eleitor}: ", "|" * votos, f"{votos} votos!")
    print("=" * 100)

imprimir_podio()