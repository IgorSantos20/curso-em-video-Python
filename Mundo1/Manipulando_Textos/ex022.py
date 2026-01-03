'''Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerearr espaços).
> Quantas letras tem o primeiro nome.'''

nome = input("Digite seu nome completo: ").strip()

print(f"Seu nome com todas as letras maiúsculas: {nome.upper()}")
print(f"Seu nome com todas as letras maiúsculas: {nome.lower()}")
print(f"O nome {nome} tem {len(nome)-nome.count(' ')} letras") 
# função len() conta quantos caracteres tem, já a função count com base no parâmetro procura na string e contabiliza.
print(f"Seu primeiro nome tem {nome.find(' ')} letras")
# a função find procura a primeira ocorrencia do caractere de parâmetro e retorna a posição.

separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras")