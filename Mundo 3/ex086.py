# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite o valor para [{i},{j}]: '))
        matriz[i].append(valor)
print(matriz)
print()

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()
