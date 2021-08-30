alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura daparede? '))
area = alt * lar
qtde = area / 2
print('A sua área é {:.2f}m2. \nA quantidade de tinta para pintar sua parede é {:.2f} unidades.'.format(area, qtde))
