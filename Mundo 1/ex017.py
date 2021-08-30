#from math import sqrt, pow
import math
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
#h = math.sqrt(pow(co, 2) + pow(ca, 2))
h = math.hypot(co, ca)
print('o comprimento da hipotenusa é {:.2f}.'.format(h))