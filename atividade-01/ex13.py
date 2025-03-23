salario_base = float(input("informe seu sálario base: "))
aumento_percentual = float(input("informe o aumento percentual anual: ")) / 100
anos = int(input("informe a quantidade de anos trabalhada: "))
salario_final = salario_base

for x in range(anos):
    salario_final *= (1 + aumento_percentual)
    aumento_percentual *= 2

print(f"o salario após {anos} anos de trabalho é de: {salario_final}")
