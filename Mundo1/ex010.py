'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

Considerar US$1.00 = R$3.27'''

reais = float(input("Valor em Dólares: "))

dolares = 3.27

print(f"R${reais} = US${reais/dolares:.2f}")