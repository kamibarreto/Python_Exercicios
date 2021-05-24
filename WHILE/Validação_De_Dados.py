print("------Validação de dados------")

sexo = input("Informe seu sexo: [M/F] ").upper()

while sexo != "M" and sexo != "F":
        sexo = input("Dados informado invalido. Por favor informe seu sexo: ").upper()

if sexo == "M":
    print("Sexo Masculino registrado com sucesso.")
else:
    print("Sexo feminino registrado com sucesso.")


'''
###OUTRA FORMA

sexo = str(input("Informe seu sexo: [M/F] )).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos. Informe novamente seu sexo: )).strip().upper()[0]

print("Sexo {} registrado com sucesso.".formart(sexo))'''

