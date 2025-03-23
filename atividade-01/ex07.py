impar = 0
antecessor = 0
prox_ímpar = 0
dif = 0

while True:

    impar = int(input("informe um número ímpar: "))
    if impar % 2 == 0:
         print("o número informado não é ímpar")
         pass
    else:
        antecessor = (impar - 1) ** 2
        prox_ímpar = impar + 2
        if antecessor > prox_ímpar:
            dif = antecessor - prox_ímpar
        else:
           dif = prox_ímpar - antecessor
        print(f"A diferença entre o quadrado do antecessor de {impar} e {prox_ímpar} é: {dif}")
        break
