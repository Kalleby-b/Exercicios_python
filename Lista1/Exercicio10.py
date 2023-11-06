arquivo = int(input('Digite o tamanho do arquivo em MB: '))
velocidade = int(input('digite a velocidade do link em Mbps: '))

tempo = arquivo/velocidade
minutos = tempo/60


print('O download irá demorar {:.3f} minutos ou {:.2f} segundos'.format(minutos,tempo))