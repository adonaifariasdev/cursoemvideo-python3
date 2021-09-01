# rie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior18 = qtdeM = qtdeF = 0
while True:
    print('-' * 30)
    print('{:^30}'.format(' CADASTRE UMA PESSOA '))
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        qtdeM += 1
    if sexo == 'F' and idade < 20:
        qtdeF += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {qtdeM} homens cadastrados')
print(f'E temos {qtdeF} mulheres com menos de 20 anos')



