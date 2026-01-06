'''Escreva um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
> Média abaixo de 5: REPROVADO
> Média entre 5 e 6.9: RECUPERÇÃO
> Média 7.0 ou supererior: APROVADO
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Aluno reprovado!\nMédia: {media:.1f}')
elif media >= 5 and media <= 6.9:
    print(f'Aluno de recuperação!\nMédia: {media:.1f}')
else:
    print(f'Aluno aprovado!\nMédia: {media:.1f}')
