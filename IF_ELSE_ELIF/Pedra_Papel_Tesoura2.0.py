from time import sleep 
from random import randint

def joken(desejo):
    print('================= Vamos jogar Jokenpo==================')
    print('Carrgando as opções...')
    sleep(3)
    
    opção = desejo * 1

    while desejo == opção:  
        print('[ 1 ] papel.\n[ 2 ] Pedra.\n[ 3 ] Tesoura.')
        
        escolha = int(input('Qual opção desejada? '))

        pc = randint(1, 3)

        print('Jogando contra a maquina...')
        sleep(4)

        print(20 * "=")
        if pc == 1:
            if escolha == 1:
                print('Raciocinio igual a uma maquina. EMPATE!')
                print('Jogador: PAPEL x Maquina: PAPEL')
            elif escolha == 2:
                print('A maquina foi mais esperta. LOSER!')
                print('Jogador: PEDRA x Maquina: PAPEL')
            elif escolha == 3:
                print('Parabens, você foi um vitorioso. WINS!')
                print('Jogador: TESOURA x Maquina:PAPEL')

        if pc == 2:
            if escolha == 1:
                print('Parabens ao jogador, saiu vitorioso. WINS!')
                print('Jogador: PAPEL x Maquina: PEDRA ')
            elif escolha == 2:
                print('Raciocinou igual uma maquina. EMPATE!')
                print('Jogador: PEDRA x Maquina: PEDRA')
            elif escolha == 3:
                print('Parece que a maquina é mais esperta. LOSER!')
                print('Jogador: TESOURA x Maquina: PEDRA')

        if pc == 3:
            if escolha == 1:
                print('Parece que você perdeu. LOSER!')
                print('Jogador: PAPEL x Maquina: TESOURA')
            elif escolha == 2:
                print('Você foi esperto, parabêns. WINS!')
                print('Jogador: PEDRA x Maquina: TESOURA')
            elif escolha == 3:
                print('Pensou igualmente a maquina, hmmm sei não... EMPATE')
                print('Jogador: TESOURA x Maquina: TESOURA ')
        opção = int(input('Deseja jogar novamente?\n [ 1 ] SIM.\n [ 2 ] NÃO.\nOPÇÃO DESEJADA: '))
        if opção == 1:
            print('*******Vamos novamente então*********')


if __name__ == '__main__':
    joken(1)