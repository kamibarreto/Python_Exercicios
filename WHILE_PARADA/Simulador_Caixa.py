print("{:-^40}".format("Banco CEV"))
cem = cinquenta = vinte = dez = um = 0

while True:
    valor =  int(input("Qual o valor que deseja sacar: R$"))
    if valor >= 100:
        cem =  int(valor / 100)
        valor = valor - (cem * 100)
    if valor >= 50:
        cinquenta = int(valor/50)
        valor = valor - (cinquenta *50)
    if valor >=20:
        vinte = int(valor/20)
        valor = valor - (vinte*20)
    if valor >= 10:
        dez = int(valor/10)
        valor = valor - (dez*10)
    if valor >= 1:
        um =  int(valor/1)
        valor = valor - (um*1)
    break

if cem != 0:
    print(f"Total de {cem} cedulas de R$100")
if cinquenta != 0:
    print(f"Total de {cinquenta} cedulas de R$50")
if vinte != 0:
    print(f"Total de {vinte} cedulas de R$20")
if dez != 0:
    print(f"Total de {dez} cedulas de R$10")
if um != 0:
    print(f"Total de {um} cedulas de R$1")