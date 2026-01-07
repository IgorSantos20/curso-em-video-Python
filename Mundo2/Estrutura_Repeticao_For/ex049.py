'''Refaça o DESAFIO 009, mostrando a tabuada de um búmero que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input('Digte um valor para ver sua tabuada: '))

for i in range(1, 11):
    print(f'{num} X {i:2} = {num*i}')
