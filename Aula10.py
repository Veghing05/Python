nome = (input('Digite o nome do aluno: '))
print('Seja Bem Vindo {}!'.format(nome))
N1 = float(input('Informe a 1° nota do {}: '.format(nome)))
N2 = float(input('Informe a 2° nota do {}: '.format(nome)))
media = (N1 + N2) / 2

if  media >= 6.0:
    print(' A média do que o {} obteve foi de {} e está APROVADO!!!'.format(nome, media))
else:
    print('A média do que o {} obteve foi de {} e está REPROVADO!'.format(nome, media))
