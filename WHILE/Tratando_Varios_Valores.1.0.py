num1 = 999
acumu = soma = num = 0
while num1 != num:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        acumu += 1
        soma += num
print("Você digitou {} números e a soma entre eles foi de {}.".format(acumu, soma))

'''
####OUTRO MÉTODO
cont = soma = 0
num = int(input("Digite um numero [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um numero [999 para parar]: "))
print("Você digitou {} numeros e a soma entre eles foi {}.".format(cont, soma))'''