'''Faça um prograna que leia a largura e a altura de uma parede em metris, calcuke a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².'''

largura = float(input("Largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura

print(f"A área da parede que mede {largura} metros de largura e {altura} metros de altura é {area}m²")

tinta = area / 2

print(f"Para pintar a parede com {area}m² precisa-se de {tinta}l de tinta")