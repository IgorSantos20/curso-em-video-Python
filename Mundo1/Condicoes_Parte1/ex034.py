'''escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digite o seu salário: R$'))

if salario > 1250.00:
    salario_novo = salario + (salario * 10 / 100)
    print(f'Salário: R${salario:.2f}')
    print(f'Salário com aumento de 10%: R${salario_novo:.2f}')
else:
    salario_novo = salario + (salario * 15 / 100)
    print(f'Salário: R${salario:.2f}')
    print(f'Salário com aumento de 15%: R${salario_novo:.2f}')