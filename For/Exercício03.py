qntd_pares = 0

for i in range(100):
    calculo_pares = i % 2
    if calculo_pares == 0:
        qntd_pares += 1
print(f"Quantidade de números pares entre 1 e 100: {qntd_pares}")