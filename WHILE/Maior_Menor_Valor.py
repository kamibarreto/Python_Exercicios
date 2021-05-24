decisão = "S"

acumu = maior = todos = 0
menor = 90000000

while decisão not in "Nn":
    num = int(input("Digite um número: "))
    decisão = str(input("Deseja Continuar? [S/N] "))
    while decisão not in "SsNn":
        decisão =str(input("Opção invalida, Deseja continuar? [S/N] "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    
    acumu += 1
    todos += num
print("Você digitou {} números e a media foi {}.".format(acumu, todos/acumu))
print("O maior valor foi {}, e o menor foi {}.".format(maior, menor))
