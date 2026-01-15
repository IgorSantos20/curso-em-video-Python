'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, quue é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderar o flag).'''

num = int(input('Digite um valor [999 para parar]: '))
soma = 0
contador = 0
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um valor: '))
print(f'Resutado: {soma}\n{contador} números.')
