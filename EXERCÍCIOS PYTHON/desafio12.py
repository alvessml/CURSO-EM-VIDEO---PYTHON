n = float(input("Qual é o preço do produto: R$"))
s1 = n * 5/100
s2 = n - s1
print("O produto que custava R${}, na promoção de 5% custará R${:.2f}".format(n, s2))