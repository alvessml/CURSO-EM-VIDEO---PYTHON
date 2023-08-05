l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))
if  l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos acimas PODEM FORMAR um triângulo ", end="")
    if l1 == l2 == l3:
        print("EQUILÁTERO!")
    elif l1 != l2 != l3 != l1:
        print("ESCALENO!")
    else:
        print("ISÓCELES!")
else:
    print('OS segmentos acima NÃO PODEM formar um triângulo.')