# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da sua viagem? '))
print('Você fará uma viagem de {}Km.'.format(distancia))
'''if distancia > 200:
    valor = distancia * 0.45
else:
    valor = distancia * 0.50'''
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45 #Maneira simplificada
print('VALOR DA PASSAGEM É R${:.2f}.'.format(valor))
