pessoas_turma = int(input("Quantas pessoas tem na turma?: "))
soma_idade = 0

for i in range(pessoas_turma):
    idade_pessoa = int(input(f"Qual a idade da {i+1} pessoa?: "))
    soma_idade += idade_pessoa

media_idade = soma_idade / pessoas_turma

if media_idade > 0 and media_idade < 25:
    print("Sua turma é majoritariamente jovem!")
elif media_idade > 25 and media_idade < 60:
    print("Sua turma é majoritariamente adulta!")
elif media_idade > 60:
    print("Sua turma é majoritariamente idosa!")