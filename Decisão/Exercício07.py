print("-- Reservatório de água --")
altura =  int(input("Digite a altura (cm): "))
largura = int(input("Digite a largura (cm): "))
comprimento = int(input("Digite o comprimento (cm): "))
consumo_medio = int(input("Digite o valor do consumo médio diário (litros/dia): "))

metro_cubico = (altura * comprimento * largura) / 1000
reservatorio = metro_cubico / consumo_medio

print(f"Capacidade do reservatório = {metro_cubico}")
print(f"Autonomia do reservatório = {reservatorio} dias")

if reservatorio < 2:
    print("Consumo elevado")
elif (reservatorio >= 2) and (reservatorio <= 7):
    print("Consumo moderado")
elif (reservatorio > 7):
    print("Consumo reduzido")