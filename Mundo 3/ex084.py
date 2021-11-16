#  Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:
#  A) Quantas pessoas foram cadastradas. #  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.

pessoas = []
dado = []
maisP = menosP = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso(Kg): ')))
    if len(pessoas) == 0:
        maisP = menosP = dado[1]
    else:
        if dado[1] > maisP:
            maisP = dado[1]
        if dado[1] < menosP:
            menosP = dado[1]

    pessoas.append(dado[:])
    dado.clear()

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maisP}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maisP:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menosP}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menosP:
        print(f'[{p[0]}] ', end='')
