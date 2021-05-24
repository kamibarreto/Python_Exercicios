print('{:=^40}'.format(' LOJAS BARRETO '))

valor = float(input('Qual o valor do produto: '))

dinheiro_cheque = valor - (valor * (10 / 100))

avista_cartao = valor - (valor * (5 / 100))

duas_cartao = valor

tres_cartão = valor + (valor * (20 / 100))

print('[ 1 ] Á vista dinheiro/cheque.\n[ 2 ] Á vista cartão.')
print('[ 3 ] 2x no cartão.\n[ 4 ] 3x ou mais no cartão.')

opção = int(input('Qual opção desejada? '))

if opção == 1:
    print('Sua compra ficou em R${:.2f}\nCom 10% de juros por ser avista no dinheiro/cheque.'.format(dinheiro_cheque))
elif opção == 2:
    print('Sua compra ficou em R${:.2f}\nCom 5% de juros por ser avista no cartão.'.format(avista_cartao))
elif opção == 3:
    print('Sua compra ficou em R${:.2f}\nCom preço normal pois foi em 2x no cartão'.format(duas_cartao))
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    print('ficou R${:.2f} em {}x com 20% de juros'.format(tres_cartão, parcela))
    print('O valor da parcela ficou em R${:.2f}'.format(tres_cartão / parcela))
else:
    print('*********OPÇÃO INVALIDA**********')