print("Gerador de PA")
print("-=" * 10)

termo = int(input("Digite o primerio termo da PA: "))
razão = int(input("Digite o valor da razão: "))
elementos = int(input("Quantos termos deseja que apareça na tela? "))

acumu = 0
acumu2 = 0
pri = termo

while acumu < elementos:
    print("{} - ".format(pri), end=" ")
    pri += razão
    acumu +=1
    acumu2 +=1
    
    if acumu == elementos:
        print("Pause")
        elementos2 = int(input("Quantos termos você quer mostrar a mais? "))
        if elementos2 != 0:
            acumu = 0
            acumu =+1
            elementos = 0
            elementos =+ elementos2 + 1

print("Progressão finalizada com {} termos mostrados: ".format(acumu2))
    