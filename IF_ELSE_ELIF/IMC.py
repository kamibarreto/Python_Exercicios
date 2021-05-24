peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Digite sua altura: (m) '))

imc = peso / (altura * altura) or (altura ** 2)

if imc < 18.5:
    print('Você esta abaixo do peso.')
elif imc <= 25: #elif 18.5 <= imc < 25:
    print('Esta no peso ideal.')
elif imc <= 30: #elif 25 <= imc < 30:
    print('Esta sobrepeso.')
elif imc <= 40: #elif 30 <= imc <40:
    print('Esta com obesidade.')
else: #elif imc >= 40:
    print('Obesidade mórbida.')
