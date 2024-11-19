qntd_pessoas = int(input("Digite a quantidade de pessoas: "))
contador_m = 0
contador_f = 0

for i in range(qntd_pessoas):
    qual_sexo = input(f"Qual o sexo da {i+1} pessoa (F/M): ")
    if qual_sexo == "M" or qual_sexo == "m":
        contador_m += 1
    elif qual_sexo == "F" or qual_sexo == "f":
        contador_f += 1
    else:
        pass
print(f"numero total de homens: {contador_m}\nnúmero total de mulheres: {contador_f}")