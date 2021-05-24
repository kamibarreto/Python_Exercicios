from time import sleep

print('------------ CONVERSOR NUMERICO-------------')
sleep(2)

numero = int(input('Digite um valor inteiro: ')) 

hexadecimal = hex(numero)[2:]
binario  = bin(numero)[2:]
octal = oct(numero)[2:]

print('Qual a opção de conversão:\n[ 1 ] Binario.\n[ 2 ] Hexadecimal\n[ 3 ] Octal')

opção = int(input('Digite a opção desejada: '))

if opção == 1:
    print('{} convertido para Binarios é igual a {}'.format(numero, binario))
elif opção == 2:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hexadecimal))
elif opção == 3:
    print('{} convertido para Octal é igual á {}'.format(numero, octal))
else:
    print('**opção invalda***')