import math
ca = float(input('Informe o cateto adjacente: '))
co = float(input('Informe o cateto oposto: '))

print('\nO cateto Adjacente medi {}.'
'\nO cateto Oposto medi {}.'
'\nA Hipotenusa do triangulo vai medir {:.2f}.'.format(ca, co, math.hypot(ca, co)))

