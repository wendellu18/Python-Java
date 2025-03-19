nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))
nota3 = float(input("informe a terceira nota: "))

media_notas = (nota1 + nota2 + nota3) / 3
mediaP1_notas = (nota1 * 2) + (nota2 * 2) + (nota3 * 3) / (2 + 2 + 3)
mediaP2_notas = (nota1 * 1) + (nota2 * 2) + (nota3 * 3) / (1 + 2 + 3)

print("a media aritmétrica das notas é: ", media_notas)
print("a media ponderada com pesos 2,2,3 é: ", mediaP1_notas)
print("a média ponderada com pesos 1,2,3 é: ", mediaP2_notas)