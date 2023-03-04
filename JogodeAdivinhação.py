from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador gerar um número

print('-=-' * 20 )
print('Vou pensar em um número entre 0 e 5, tente advinhar! ')
print('-=-' * 20)

jogador = int(input('Em que número pensei? ')) # Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
     print('Você me venceu, PARABÉNS!! ')
     print('Eu pensei no número {} e você pensou no número {}.'.format(computador, jogador))
else:
     print('Eu te venci, você, PERDEU!! ')
     print('Eu pensei no número {} e você pensou no número {}.'.format(computador, jogador))

