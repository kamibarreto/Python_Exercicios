print("-------ANALISE DE PERFIL -------")

quant = int(input("Quantas pessoas será analisada? "))
acumu = femi = idade = 0
nomevelho = ""
for i in range(1, quant+1):
    print("-----{}° PESSOA-----".format(i))
    nome = input("NOME: ").upper().strip()
    idade = int(input("IDADE: "))
    sexo = input("[M/F]: ").upper().strip()

    acumu += idade
    if sexo == "M":
        if i == 1:
            velho = idade
        else:
            if idade >= velho:
                velho = idade
                nomevelho = nome
        
    if sexo == "F":
        femi += 1

media = acumu / quant

print("A media de idade do grupo é de {}".format(media))
print("O homem mais velho tem {} e se chama {}. ".format(velho, nomevelho))
print("Se tem {} mulheres com mais de 20.".format(femi))

    

