
print('-=-' * 20)
velocidade = float(input('Qual sua velocidade atual: ')) #
print('-=-' * 20)

multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Seu carro foi Multado!! ')
    print('O valor da multa foi de R${:.2f} reais.'.format(multa))

else:
    print('Obrigado, tenha uma boa viagem!! ')
