from time import sleep


valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos deseja pagar a casa? '))

prestacao =  valor_casa /  (anos * 12)

porcento = (salario / 100) * 30

print('Aguarde, estamos calculando...')
sleep(3)

if prestacao > porcento:
    print('Seu emprestimo foi negado!')
else:
    print('Parabens, seu emprestimo foi aprovado!', end=" ")
    print('A prestação será de R${:.2f} mensalmente'.format(prestacao))
   
