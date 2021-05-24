nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media =  (nota1 + nota2) / 2

if media < 5.0:
    print('Reprovado! Sua media foi {:.2f}.'.format(media))
elif media < 6.9:
    print('Recuperação!Sua media foi {:.2f}.'.format(media))
else:
    print('Parabéns! Você foi aprovado! Sua media foi {:.2f}.'.format(media))
print(30 * '=')
print('Continue estudando, os estudos são tudo e tudo acaba não sendo nada - ainstein o grande')