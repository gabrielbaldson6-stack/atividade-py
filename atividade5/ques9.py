n = int(input("Quantidade de termos: "))

soma = 0
den = 1

for num in range(1, n+1):
    soma += num / den
    den += 2

print("Soma =", soma)
