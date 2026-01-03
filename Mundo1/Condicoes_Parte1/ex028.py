'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça ao usuário tentar descobrir qual foi o número  escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint

numero = randint(0, 5)

print('-=-=-=-=JOGO DE ADIVINHAÇÂO-=-=-=-=')
print('Pensei em um número de 0 a 5, tente adivinhar qual foi.')
palpite = int(input('Digite seu palpite: '))

if palpite == numero:
    print(f'Meus parabéns! Você acertou.')
    print(f'Palpite: {palpite}')
    print(f'Número: {numero}')
else:
    print('Você errou! Sinto muito.')
    print(f'Palpite: {palpite}')
    print(f'Número: {numero}')
