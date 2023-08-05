from random import randint
from time import sleep
computador = randint(1, 10) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 1 a 10. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tentar adivinhar
print(('PROCESSANDO...'))
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
