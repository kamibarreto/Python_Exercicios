from datetime import date
print('---------------Analise da idade de pessoas-------------')

ano_atual= date.today().year
maior = 0
menor = 0

for i in range(1, 7):
    data = int(input("Em que ano você nasceu? "))
    idade = ano_atual - data
    print("sua idade é {}.".format(idade))

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print("Se tem {} pessoas de maior.".format(maior))
print("Se tem {} pessoas de menor.".format(menor))
