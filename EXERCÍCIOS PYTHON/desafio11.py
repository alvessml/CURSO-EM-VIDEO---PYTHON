l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
area = l * a
pin = area / 2
print("Sua parede tem uma dimensão de {}x{} e sua área é de {}m².".format(l, a, area))
print("Para pintar essa parede, você precisará de {:.4}l de tinta".format(pin))