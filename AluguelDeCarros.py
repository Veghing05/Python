Dias = int(input('Quantos dias o carro foi alugado: '))
KM = float(input('Quantos KMs foi percorrido: '))
Pg1 = Dias * 60
KMs =  KM * 0.15
Total = Pg1 + KMs
print('O carro foi alugado por {} dias e terá um custo de R${:.2f} reais. '.format(Dias, Pg1))
print('O carro percorreu {} Kms e terá um custo de  R${:.2f} reais.'.format(KM, KMs))
print('O seu custo total é de R${:.2f} reais.'.format(Total))
