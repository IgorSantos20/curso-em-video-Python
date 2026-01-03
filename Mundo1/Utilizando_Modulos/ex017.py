'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostrre o comprimento da hipotenusa.'''

from math import sqrt

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

valor = (cateto_oposto**2 + cateto_adjacente**2)
hipotenusa1 = valor ** (1/2)
hipotenusa2 = pow(valor, 0.5)
hipotenusa3 = sqrt(valor)

print(f"Utilizando a fórmula: {hipotenusa1:.2f}")
print(f"Utilizando o método interno pow: {hipotenusa2:.2f}")
print(f"Utilizando a função sqrt da biblioteca math: {hipotenusa3:.2f}")

