print("==" * 20)
print("         10 TERMOS DE UM P.A          ")
print("==" * 20)
pri = int(input("Primeiro termo: "))
razão = int(input("RAZÃO: "))
decimo = pri + (10 - 1) * razão
for c in range(pri, decimo + razão, razão):
    print("{}".format(c), end="➝ ")
print("ACABOU!")


