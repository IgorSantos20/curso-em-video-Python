'''Faça um programa que leia o ano de nascimetno de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimeto: '))
ano = date.today().year
idade = ano - ano_nascimento

if idade < 18:
    print(f'Você ainda não pode se alistar.\nTempo restante: {18-idade} ano(s)')
elif idade == 18:
    print('Você deve se alistar este ano.')
else:
    print(f'Você passou do tempo de se alistar.\nTempo de atraso: {idade - 18} ano(s)')