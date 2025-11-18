'''Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.'''


from math import sqrt

valor = int(input("Digite um número: "))

dobro = valor * 2
triplo = valor * 3
raizquadrada = valor ** (1/2)
raizquadrada2 = sqrt(valor)  # Utilizando o método sqrt

print(f"O dobro de {valor} é {dobro}")
print(f"O triplo de {valor} é {triplo}")
print(f"A raíz quadrada de {valor} é {raizquadrada}")
print(f"A raíz quadrada de {valor} é {raizquadrada2}")