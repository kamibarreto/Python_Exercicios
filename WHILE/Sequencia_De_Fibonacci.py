print("-" * 40)
print("SEQUÊNCIA DE FIBONACCI")
print("-" * 40)
termos = int(input("Quantos termos você deseja mostrar? "))
print("~" * 40)

acumu = 0
penultimo = 0
ultimo = 1

print("{} ".format(penultimo), end=" ")

while acumu < termos: 
    resul = ultimo + penultimo    
    print("{} -".format(ultimo), end= " ")
    penultimo = ultimo
    ultimo = resul

    acumu += 1

print("Fim")


