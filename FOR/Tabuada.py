print("-----------Tabuada de 0 a 10-----------")

tabu =  int(input("Qual o valor da tabuada: "))

for i in range(0, 11,):
    print("{} x {:2} = {}".format(tabu, i, tabu * i))