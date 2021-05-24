acumulador = 0
cont = 0 
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end=" ")
        acumulador +=i
        cont +=1

print(8 * "-")

print("No intervalo de 1 a 500, se tem {} numeros divisiveis por 3.".format(cont))
print("A soma entre todo os multiplos de 3 é: {}".format(acumulador))
