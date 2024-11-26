consoantes = ["a", "e", "i", "o", "u"]
palavra_digitada = input("Digite uma palavra: ")
total_vogais = 0
total_consoantes = 0

for letra in list(palavra_digitada):
  if letra in consoantes:
    print(f"{letra}: é vogal")
    total_vogais += 1
  else:
    print(f"{letra}: é consoante")
    total_consoantes += 1
print(f"Total de vogais: {total_vogais}\nTotal de consoantes: {total_consoantes}")