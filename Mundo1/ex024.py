'''Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"'''

cidade = str(input('Em que cidade você nasceu? ')).strip().lower()
print(cidade[:5] == 'santo')