nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade= input("Digite sua idade: ")
tempo = float(input("Quantas horas você trabalha por dia? : "))
money = float(input("Quanto você ganha por horas trabalhadas? : "))
semana = int(input("Quantos dias do mês você trabalha? :"))
mes = 30-semana 
mess = 30-mes
print(f"Olá, {nome} {sobrenome} seja bem vindo ao nosso sistema!")
print(f"Atualmente tendo {idade} anos")
print(f"você recebe {tempo*money} por dia!")
print(f"vocÊ recebe {tempo*money*mess} por mês e trabalha por {tempo*mess}")
