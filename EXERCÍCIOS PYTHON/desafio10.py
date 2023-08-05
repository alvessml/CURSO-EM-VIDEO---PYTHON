real = float(input("Quantos você tem na carteira? R$"))
dollar = 5.19 * real
euro = 6.17 * real
print("Com R$", real, "você pode comprar ${:.2f}".format(dollar))
print("Com R$ {} você pode comprar €{:.2f}".format(real, euro))