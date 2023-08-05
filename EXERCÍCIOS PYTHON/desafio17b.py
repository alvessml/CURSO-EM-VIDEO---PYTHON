import math
co = float(input('Comprimento do carteto aposto: '))
ca = float(input('Comprimeto do cateto adjecente: '))
hi = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))
