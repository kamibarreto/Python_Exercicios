from datetime import datetime
from time import sleep

ano = int(input('Digite o ano de seu nascimento: '))

data = datetime.now()

idade = data.year - ano

print('Verificando as informações...')
sleep(3)

if idade < 18:
    print('ainda vai se alistar , pois sua idade é de {} anos.'.format(idade))
    print('falta {} ano(s) para se alistar.'.format(18 - idade))
elif idade == 18:
    print('Já esta na hora de alistar, sua idade é de {} anos.'.format(idade))
else:
    print('Já passou o tempo de se alistar, pois sua idade é {} anos'.format(idade))
    print('Você ultrapassou {} ano(s) do tempo de alistamento.'.format(idade - 18))
