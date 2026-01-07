'''Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''


contador = 0
soma = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        contador +=1
        soma += num
print(f'Existem {contador} números entre 1 e 500 que são ímpares e múltiplos de 3.')
print(f'A soma de todos os valores é {soma}')

