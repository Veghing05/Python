At = float(input('Qual a altura da parede : '))
Lg = float(input('Qual a largura da parede : '))
area = Lg * At
print('A parede corresponde a altura de {} metros x {} metros de largura. com uma área de {} m².'.format(At, Lg, area))
Lt = area / 2
print('Para pintar uma parede irá precisar de {} lt de tinta.'.format(Lt))
