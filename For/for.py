for i in range(7):
    print("Gol da alemanha")

for i in range(3):
    print(i)

#range (inicio, fim, salto)
for contador in range(0,11,2):
    print(contador)

#for usando listas
notas_alunos = [10,9,7,8,5]
for i in notas_alunos:
    print(i)

#usando break para parar o for
for gol in range(1000):
    print("Gol da alemanha!")
    if gol == 6:
        break
print("Chega de gol")
print("Gol do Brasil")

#Usando o comando continue e else
for i in [1,10,20,30,35,40,50]:
    if i == 35:
        continue
    print(i)
else:
    print("Acabou")

#Somandos os valores limitado a 50
inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o último número: "))
salto = int(input("Digite o salto: "))
total = 0
texto = "Calculo: "

for numero in range(inicio,fim,salto):
    total += numero
    texto = texto + str(numero)
    if numero >= 50:
        break
    if numero != fim -1:
        texto = texto + " + "
print(texto)
print(total)

#Calcular a média de nota dos alunos
qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))
total = 0
for aluno in range(qtd_alunos):
    nota = float(input(f"Digite a nota do {aluno+1} aluno: "))
    total += nota
print(f"A média da turma é: {total/qtd_alunos}")