'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''


num = int(input('Digite um valor para saber se ele é ou não um número primo: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[33m{i}', end=' ') 
        total += 1
    else:
        print(f'\033[31m{i}', end=' ')
print('\033[m') 
print(f'O número {num} foi divisível {total} vezes.')

if total == 2:
    print(f'PORTANTO, o número {num} É PRIMO!')
else:
    print(f'PORTANTO, o número {num} NÃO É PRIMO!')
