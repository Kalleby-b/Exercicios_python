limite = int(input('Qual o valor de N? '))
soma = 0
for i in range(1,limite+1):
    soma += 1/i

print('soma = {:.2f}'.format(soma))