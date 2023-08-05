n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
média = (n1 + n2) /2
if média > 7:
    print("Tirando {} e {}, a média do aluno é {:.1f}".format(n1, n2, média))
    print("O aluno está \033[1:32mAPROVADO\033[m.")
elif 7 > média >= 5:
    print("Tirando {} e {}, a média do aluno é {:.1f}".format(n1, n2, média))
    print("O aluno está em \033[1:33mRECUPERAÇÃO\033[m.")
else:
    print("Tirando {} e {}, a média do aluno é {:.1f}".format(n1, n2, média))
    print("O aluno está \033[1:31mREPROVADO\033[m.")