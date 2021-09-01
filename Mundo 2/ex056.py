# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

somaIdade = 0
maisVelho = 0
mulherMenor20 = 0
for p in range(1, 5):
    print('---- {}a. PESSOA ----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaIdade = somaIdade + idade
    if sexo == 'M':
        if idade > maisVelho:
            maisVelho = idade
            nomeVelho = nome
    if sexo == 'F':
        if idade < 20:
            mulherMenor20 += 1
print('Soma da Idade do grupo é: {} anos.'.format(somaIdade))
print('A média de idade do grupo é de {} anos.'.format(somaIdade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisVelho, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulherMenor20))

