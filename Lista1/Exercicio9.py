from math import ceil

area = float(input('Qual a Área a ser pintada?(em metros quadrados): '))
tinta = ceil(area/6)
folga = tinta/10
tinta = tinta+ folga

latas1 = ceil(tinta/18)
latas2 = ceil(tinta/3.6)

sit1 = latas1*80
sit2 = latas2*25

if tinta <= 3.6:
    sit3 = 25
    print("Na primeira situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 18 litros á 80R$".format(sit1,area, latas1))
    print("Na segunda situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 3.6 litros á 25R$".format(sit2,area,latas2))
    print("Na terceira situação você gastar {} reais para pintar {} metros quadrados, com 1 lata de 3.6 litros á 25R$".format(sit3,area))
elif (3.6< tinta < 18):
    if (tinta - 3.6 ) < (18 - tinta):
        latas3 = ceil(tinta/3.6)
        sit3 = latas3 * 25
        print("Na primeira situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 18 litros á 80R$".format(sit1,area, latas1))
        print("Na segunda situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 3.6 litros á 25R$".format(sit2,area,latas2))
        print("Na terceira situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 3.6 litros á 25R$".format(sit3,area, latas3)) 
    else:
        sit3 = 80
        print("Na primeira situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 18 litros á 80R$".format(sit1,area, latas1))
        print("Na segunda situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 3.6 litros á 25R$".format(sit2,area,latas2))
        print("Na terceira situação você gastar {} reais para pintar {} metros quadrados, com 1 lata de 18 litros á 80R$".format(sit3,area))
else:
    latas18 = tinta // 18
    lat = (tinta%18)
    latas3_6 = (float('{:.2f}'.format(lat)))#Converte para uso de 2 casas decimais
    latas3_6 = ceil(latas3_6/3.6)
    sit3 = latas18*80 + latas3_6*25
    print("Na primeira situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 18 litros á 80R$".format(sit1,area, latas1))
    print("Na segunda situação você gastar {} reais para pintar {} metros quadrados, com {} latas de 3.6 litros á 25R$".format(sit2,area,latas2))
    print("Na terceira situação você gastar {} reais para pintar {} metros quadrados,\n com {} latas de 18 litros á 80R$ e {} de 3.6 Litros a 25R$".format(sit3,area,latas18,latas3_6))