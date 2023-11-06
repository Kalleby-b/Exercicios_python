import pandas as pd
numeros = []
print("="*60)
for i in range(5):
    numeros.append(input('Digite o numero: '))

for i in range(len(numeros)):
    numeros[i] = float(numeros[i] )

soma_numeros = 0
for i in range(len(numeros)):
    soma_numeros += numeros[i]

media = soma_numeros/(len(numeros))
print("="*60)
print('soma: {}\nmedia: {}'.format(soma_numeros, media))

