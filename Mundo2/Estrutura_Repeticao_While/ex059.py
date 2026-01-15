'''Crie um programa que leia dois valores e mostre um menu de opções. Seu programa deverá realizar a opção selecionada em cada caso.'''

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

while True:
    print('[ 1 ] Somar'
    '\n[ 2 ] Multiplicar'
    '\n[ 3 ] Maior'
    '\n[ 4 ] Novos números'
    '\n[ 5 ] Sair do programa')

    opc = int(input('Opção: '))

    if opc == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    
    elif opc == 2:
        multiplicacao = num1 * num2
        print(f'{num1} x {num2} = {multiplicacao}')
    
    elif opc == 3:
        print(f'Maior: {max(num1, num2)}')
    
    elif opc == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    
    elif opc == 5:
        print('Finalizando...')
        break

    else:
        print('Opção inválida!')

