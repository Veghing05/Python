Frase = str(input('Digite uma frase: ')).upper().strip()
print(' A letra A aparece {} vezes.'.format(Frase.count('A')))
print('O primeiro A aparece na posição {}.'.format(Frase.find('A')+1))
print('O último A aparece na posição {}.'.format(Frase.rfind('A')+1))
