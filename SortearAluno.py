import random

a1 = str(input('1° Aluno :'))
a2 = str(input('2° Aluno :'))
a3 = str(input('3° Aluno :'))
a4 = str(input('4° Aluno :'))

lista = random.choice[a1, a2, a3, a4]
escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
