'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
[ 1 ] binário
[ 2 ] octal
[ 3 ] hexadecimal'''

num = int(input('Digite um valor: '))
opc = int(input('[ 1 ] binário\n'
'[ 2 ] octal\n'
'[ 3 ] hexadecimal\n'
'Escolha sua opção: '))

if opc == 1:
    print(bin(num)[2:])
elif opc == 2:
    print(oct(num)[2:])
elif opc == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida!')