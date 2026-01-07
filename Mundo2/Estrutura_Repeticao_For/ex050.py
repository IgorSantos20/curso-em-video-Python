'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, Se o valor digitado for ímpar desconsidere-o.'''

soma = 0
contador = 0

for i in range(1, 7):
    num = int(input(f'Digite o {i} valor: '))
    if num % 2 == 0:
        contador += 1
        soma += num
print(f'A soma dos {contador} números pares é {soma}')