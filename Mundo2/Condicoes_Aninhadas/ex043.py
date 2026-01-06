'''Desenvolva um lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
> Abaixo de 18.5: Abaixo do peso
> Entre 18.5 e 25: Peso ideal
> 25 até 30: Sobrepeso
> 30 até 40: Obesidade
> Acima de 40: Obesidade mórbida
'''

print('-=-=-=-=CALCULO DE IMC=-=-=-=-')
peso = float(input('Digite seu peso: (KG)'))
altura = float(input('Digite sua altura: (M)'))

imc = peso / altura**2

if peso < 18.5:
    print(f'Abaixo do peso!\nImc: {imc:.1f}')
elif 18.5 <= imc < 25:
    print(f'Peso ideal!\nIMC: {imc:.1f}')
elif 25 <= imc < 30:
    print(f'Sobrepeso!\nIMC: {imc:.1f}')
elif 30 <= imc < 40:
    print(f'Obesidade!\nIMC: {imc:.1f}')
else:
    print(f'Obesidade mórbida!\nIMC: {imc:.1f}')
