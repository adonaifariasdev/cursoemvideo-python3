import math
ang = float(input('Digite o valor de um anglo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O ângulo de {}º tem SENO igual a: {:.2f}.'.format(ang, sen))

print('O ângulo de {}º tem COSSENO igual a: {:.2f}.'.format(ang, cos))

print('O ângulo de {}º tem TANGENTE igual a: {:.2f}.'.format(ang, tan))
