from time import sleep


print("-----------10 TERMOS DE UMA PA----------")

sleep(2)


pri = int(input("Digite o Primeiro termo: "))
raz = int(input("Digite a razão da PA: "))
ele = int(input("Quantos elementos deseja inserir na tela? "))

ulti = pri + (ele - 1) * raz
ulti += 1

for i in range(raz, ulti, raz):
    print(i)

