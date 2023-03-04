Nc = str(input('Digite seu nome completo:')).strip()


print('Olá Muito prazer {}!'.format(Nc))
Ls1 = Nc.split()[0]
Ls = Nc.split()
print('Seu primeiro nome é : {}'.format(Ls1))
print('Seu último nome é : {}'.format(Ls[len(Ls)-1]))


