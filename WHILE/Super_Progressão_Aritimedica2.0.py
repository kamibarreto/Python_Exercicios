print("GAERADOR DE PA")
print("-=" * 10)

primerio = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))

termo = primerio
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print("{} - ".format(termo), end=" ")
        termo += razão
        cont +=1
    print("PAUSA")
    mais = int(int(input("Quantos termos você quer mostrar a mais? ")))
print("Progressão finalizada com {} termos finalizada.".format(total))