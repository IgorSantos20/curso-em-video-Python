valor = int(input('Digite um valor entre 0 e 10: '))

while valor < 0 or valor > 10:
    valor = int(input('Digite um valor dentro do intervalo: '))
print('FIM')