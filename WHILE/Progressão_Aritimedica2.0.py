termo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite o valor da razão: "))
elementos =  int(input("Quantos elementos deseja inserir na tela: "))

ulti = termo + (elementos - 1) * razão
pa = termo


while pa < ulti + razão:
    print("{} ".format(pa), end="↛ ")     
    pa += razão
print("FIM")