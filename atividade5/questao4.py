candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulos = 0
brancos = 0

print("1 - José")
print("2 - João")
print("3 - Maria")
print("4 - Ana")
print("5 - Nulo")
print("6 - Branco")
print("0 - Encerrar")

while True:
    voto = int(input("Digite seu voto: "))

    if voto == 0:
        break

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1

total = candidato1 + candidato2 + candidato3 + candidato4 + nulos + brancos

print("\nResultado da Eleição")
print("José:", candidato1)
print("João:", candidato2)
print("Maria:", candidato3)
print("Ana:", candidato4)
print("Nulos:", nulos)
print("Brancos:", brancos)

if total > 0:
    print(f"% Nulos: {(nulos/total)*100:.2f}%")
    print(f"% Brancos: {(brancos/total)*100:.2f}%")
