# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares 
# e ímpares em ordem crescente.
valores = []
pares = []
impares = []
for c in range(0, 7):
    valores.append(int(input(f'Digite o {c+1}o. valor: ')))
    for v in valores:
        if v % 2 == 0:
            pares.append(valores[:])
        elif v % 2 == 1:
            impares.append(valores[:])
    valores.clear()
print(f'Você digitou os valores: {sorted(pares+impares)}.')
print(f'Valores pares digitados são: {sorted(pares)}.')
print(f'Valores ímpares digitados são: {sorted(impares)}.')
