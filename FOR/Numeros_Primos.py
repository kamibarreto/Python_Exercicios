print("----------Numeros primos------------")

primo = int(input("Digite um numero: "))

acumu = 0


for i in range(1, primo+1):
    if primo % i == 0:
        acumu += 1
if acumu == 2:
    print("Este numero é primo. ")
else:
    print("Este numero não primo. ")