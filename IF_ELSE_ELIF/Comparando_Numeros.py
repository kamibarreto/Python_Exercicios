primeiro = int(input('Digite valor: '))
segundo = int(input('Digite outro valor: '))
ordem = sorted([primeiro, segundo])
#o sorted ele coloca em forma crescente, e precisa estar em uma lista

if primeiro > segundo:
    print('O valor {} é o maior!'.format(ordem[1]))
elif primeiro < segundo:
    print('O valor {} é o maior!'.format(ordem[1]))
else:
    print('os valores atribuidos são iguais!')