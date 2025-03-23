turmas = int(input("quantas turmas? "))
alunos_total = 0

for i in range(turmas):
    alunos = int(input(f"digite a quantidade de alunos na turma {i+1}: "))
    if alunos > 40:
        print(f"a turma {i+1} possui mais de 40 alunos!")
    alunos_total += alunos

media_alunos = alunos_total / turmas
print(f"a média de alunos por turma é: {media_alunos}")
