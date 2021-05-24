mais = homens = mulheres = 0

while True:
    print("-" * 30)
    print("Cadastre uma Pessoa")
    print("-" * 30)

    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]

    if idade > 18:
            mais += 1
    if sexo == "M":
            homens += 1     
    if sexo == "F": #if sexo  == "F" and idade < 20:
        if idade < 20: 
            mulheres += 1
    decisao = " "
    print("=" * 30)
    while decisao not in "SN":
        decisao = str(input("Quer continuar? [S/N]")).upper().strip()[0]

    if decisao == "N":
        break

print(f"Total  de pessoas com mais de 18 anos: {mais}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulheres} mulheres com menos de 20 anos.")
