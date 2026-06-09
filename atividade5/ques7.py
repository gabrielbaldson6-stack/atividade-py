nome = input("Nome do atleta: ")

notas = []

for i in range(7):
    notas.append(float(input("Nota: ")))

melhor = max(notas)
pior = min(notas)

notas.remove(melhor)
notas.remove(pior)

media = sum(notas) / len(notas)

print("Atleta:", nome)
print("Melhor nota:", melhor)
print("Pior nota:", pior)
print("Média:", round(media,2))
