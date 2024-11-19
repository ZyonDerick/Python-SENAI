idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você não precisa votar!")
elif (idade >=16) and (idade < 18):
    print("Voto facultativo!")
elif (idade >= 18) and (idade <= 70):
    print("Voto obrigatório!")
else:
    print("Voto facultativo!")