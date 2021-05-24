print(10 * "-")
print("______TABUADA______")
print(10 * "-")
print("Digite um numero negativo para parar.")

while True:
    print("-" * 40)
    valor = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 40)
    valor2 = str(valor)
    if valor2[0] == "-":
        break
    acumu = 0
    while acumu < 10:
        acumu +=1
        print(f"{valor} x {acumu} = {valor*acumu}")




while True:
    n = int(input("Quer ver a tabuada de qual valor: "))
    print("-" * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {n*c}")
    print("-" * 30)
print("Programa tabuada encerrado!")