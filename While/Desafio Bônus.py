nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

while tamanho_nome < 3:
    print("O nome deve conter mais de 3 caracteres!")
    nome = input("Digite seu nome: ")
    tamanho_nome = len(nome)

idade = int(input("Digite sua idade: "))

while idade > 150 or idade < 0:
    print("Idade tem que ser maior que 0 e menor que 150")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))

while salario < 0:
    print("Salário precisa ser maior que 0")
    salario = float(input("Digite seu sálario: "))

sexo = input("Digite seu sexo (F/M): ").upper()

while sexo not in ["M", "F"]:
    print("Sexo inválido")
    sexo = input("Digite seu sexo (F/M): ").upper()

estado_civil = input("Digite seu estado civil (S,C,V,D): ").upper()

while estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
    print("Estado civil inválido")
    estado_civil = input("Digite seu estado civil (S,C,V,D): ")

print(f"Cadastro realizado com SUCESSO!\nNome: {nome}, idade: {idade}, salario: {salario}, sexo: {sexo}, estado_civil: {estado_civil}")