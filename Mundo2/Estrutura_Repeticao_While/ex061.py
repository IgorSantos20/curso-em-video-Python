'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostranddo os 10 primeiros termos da progressão usando a estrutura while.'''

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro

contador = 1

while contador <= 10:
    print(f'{termo} -> ', end=' ')
    termo = termo + razao
    contador += 1
print('Fim')