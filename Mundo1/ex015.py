'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.'''

dias = int(input("Digite a quantidade de dias que permaneceu com o carro: "))
quilometros = float(input("Digite a quantidade de Km rodados: "))

diaspreco = 60
kmpreco = 0.15

print(f"Dias {dias} = {dias*diaspreco:.2f}")
print(f"Km {quilometros} = {quilometros*kmpreco:.2f}")
print(f"Total: {dias*diaspreco + quilometros*kmpreco:.2f}")
