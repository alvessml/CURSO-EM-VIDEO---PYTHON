n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
mf = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(mf))
print('Parabéns!' if mf >= 6 else 'Estude mais!')
