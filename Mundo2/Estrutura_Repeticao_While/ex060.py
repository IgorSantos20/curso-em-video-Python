'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

num = int(input('Digite um valor: '))
fatorial = 1
contador = num

while contador > 0:
    print(f'{contador} ', end=' ')
    print('x' if contador > 1 else '=', end=' ')
    fatorial = fatorial * contador
    contador -= 1

print(fatorial)