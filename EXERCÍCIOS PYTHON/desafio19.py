import random
pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
qua = input('Quarto aluno: ')
lista = [pri, seg, ter, qua]
sort = random.choice(lista)
print('O aluno sorteado foi {}'.format(sort))
