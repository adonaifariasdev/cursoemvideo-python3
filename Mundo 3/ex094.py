# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
dados = dict()
lista = list()
somaIdade = media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, Digite apenas M ou F.')
    if dados['sexo'] in 'N':
        break
    dados['idade'] = int(input('Idade: '))
    somaIdade += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
media = somaIdade / len(lista)
print('-=' * 30)
print(f'A) A quantidade de pessoas cadastradas foi: {len(lista)}')
print(f'B) A média de idade é: {media:5.2f} anos.')
print('C) As mulheres cadastradas são: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}; ', end='')
print()
print('D) As pessoas que estão acima da média de idade são: ')
for p in lista:
    if p['idade'] >= media:

        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
