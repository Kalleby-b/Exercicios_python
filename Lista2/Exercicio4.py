from math import sqrt
a = float(input('Digite o Valor de A: '))
b = float(input('Digite o Valor de B: '))
c = float(input('Digite o Valor de C: '))

delta = (b**2)-4*a*c

if delta < 0:
    print("Raizes imaginarias")
elif delta == 0:
    x1 = (-b)/ (2*a)
    print('-'*50)
    print ("Raiz Unica!\n")
    print('Raiz = {:.2f}'.format(x1))
    print('-'*50)
else:
    x1 = (-b + sqrt(delta))/ (2*a)
    x2 = (-b - sqrt(delta))/ (2*a)
    print('-'*50)
    print('Raizes Distintas')
    print("x' = {}, X'' = {}".format(x1, x2))
    print('-'*50)