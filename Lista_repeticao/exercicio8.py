lista = []
for i in range(10):
    lista.append(int(input('Numero: ')))
pares = 0
impares = 1
for i in lista:
    if i%2 ==0:
        pares +=1
    else:
        impares+=1

print('\033[0;32mpares: {}\033[m'.format(pares))
print('\033[0;31mimpares: {}\033[m'.format(impares))