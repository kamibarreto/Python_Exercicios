maior = 0
menor = 9000000
for i in range(1, 6):
    peso = float(input("Digite o peso da {}° pessoa: ".format(i)))

    if peso >= maior:
        maior = peso
    
    if peso <= menor:
        menor = peso

print("O maior peso lido é {}.".format(maior))
print("O menor peso lido é {}.".format(menor))