from random import randint
v = 0

while True:
    jogador =  int(input("Digite um valor: "))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I]")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {pc}. Total de {total}", end=" b")
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("você VENCEU!!!")
            v += 1
        else:
            print("Você PERDEU!!!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU!!!")
            v += 1
        else:
            print("Você VENCEU!!!")
            break
    print("Vamos jogar novamente...")

print(f"GAME OVER!! Você venceu {v} vezes.")