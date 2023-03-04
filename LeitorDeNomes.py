Nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')

print('Seu nome em Maiúsculo : {}'.format(Nome.upper())) # MAIUSCULA
print('Seu nome em Minúsculo : {}'.format(Nome.lower())) #MINUSCULA
print('Seu nome possui {} letras.'.format(len(Nome) - Nome.count(' '))) # LER LETRAS SEM CONTAR ESPAÇOS
print('Seu primeiro nome possui {} letras.'.format(len(Nome.split()[0]))) # LER QUANTAS LETRAS TEM



