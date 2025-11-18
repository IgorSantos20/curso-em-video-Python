'''Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.'''

metros = float(input("Digite o valor em metros para sua conversão: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"{metros} metros = {centimetros}centímetros")
print(f"{metros} metros = {milimetros} milímetros")