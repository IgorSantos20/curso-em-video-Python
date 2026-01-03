'''Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.'''

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

print(f'Maior: {max(num1, num2, num3)}')
print(f'Menor: {min(num1, num2, num3)}')