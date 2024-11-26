notas = []
soma = 0
total_notas = 0

while len(notas) < 4:
  nota = float(input("Digite sua nota: "))
  notas.append(nota)

for i in notas:
  print(f"Nota {total_notas+1}: {i}")
  soma += i
  total_notas += 1
print(f"Média das notas: {soma/total_notas}")