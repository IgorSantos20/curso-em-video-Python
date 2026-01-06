'''A Cofederação Nacional de Natação precisa de um programa que leia ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
> Até 9 anos: MIRIM
> Até 14 anos: INFANTIL
> Até 19 anos: JUNIOR
> Até 25 anos: SÊNIOR
> Acima: MASTER
'''

from datetime import date

ano_atual = date.today().year

ano_ani = int(input('Digite o ano em que você nasceu: '))
idade = ano_atual - ano_ani

if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
