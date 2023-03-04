import math

ângulo = float(input('Qual o valor do ângulo:'))
Seno = math.sin(math.radians(ângulo))
print('O ângulo de  {} tem o SENO de : {:.2f}.'.format(ângulo, Seno))
Cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de : {:.2f}'.format(ângulo, Cosseno))
Tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE {:.2f}'.format(ângulo, Tangente))
