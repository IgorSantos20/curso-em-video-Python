'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.'''

from math import trunc # a função trunc remove a parte fracionária e retorna a parte inteira

numero = float(input("Digite um valor Real qualquer: "))

print(f"A porção inteira do número {numero} é {trunc(numero)}")