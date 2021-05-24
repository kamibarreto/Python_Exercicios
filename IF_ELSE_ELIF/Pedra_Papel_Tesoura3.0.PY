from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int (input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-=' * 11)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))

if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print('EMPATE.')
    elif jogador == 1:
        print('Jogador venceu.')
    elif jogador == 2:
        print('Computador venceu.')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
            print('Computador venceu.')
    elif jogador == 1:
            print('EMPATE')
    elif jogador == 2:
            print('Jogador venceu.')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
            print('Computador venceu')
    elif jogador == 2:
        print('Empate.')
else:
    print('*****invalido******')