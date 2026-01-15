'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
> Quantas pessoas tem mais de 18 anos.
> Quantos homens foram cadastrados.
> Quantas mulheres tem menos de 20 anos.'''

totH = totM18 = totM20 =0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    if idade >= 18:
        totM18 += 1

    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
        if sexo == 'M':
            totH += 1
        if sexo == 'F' and idade < 20:
            totM20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Pessoas maiores de 18 anos: {totM18} pessoas')
print(f'Homens cadastrados: {totH}')
print(f'Mulheres com menos de 20 anos: {totM20}')
print('fim')