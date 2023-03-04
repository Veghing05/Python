frase  = 'Curso em Video Python'
        # C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
 # ANÁLISE
print('='*22)
print('ANÁLISE')
print(len(frase)) # CONTAR CARACTERES
print(frase.count('e')) # MOSTRAR QUANTAS LETRAS ESPECIFICAS
print(frase.count('o',0,13)) #
print(frase.find('deo')) # LOCALIZA A POSIÇÃO DAS LETRAS
print(frase.find('android')) # LOCALIZA A FRASE
print('Curso' in frase) # MOSTRA SE A PALAVRA EXISTE NA FRASE

# TRANSFORMAÇÃO
print('-'*22)
print('TRANSFORMAÇÃO')
print('-'*22)
print(frase.replace('Python', 'Android')) # TROCA AS PALAVRAS
print(frase.upper()) # MUDA A FRASE TODA PARA MAIUSCULA
print(frase.lower()) # MUDA A FRASE TODA PARA MININUSCULA
print(frase.capitalize()) # DEIXA A 1° LETRA MAIUSCULA
print(frase.title()) # DEIXA A 1° LETRA DE TODO COMEÇO DE FRASE MAIUSCULA
print(frase.strip()) # REMOVE OS ESPAÇOS INÚTEIS
print(frase.rstrip()) # REMOVE OS ESPAÇOS A DIREITA
print(frase.lstrip()) # REMOVE OS ESPAÇOS A ESQUERDA

# DIVISÃO
print('-'*42)
print('DIVISÃO')
print('-'*42)
print('frase.split()')
print(frase.split()) # DIVIDE OS ESPAÇOS

# JUNÇÃO
print('-'*42)
print('JUNÇÃO')
print('-'*42)
print(';'.join(frase)) # JUNTA AFRASE
print('='*45)
