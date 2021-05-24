from random import randint

print("=-" * 40)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=" * 40)
acumu = 0

while True:
    pc = randint(0, 10)
    valor = int(input("Diga um valor: "))
    escolha = str(input("PAR ou Ímpar: [P/I]")).upper().strip()
    soma = valor + pc
    while escolha[0] not in 'PI':
        escolha = str(input("Opção invalida. PAR ou ÍMPAR: [P/I] ")).upper().strip()
    print(F"Você jogou {valor} e o computador {pc}. Total de {soma} DEU", end=" ")
    if soma % 2 == 0:
        print("PAR")
        if escolha[0] == "P":
            print("Você VENCEU!!!")
        else:
            print("Você PERDEU!!!")
            break
    else:
        print("ÍMPAR")
        if escolha[0] == "I":
            print("Você VENCEU!!!")
        else:
            print("Você PERDEU!!!")
            break
    acumu += 1
print(f"GAME OVER! Voce venceu {acumu} vezes.")