from math import ceil


#altura = float(input('Qual a altura da parede? '))
#largura = float(input('qual a largura da parede? '))

#area = altura*largura

area = int(input('Qual a Area a ser pintada?  '))

latas = ceil(ceil(area/3)/18)

gasto = latas * 80

print('você ira gastar {} reais para pintar {} metros quadrados com {} latas de tinta ba 80 reais'.format(gasto, area, latas))

