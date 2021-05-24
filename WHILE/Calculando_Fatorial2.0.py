fator = int(input("Digite um numero para calcular o seu fatorial: "))

acumu = fator
multi = 1

print("Fatorial {}! = ".format(fator), end='')

while acumu > 0:
    print("{}".format(acumu), end="")
    print(" x " if acumu > 1 else ' = ', end='')
    multi *= acumu
    acumu -= 1
print(multi)
