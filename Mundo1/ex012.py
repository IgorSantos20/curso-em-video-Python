'''Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preco = float(input("Digite o preço do produto: R$"))

desconto = 5

novopreco = preco - (preco * desconto / 100)

print(f"Preço sem desconto: R${preco:.2f}")
print(f"Peço com desconto de 5%: R${novopreco}")