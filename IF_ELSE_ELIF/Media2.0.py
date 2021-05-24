nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if 7 > media >= 5: #if media >= 5 and media < 7:
    print('O aluno esta de RECUPERAÇÃO!')
elif media < 5:
    print('O aluno esta reprovado.')
elif media >= 7:
    print('Aluno esta aprovado')