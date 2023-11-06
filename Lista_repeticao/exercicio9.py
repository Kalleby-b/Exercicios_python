numero = int(input('Numero para o calculo de fatorial: '))
limite =numero
fatorial = 1

while limite > 1:
    fatorial = fatorial * numero
    numero-=1
    limite -=1
print('\033[0;32mfatorial: {}\033[m'.format(fatorial))