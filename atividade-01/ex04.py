custo_diario = 90
kilometragem = int(input("informe a quantidade de km rodados: "))
if kilometragem <= 100:
        print("o valor total do aluguel do veiculo é de: ", custo_diario, "R$")
else:
        distancia_excedente = kilometragem - 100
        valor_adicional = distancia_excedente * 12
        valor_total = custo_diario + valor_adicional
        print("o valor total do aluguel do veiculo é de:", valor_total, "R$")