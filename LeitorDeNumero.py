Numero = int(input('Digite um númetro de 0 a 9999:'))
U = Numero // 1 % 10
D = Numero // 10 % 10
C = Numero // 100 % 10
M = Numero // 1000 % 10
print('Analisando o número {}...'.format(Numero))
print('Unidade: {} '.format(U))
print('Dezena : {} ' .format(D))
print('Centena: {}' .format(C))
print('Milhar : {}'.format(M))
