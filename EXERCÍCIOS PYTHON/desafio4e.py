n = input('Digite algo: ')
print("O tipo primitivo desse valor é ", type(n))
print("Só tem espaços? ", n.isspace())
print("É um número? ", n.isnumeric())
print("É um alfabeto? ", n.isalpha())
print("É um alfanumérico", n.isalnum())
print("Está em maiusculas? ", n.isupper())
print("Está em minusculas? ", n.islower())
print("Está capitalizada? ", n.istitle())
