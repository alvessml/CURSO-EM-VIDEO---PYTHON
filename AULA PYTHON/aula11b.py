from random import randint
from time import sleep
computador = randint(1, 5)
print('Vou pensar em um número de 1 á 5, \033[1;32mTENTE ADVINHAR!!!\033[m')
print(('PROCESSANDO...'))
sleep(3)
jogador = int(input('Em que número eu pensei? '))
if computador == jogador:
    print('\033[1;4;32mVOCÊ ME VENCEU, PARABÉNS!!!\033[m')
else:
    print('\033[1;2;31mERROU\033[m, eu pensei em {} tente outra vez.'.format(computador))
