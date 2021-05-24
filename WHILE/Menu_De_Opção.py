from time import sleep

print("------------------MENU DE OPÇÃO-------------------")

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
opção = 0
while opção != 5:
    print(''' OPÇÕES:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA    
    ''')
    opção = int(input("Digite a opção desejada: "))
    while opção > 5:
        opção = int(input("Opção invalida, digite a opção desejada: "))
    if opção == 1:
        print("Calculando...")
        sleep(2)
        print("{} + {} = {}".format(valor1, valor2, valor1+valor2))
        sleep(3)
    elif opção == 2:
        print("Calculando...")
        sleep(2)
        print("{} x {} = {}".format(valor1, valor2, valor1*valor2))
        sleep(3)
    elif opção == 3:
        lis = [valor1, valor2]
        order  = sorted(lis)
        print("O maior valor digitado foi {}.".format(order[1]))
        sleep(2)
    elif opção == 4:
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))

print("Obrigado por utilizar nosso programa! ᕦ( ͡° ͜ʖ ͡°)ᕤ ")
