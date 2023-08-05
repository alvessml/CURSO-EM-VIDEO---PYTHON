peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / altura ** 2
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO do peso!")
elif imc < 24.9:
    print("PARABÉNS, você está com o PESO IDEAL!")
elif imc < 30:
    print("Você está com SOBREPESO!")
elif imc < 40:
    print("Você está com OBESIDADE!")
else:
    print("Você está com OBESIDADE MÓRBIDA!")

