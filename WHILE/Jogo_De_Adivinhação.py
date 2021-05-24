from time import sleep
from random import randint
print("----------Jogo de adivinhação---------")
sleep(2)


aleat = randint(0, 10)

acumu = 1
deci =  str(input("Prazer, sou seu computador, vamos jogar? [S/N] ")).upper().split()[0]

while deci not in "SsNn":
    deci = str(input("OPÇÃO INVALIDA, DIGITE UM OPÇÃO VALIDA. [S/N] ")).upper().split()[0]

if deci == "N":
    print("Parece que vc arregou, na proxima jogaremos então.( ͡~ ͜ʖ ͡°)")
else:
    print("Correto, então vamos começar (▀̿Ĺ̯▀̿ ̿). ")
    print("Deixa eu pensar...")
    sleep(3)
    chute =  int(input("Pensei em um numero de 0 a 10, qual foi? "))
     
    while chute !=  aleat:
        print("Parece que você errou ¯\_(ツ)_/¯.")
        acumu += 1
        if chute < aleat:
            chute = int(input("Tente de novo, um pouco mais, meu amigo: ( ͡° ʖ̯ ͡°)  "))
        else: 
            chute = int(input("Tente de novo, um pouco menos, meu amigo: (ง ͠° ͟ل͜ ͡°)ง "))

    print("Parabens, você acertou, com {} tentativa(s). ( ✧≖ ͜ʖ≖) ".format(acumu))