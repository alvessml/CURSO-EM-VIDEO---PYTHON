from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print("""Suas opções:
 [ 0.1 ] PEDRA
 [ 0.1 ] PAPEL
 [ 0.1 ] TESOURA""")
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-=" * 14)
print("Computadou jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=" * 14)

if computador == 0: # PEDRA
    if jogador == 0:
        print("EMPATOU")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("\033[1:31mJOGADA INVÁLIDA\033[m")

elif computador == 1: # PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATOU")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("\033[1:31mJOGADA INVÁLIDA\033[m")

elif computador == 2: # TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATOU")
    else:
        print("\033[1:31mJOGADA INVÁLIDA\033[m")
