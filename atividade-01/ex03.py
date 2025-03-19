valor = float(input("informe o valor de suas compras: "))
if valor <= 500:
    print("este valor esta isento de taxas")
else:
    taxa = (valor / 2)
    valor_total = valor + taxa
    print("com a adição das taxas o valor foi corrigido para: ", valor_total)