print("--------------Contador de soma de pares------------")

acumulador = 0

for i in range (0, 6):
    nume = int(input("Digite um valor: "))
    if nume % 2 == 0:
        print("{} é um numero par".format(nume))
        acumulador += nume
    else:
        print("{} é um numero impar, neste caso não faz parte da contagem.".format(nume))

print("A soma de todos os numeros pares é {};".format(acumulador))