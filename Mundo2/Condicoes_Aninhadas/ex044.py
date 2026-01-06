'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando seu preço normal e condição de pagamento.
> À vista dinheiro/cheque: 10% de desconto
> À vista no cartão: 5% de desconto
> Em até 2x no cartão: preço normal
> 3x ou mais no cartão: 20% de juros'''

valor = float(input('Digite o valor a ser pago: R$'))

print('[ 1 ] à vista dinheiro/cheque\n'
'[ 2 ] à vista cartão\n'
'[ 3 ] 2x no cartão\n'
'[ 4 ] 3x ou mais no cartão')

opc = int(input('Digite sua opção: '))

if opc == 1:
    print(f'Valor: R${valor:.2f}\nDesconto: 10%\nValor com desconto: R${valor - (valor * 10 / 100):.2f}')
elif opc == 2:
    print(f'Valor: {valor}\nDesconto: 5%\nValor com desconto: R${valor - (valor * 5 / 100):.2f}')
elif opc == 3:
    print(f'Valor: R${valor:.2f}\nParcelas: 2x R${valor/2:.2f}')
elif opc == 4:
    parcelas = int(input('Quantidade de parcelas: '))
    valor =valor + (valor * 20 / 100)
    print(f'Valor: R${valor}\nJuros: 20%\nValor com juros: R${valor:.2f}\nParcelas: {parcelas}x R${valor/parcelas:.2f}') 