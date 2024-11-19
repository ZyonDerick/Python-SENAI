# imprimir gol da alemanha 7 vezes

"""
gols = 0
while gols < 7:
    gols = gols + 1
    print("Gol da Alemanha")

print("Gol do Brasil")
"""

#Somando valor até ser igual a 10
"""
valor = 0
while valor < 10:
    valor = valor + 1
    print(valor)
"""

#Somando os valores
"""
contador = 1
soma = 0
while contador <= 5:
    soma = soma + contador
    contador = contador + 1
print(f"A soma é {soma}")
"""

#Usando Else no While
"""x = 0
while x < 10:
    print(f"O valor de x nesta interação é {x}")
    print("X ainda é menor que 10. somando 1 a x")
    x = x + 1
else:
    print("O valor de x é 10\nAcabou o Loop")"""

#Printando até acertar o valor
"""
valor = int(input("Quanto é 2 + 2:"))
while valor != 4:
    print("Errou!")
    valor = int(input("Quanto é 2 + 2:"))
else:
    print("Você acertou!")
"""

#Pass, break
"""
valor = 0
while valor < 10:
    if valor == 4:
        #break #Para o código!
        continue
    else:
        #Nenhuma ação específica
        pass #Instrução Nula
    print(valor)
    valor = valor + 1
"""

#Média da sala de aula usando while
"""
notas = 0
qtd_notas = 0

while True:
    nota = float(input("Informe a nota (-1 para finalizar): "))
    if nota == -1:
        break
    notas += nota
    qtd_notas += 1

if qtd_notas > 0:
    print(f"Quantidade de notas informadas {qtd_notas}")
    print(f"A média da sala foi de {notas / qtd_notas:.2f}")
else:
    print("Nenhuma nota informada!")
"""