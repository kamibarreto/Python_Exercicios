print("-" * 40)
print("Loja Super BARATÃO")
print("-" * 40)

barato = total = mil = 0
nome  = " "

while True:
    produto = str(input("Nome do Produto: "))
    preço =  float(input("Preço: "))
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if preço > 1:
        barato = preço
        nome = produto
    else:
        if preço < barato:
            barato = preço
            nome = produto
        if preço  > 1000:
            mil += 1
            total += preço
    if escolha == "N":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi de R${total}.")
print(f"Temos {mil} produtos custando mais de R$1000.00.")
print(f"O produto mais barato foi {nome} que custou R${barato}.")    