'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date
data_atual = date.today().year
menor = 0
maior = 0
for pessoa in range(1, 8):
    nascimento = int(input('Digite sua data de nascimento: '))
    idade = data_atual - nascimento
    if idade >= 21:
        print('Pessoa maior de idade.')
        maior += 1
    else:
        print('Pessoa menor de idade.')
        menor += 1
print(f'{menor} pessoa(s) são menor de idade.')
print(f'{maior} pessoa(s) são maior de idade.')