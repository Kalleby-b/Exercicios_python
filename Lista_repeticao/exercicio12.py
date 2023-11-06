tabuada = int(input('Qual tabuada deseja montar? '))
inicio = int(input('Começando em: '))
fim = int(input('Terminando em: '))
if fim < inicio:
    print('\033[0;31mERRO O NUMERO FINAL É MENOR QUE O INICIAL\033[m')
    verificar = False
    while verificar == False: 
        print('\033[0;31mERRO O NUMERO FINAL É MENOR QUE O INICIAL\033[m')
        inicio = int(input('Começando em: '))
        fim = int(input('Terminando em: '))
        if fim < inicio:
            verificar = False
        else:
            verificar = True
for i in range(inicio, fim+1):
    print('{} x {} = {}'.format(tabuada, i , (tabuada*i)))