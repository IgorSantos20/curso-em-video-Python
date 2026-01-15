'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conseguiu no final do jogo'''

from random import randint

print('-='*10)
print('JOGO DO PAR OU ÍMPAR')
print('-='*10)

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
        print('Deu PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
        print('Vamos jogar novamente...')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitorias} vezes.')