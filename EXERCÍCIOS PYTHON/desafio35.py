print('-='*20)
print('Analizador de triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmentos acima PODEM FORMAR triângulo.')
else:
    print('o segmentos acima NÃO PODEM FORMAR triângulo.')
