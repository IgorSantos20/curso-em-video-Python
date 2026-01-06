'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
> Equilátero: todos os lador iguais
> Isósceles: dois lados iguais
> Escaleno: todos os lados diferentes
'''

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Os segmentos podem formar triângulo.')
    if r1 == r2 == r3:
        print('Triângulo EQUILÁTERO')
    elif r1 != r2 != r3:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓSCELES')
else:
    print('Não podem formar triângulo')
