'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

computador = randint(0, 10)

print('-=-=-=-=JOGO DE ADIVINHAÇÂO-=-=-=-=')
print('Pensei em um número de 0 a 10, tente adivinhar qual foi.')

acertou = False
contador = 0

while not acertou:
    palpite = int(input('Digite seu palpite: '))
    contador +=1
    if palpite == computador:
        acertou = True


print(f'Você acertou!')
print(f'Tentativas: {contador}')