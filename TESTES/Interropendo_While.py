soma = 0
while True:
    n = int(input("Digite um numéro: "))
    if n == 999:
        break
    soma += n
print("A soma vale {}".format(soma))