import emoji

print('Obrigado por viajar conosco!', (emoji.emojize(':airplane:', language='alias')))

Km = float(input("Me informe quantos km's tem o destino: "))
print("A sua viagem possui de {} Km's." . format(Km))

if Km <= 200:
   Kmm = Km * 0.50
   print('O valor da sua passagem foi de R${:.2f} reais.'.format(Kmm))

else:
    Kmn = Km * 0.45
    print('O valor da sua passagem foi de R${:.2f} reais.'.format(Kmn))


