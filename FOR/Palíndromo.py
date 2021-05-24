nome = input("Digite um nome: ")

sem = nome.replace(" ", "")

frase = sem[::-1]

if sem == frase:
    print("é um polimonio")
else:
    print("não é um polinomio")

