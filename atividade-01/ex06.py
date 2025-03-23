def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero // 2) + 1):
        if numero % i == 0:
            return False
    return True

primos = []
numero = 2

while len(primos) < 100:
    if e_primo(numero):
        primos.append(numero)
    numero += 1

print(primos)
