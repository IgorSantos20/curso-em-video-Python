'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não conituar a digitar valores.'''

num = int(input('Digite um valor: '))
contador = 1
soma = num
media = 0
maior = num
menor = num
continuar = True

while continuar == True:
    opc = str(input('Deseja continuar? [S/N]')).strip().upper()
    if opc == 'S':
        num = int(input('Digite um valor: '))
        contador += 1
        soma += num
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    else:
        continuar = False
print(f'Média: {soma/contador}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')