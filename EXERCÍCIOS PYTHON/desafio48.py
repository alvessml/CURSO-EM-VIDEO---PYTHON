soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
       # cont = cont + 1
        soma += n
       # soma = soma + n
       #print(soma)
print("A soam de todos os {} valores solicitados é {}".format(cont, soma))
