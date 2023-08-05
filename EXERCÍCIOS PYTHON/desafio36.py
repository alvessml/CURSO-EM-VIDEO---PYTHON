casa = float(input("Valor da casa: "))
salariocom = float(input("Salário do comprador: "))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salariocom * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos ".format(casa, anos), end='')
print("a prestação será de R${:.2f}.".format(prestação))
if prestação <= minimo:
    print('Salário pode ser CONCEDIDO.')
else:
    print('Salário NÃO CONCEDIDO.')

