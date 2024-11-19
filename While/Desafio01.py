while True:
    resposta = input("Você gosta de Python? (S/N): ").upper()
    if resposta == "S":
        print(f"({resposta}) Resposta correta!")
        break
    elif resposta == "N":
        print(f"({resposta}) Que pena!")
        break
    elif (resposta != "S") and (resposta != "N"):
        print(f"({resposta}) esta não é uma resposta válida!")
        break