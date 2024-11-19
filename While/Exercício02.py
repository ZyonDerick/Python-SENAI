turmas = int(input("Digite a quantidade de turmas na unidade: "))
contador = 0
soma = 0
while contador < turmas:
    alunos = int(f"Digite a quantidade de alunos da turmas {contador+1}: ")
    if alunos <= 40:
        contador += 1
        soma += alunos
    else:
        print("O numero de alunos não pode passar de 40")
print(f"A média das turmas é {soma/turmas:.0f}")