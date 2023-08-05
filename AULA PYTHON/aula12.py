nome = str(input('Qual é o seu nome? '))
if nome == "Samuel":
    print("Que nome bonito!")
elif nome == "Maria" or nome == "Thalles" or nome == "Gabriel":
    print("Seu nome e bem popular no Brasil!")
elif nome in "Ana Gabriela Juliana Jessica":
    print("Belo nome feminino!")
else:
    print("Seu nome e bem normal!")
print("Tenha um Bom dia, {}!".format(nome))
