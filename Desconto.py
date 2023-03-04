Prod = input('Digite o produto: ')
Vl = float(input('Qual o valor do {}: R$'.format(Prod)))
print('O valor do {} é R${} reais.'.format(Prod, Vl))
Desc = 5 * Vl / 100
VlD = Vl - Desc
print('O valor do desconto é de R${:.2f}'.format(Desc))
print('O valor com o desconto aplicado é de R${:.2f}'.format(VlD))


