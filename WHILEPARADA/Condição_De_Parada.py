acumu = soma = 0
while True:
    valor = int(input("Digite um valor (999 para parar): "))
    if valor  == 999:
        break
    soma += valor
    acumu += 1


print("A soma dos {} valores foi {}!".format(acumu, soma))
