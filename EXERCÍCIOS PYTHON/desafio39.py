from datetime import date
atual = date.today().year
nasc = int(input("Ano de nacimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar \033[1:31mIMEDIATAMENTE\033[m!")
elif idade < 18:
    falta = 18 - idade
    alistamento = atual + falta
    print("Ainda faltam {} anos para o alistamento.".format(falta))
    print("\033[1:32mSeu alistamento será em {}\033[m.".format(alistamento))
elif idade > 18:
    atrasado = idade - 18
    alistamento = atual - atrasado
    print("Você ja deveria ter se alistado há {} anos atrás.".format(atrasado))
    print("\033[1:33mSeu alistamento foi em {}\033[m.".format(alistamento))
    
