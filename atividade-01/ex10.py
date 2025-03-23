numero = 0
while True:
    numero = int(input("informe um número: "))
    if numero <= 1:
        print("o número informado é inválido")
        break
    cont = 0
    for x in range(2, numero): 
        if numero % x == 0:
            cont += 1
            break
    if cont == 0:
        print(f"o número {numero} é primo")
        break
    else:
        print(f"o número {numero} não é primo")
        break
