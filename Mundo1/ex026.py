'''Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).strip().lower()
frase_invertida = frase[::-1]
print(f'A letra A aparece {frase.count('a')}')
print(f'A primeira ocorrencia de A foi na posição {frase.find('a')+1}')
print(f'A última ocorrencia de A foi na posição {frase.rfind('a')+1}')
