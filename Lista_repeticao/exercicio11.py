Quantidade = int(input('Quantidade de notas para a media: '))
notas = []
for i in range(Quantidade):
    notas.append(float(input('Digite a nota: ')))
soma = 0
for i in range(len(notas)):
    soma += notas[i]

media = soma/(len(notas))

print('\033[0;34mmedia: {}\033[m'.format(media))