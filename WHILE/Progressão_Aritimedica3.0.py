termo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite o valor da razão: "))
elementos =  int(input("Quantos elementos deseja inserir na tela: "))

acumu = 0
pri = termo

while acumu < elementos:
    print("{} - ".format(pri), end=" ")
    pri += razão
    acumu += 1
print("FIM")