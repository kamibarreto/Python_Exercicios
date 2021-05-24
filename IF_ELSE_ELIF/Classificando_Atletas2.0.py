from datetime import date

atual = date.today().year

ano = int(input('Em que ano Nasceu: '))

idade = atual - ano

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('CLASSIFICAÇÃO: mirim.')
elif idade <= 14:
    print('CLASSIFICAÇÃO: infantil.')
elif idade <= 19:
    print('CLASSIFICAÇÃO: junior.')
elif idade <= 25:
    print('CLASSIFICAÇÃO: sênior.')
else:
    print('CLASSIFICAÇÃO: master.')