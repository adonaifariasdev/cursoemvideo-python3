velocidade = int(input('Qual a velocidade do carro(Km/h)? '))
if velocidade > 80:
    print('VOCÊ ESTÁ A {} Km/h,ACIMA DA VELOCIDADE PERMITIDA!'.format(velocidade))
    print('VOCÊ FOI MULTADO!')
    print('VALOR DA MULTA R${:.2f}'.format((velocidade - 80)* 7))
'''else:
    print('PARABÉNS! VOCÊ ESTÁ NO LIMITE DE VELOCIDADE PERMITIDA de 80Km/h!')'''
print('TENHA UM BOM DIA! DIRIJA COM SEGURANÇA!')