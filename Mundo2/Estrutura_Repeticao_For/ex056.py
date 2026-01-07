'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoa. No final do programa, mostre:
> A média de idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres tem menos de 20 anos.
'''

somaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for pessoa in range(1, 5):
    nome = str(input(f'Nome da {pessoa} pessoa: '))
    idade = int(input(f'Idade da {pessoa} pessoa: '))
    sexo = str(input(f'Sexo da {pessoa} pessoa (M/F): ')).upper()
    somaidade += idade

    if pessoa == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo in 'Ff' and idade > 20:
        totalmulher20 += 1

media_idade = somaidade / 4
print(f'Média das idades: {media_idade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos')
print(f'Há {totalmulher20} mulheres com mais de 20 anos.')