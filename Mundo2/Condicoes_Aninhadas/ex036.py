'''Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado. '''

valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário: R$'))
anos = int(input('Anos: '))

pres_mensal = valor_casa / (anos * 12)
minimo =  salario * 30 / 100


if pres_mensal <= minimo:
    print(f'Empréstimo concedido!')
    print(f'Parcelas: {pres_mensal:.2f}')
else:
    print(f'Empréstimo negado! Salário insuficiente')