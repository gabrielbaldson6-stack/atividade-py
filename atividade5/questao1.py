valor_divida = float(input("Digite o valor da dívida: R$ "))

print("\nValor da Dívida | Valor dos Juros | Parcelas | Valor da Parcela")

parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

for i in range(len(parcelas)):
    valor_juros = valor_divida * juros[i] / 100
    total = valor_divida + valor_juros
    valor_parcela = total / parcelas[i]

    print(f"R$ {total:.2f} | R$ {valor_juros:.2f} | {parcelas[i]} | R$ {valor_parcela:.2f}")
