"""
numero_treino = int(input("Digite um número que você deseja treinar: "))
erros = 0
acertos = 0

for i in range(1,11):
    resposta_numero = int(input(f"Qual o valor da tabuada {numero_treino} x {i}: "))
    calculo = numero_treino * i
    if calculo != resposta_numero:
        print(f"VOCÊ ERROU, O VALOR CORRETO É {calculo}")
        erros += 1
    elif calculo == resposta_numero:
        print(f"CORRETO")
        acertos += 1
print(f"Total de acerto: {acertos}\nTotal de erros: {erros}")
"""

erros = 0
acertos = 0
repetir = 0

while True:
    numero_treino = int(input("Digite o número da tabuada que deseja treinar: "))
    numero_repetir = int(input("Digite até qual tabuada você quer fazer: "))

    while repetir < numero_repetir:
        repetir += 1
        resposta_numero = int(input(f"Qual o valor da tabuada {numero_treino} x {repetir}: "))
        calculo = numero_treino * repetir

        if resposta_numero != calculo:
            print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É {calculo}")
            erros += 1
        elif resposta_numero == calculo:
            print(f"CORRETO!")
            acertos += 1
        
        if repetir == numero_repetir:
            print(f"Total de acerto: {acertos}\nTotal de erros: {erros}")
            pergunta = input("Você deseja jogar novamentew (S/N): ").upper()
        
    if pergunta == "S":
        erros = 0
        acertos = 0
        repetir = 0
    elif pergunta == "N":
        break