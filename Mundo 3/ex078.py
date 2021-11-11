# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
# posições na lista.

valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}º valor: ')))
print(f'Você digitou os valores: {valores}.')
print(f'O maior valor digitado foi {max(valores)} na {valores.index(max(valores))+1}ª posição.')
print(f'O menor valor digitado foi {min(valores)} na {valores.index(min(valores))+1}ª posição.')
