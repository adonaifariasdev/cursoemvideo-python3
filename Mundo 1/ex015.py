empresa = 'VALMONT RENT A CAR'
relatorio = ' DADOS PARA PAGAMENTO'
print('='*30)
print('{:=^30}'.format(empresa))
print('='*30)

dias = int(input('Quantidade de dias alugado? '))
km = int(input('Qual a quilometragem percorrida? '))
diaria = 60
rodada = 0.15
print('='*30)
print('{:=^30}'.format(relatorio))
print('='*30)
print('DIAS ALUGADOS: {} DIAS.'.format(dias))
print('KM PERCORRIDA: {} KM.'.format(km))
print('PREÇO DA DIÁRIA R${:.2f}.'.format(diaria))
print('PREÇO POR KM RODADO R${:.2f}.'.format(rodada))
pagarDia = dias * diaria
pagarKm = km * rodada
total = pagarDia + pagarKm
print('TOTAL A PAGAR R${:.2f}.'.format(total))
print('='*30)

