print("=" * 10, "LOJAS ALVES", "=" * 20)
preço = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2 vezes no cartão
[ 4 ] 3 ou mais no cartão""")
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcela em 2x de R${:.2f} SEM JUROS".format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totalparc = int(input("Você quer parcelar de quantas vezes? "))
    parcela = total / totalparc
    print("Sua compra será parcelada em {} de R${:.2f} COM JUROS!".format(totalparc, parcela))
else:
    total = preço
    print("\033[1:31mOPÇÃO INVALIDA\033[m de pagamento. Tente novamente!")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, total))

