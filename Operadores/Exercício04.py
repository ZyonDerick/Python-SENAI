nome= input("Digite seu primeiro nome: ")
sobrenome= input("Digite seu Sobrenome: ")
idade= int(input("Digite sua idade: "))
cidade= input("Digite sua cidade: ")
altura= float(input("Digite sua altura em metros: "))
peso= float(input("Digite seu peso em kg: "))
imc = peso/(altura**2)
print(f"Olá, {nome} {sobrenome} de {cidade}, seja bem vindo ao nosso sistema \nVocê tem atualmente {idade} anos e possui um indice de massa corporal de {imc:.1f}")
if imc < 18.5: 
    print("Você está magro")
elif imc >= 18.5 and imc <= 24.5:
    print("você esta em um peso normal")
elif imc >= 24.6 and imc <= 29.9:
    print("Você esta um pouco acima do peso")
elif imc > 30:
    print("você esta obeso") 