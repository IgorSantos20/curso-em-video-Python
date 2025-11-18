'''Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.'''

valor = int(input("Digite um valor para ver seu antecessor e seu sucessor: "))

antecessor = valor - 1
sucessor = valor + 1

print(f"O antecessor de {valor} é: {antecessor}")
print(f"O sucessor de {valor} é {sucessor}")