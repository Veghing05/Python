a = int(input('Informe o 1° número: '))
b = int(input('Informe o 2° número: '))
c = int(input('Informe o 3° número: '))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print('O número maior é o {}.'.format(maior))

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
print('O número menor é o {}.'.format(menor))
