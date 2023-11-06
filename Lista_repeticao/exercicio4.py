numeros = []
for i in range(5):
    numeros.append(input('Digite o numero: '))

for i in range(len(numeros)):
    numeros[i] = float(numeros[i] )

    
numeros.sort()
print(numeros[len(numeros)-1])