gabarito = ["A","B","C","D","E","E","D","C","B","A"]

maior = 0
menor = 10
total_alunos = 0
soma_notas = 0

while True:
    acertos = 0

    for i in range(10):
        resp = input(f"Questão {i+1}: ").upper()

        if resp == gabarito[i]:
            acertos += 1

    print("Nota:", acertos)

    maior = max(maior, acertos)
    menor = min(menor, acertos)

    soma_notas += acertos
    total_alunos += 1

    continuar = input("Outro aluno? (S/N): ").upper()

    if continuar == "N":
        break

print("Maior acerto:", maior)
print("Menor acerto:", menor)
print("Total de alunos:", total_alunos)
print("Média da turma:", soma_notas / total_alunos)
