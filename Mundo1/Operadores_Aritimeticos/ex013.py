'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario = float(input("Digite seu salário: R$"))

aumento = 15

novosalario = salario + (salario * aumento / 100)

print(f"Salário sem aumento: R${salario:.2f}")
print(f"Salário com aumento de {aumento}%: R${novosalario:.2f}")