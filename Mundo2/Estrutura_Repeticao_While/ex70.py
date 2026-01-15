'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
> Qual é o total gasto na compra.
> Quantos produtos custam mais de R$1000.
> Qual é o nome do produto mais barato.
'''

total = totmil = menor = cont = 0
prodB = ' '

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Valor: R$'))
    cont += 1
    total += preco
    
    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break
print(f'Valor total: R${total}')
print(f'Produtos custando mais de R$1.000: {totmil}')
print(f'O produto mais barato custa: R${menor}')
