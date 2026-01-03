'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''


print('-=-=-=-=Radar Eletrônico-=-=-=-=')
velocidade = int(input('Digite a sua velocidade: '))

if velocidade > 80:
    print('Você ultrapassou o limite de velocidade!')
    print(f'Multa de R${(velocidade - 80) * 7.00:.2f}')
else:
    print('Velocidade dentro do limite. Boa viagem!')