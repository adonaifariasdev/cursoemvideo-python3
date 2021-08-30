# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Comprimento da primeira reta(m): '))
b = float(input('Comprimento da segunda reta(m): '))
c = float(input('Comprimento da terceira reta(m): '))
print('-='*20)
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos PODEM FORMAR TRIÂNGULO!')
else:
    print('Os seguimentos NÃO PODEM FORMAR TRIÂNGULO!')
print('-='*20)
