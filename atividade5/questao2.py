faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

while True:
    numero = float(input("Digite um número: "))

    if numero < 0:
        break

    if 0 <= numero <= 25:
        faixa1 += 1
    elif 26 <= numero <= 50:
        faixa2 += 1
    elif 51 <= numero <= 75:
        faixa3 += 1
    elif 76 <= numero <= 100:
        faixa4 += 1

print("\nResultado:")
print(f"[0-25]: {faixa1}")
print(f"[26-50]: {faixa2}")
print(f"[51-75]: {faixa3}")
print(f"[76-100]: {faixa4}")
