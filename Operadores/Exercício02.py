#Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número
"""num1 = int(input("Digite um número: "))
print(f"O quadrado deste número é: {num1 ** 2}")

#Faça um Programa que cadastre(Nome,Sobrenome,Idade,RA) peça as 4 notas bimestrais e mostre a média.
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
ra = int(input("Digite seu RA: "))

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
nota3 = int(input("Digite sua terceira nota: "))
nota4 = int(input("Digite sua quarta nota: "))

print(f"Nome: {nome} {sobrenome}")
print(f"Idade: {idade}")
print(f"RA: {ra}")
print(f"Média: {(nota1 + nota2 + nota3 + nota4)/4:.1f}")"""

#Crie um programa que peça um número e logo em seguida exiba a tabuada desse número
numero = int(input("Digite um número"))
for i in range(1,11):
    print(f"{numero}x{i} = {numero*i}")
    
