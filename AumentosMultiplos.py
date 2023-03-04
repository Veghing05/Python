Sal = float(input('Digite o valor do seu salário: '))
if Sal > 1250:
    SJ1 = Sal * 1.10

else:
    SJ1 = Sal * 1.15

print('O valor do salario ajustado é de R${:.2f} reais'.format(SJ1))


