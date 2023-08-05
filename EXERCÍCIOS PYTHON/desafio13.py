n = float(input("Qual é o salário do Funcionário? R$"))
sla = n + (n * 15/100)
print("Um fucionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}".format(n, sla))
