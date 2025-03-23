n1 = float(input("informe um primeiro número: "))
n2 = float(input("informe um segundo número: "))
n3 = float(input("informe um terceiro número: "))

if n1 == n2 and n1 > n3:
    print(f"o primeiro e segundo número são iguais a {n1} e ambos são maiores que {n3}")
elif n1 == n3 and n1 > n2:
    print(f"o primeiro e terceiro número são e iguais a {n1} e ambos são maiores que {n2}")
elif n2 == n3 and n2 > n1:
    print(f" o segundo e terceiro número são iguais a {n2} e ambos são maiores que {n1}")
elif n1 == n2 == n3:
    print(f"os três números são iguais a: {n1} ")
elif n1 > n2 > n3:
    print(f"o maior número é: {n1} e o menor é {n3}")