n = int(input('Digite o valor de n: '))
m = 1
s = 0
soma = ['']
for i in range(1,n+1):
    s += i/m
    soma.append('{}/{}'.format(i , m))
    m +=2

palavra = '1'
soma.pop(0)
soma.pop(0)
for i in range(len(soma)):
    palavra += " + " + soma[i]

print(palavra, " = {:.2f}".format(s))