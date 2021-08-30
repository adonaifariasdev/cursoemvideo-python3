salario = float(input('Salario Atual R$'))
novoSal = salario + (salario * (15/100))
print('O Salário Atual de R${:.2f} com 15% de aumento ficará R${:.2f}.'.format(salario, novoSal))
