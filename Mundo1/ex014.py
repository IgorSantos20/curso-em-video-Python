'''Escreva um programa que converta uma temperatura digitada em C e converta para F'''

graus = int(input("Digite a temperatura em Graus Celsius: "))

fahrenheit = (graus * 1.8) + 32

print(f"{graus}C = {fahrenheit} F")