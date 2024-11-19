estado_civil = input("Digite seu estado civil.\nOpções (C, S, D, V, O): ").upper()

if estado_civil == "C":
    print(f"{estado_civil} - Casado(a)")
elif estado_civil == "S":
    print(f"{estado_civil} - Solteiro(a)")
elif estado_civil == "D":
    print(f"{estado_civil} - Divorciado(a)")
elif estado_civil == "V":
    print(f"{estado_civil} - Viúvo(a)")
elif estado_civil == "O":
    print(f"{estado_civil} - Outro")
else:
    print("Essa opção não é válida!")