from time import sleep

print('*********Descubra qual triângulo é:*************')
sleep(2)

l1 = float(input('Digite a primeira reta em cm: '))
l2 = float(input('Digite a segunda reta em cm: '))
l3 = float(input('Digite a terceira reta em cm: '))

print('Calculando...')
sleep(3)

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    if l1 == l2 and l1 == l3: #if l1 == l2 == l3:
        print('Este é um triângulo equilátero, pois possue todos os lados iguais.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
            print('Este é um triângulo esósceles, pois possue dois lados iguais.')
    elif l1 != l2 and l1 != l3 and l2 != l3: # if l1 != l2 != l3 != l1:
        print('Este é um triangulo escaleno, pois possue todos os lados diferentes.')
else:
    print('Os valores apresentados não podem formar um triângulo.')