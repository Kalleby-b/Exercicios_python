tamanho = int(input('Tamanho do conjunto: '))
conjunto = []
for i in range(tamanho):
    conjunto.append(int(input('Digite o numero: ')))

soma = 0
for i in conjunto:
    soma += i


conjunto.sort()
print('\033[0;35msoma: {}\033[m'.format(soma))
print('\033[0;32mmenor valor: {}\033[m'.format(conjunto[0]))
print('\033[0;34mmaior valor: {}\033[m'.format(conjunto[(len(conjunto)-1)]))
