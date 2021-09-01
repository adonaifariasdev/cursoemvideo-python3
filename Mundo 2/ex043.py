# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

from time import sleep
print('-='*20)
print('|    Índice de Massa Corporal 1.0      |')
print('-='*20)
peso = float(input('Peso(kg): '))
altura = float(input('Altura(m): '))
imc = peso / (pow(altura, 2))
print('PROCESSANDO...')
sleep(3)
print('-='*20)
print('|    Status de Massa Corporal 1.0      |')
print('-='*20)
if imc < 18.5:
    grau = 'ABAIXO DO PESO.'
elif imc >= 18.5 and imc <25:
    grau = 'PESO IDEAL.'
elif imc >= 25 and imc < 30:
    grau = 'SOBREPESO.'
elif imc >= 30 and imc < 40:
    grau = 'OBESIDADE.'
else:
    grau = 'OBESIDADE MÓRBIDA.'
print(' PESO: {:.2f}Kg   |   ALTURA: {:.2f}m'.format(peso, altura))
print(' IMC: {:.2f}      |   GRAU: {}'.format(imc, grau))
print('-='*20)
