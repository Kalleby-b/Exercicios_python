nota = input('Digite a nota de 0 a 10: ')

if nota.isalpha() == True or (0> float(nota) <= 10):
    verificar = False
    while verificar == False:
        print('Valor inválido!!')
        nota = input('Digite a nota de 0 a 10: ')
        if nota.isalpha() == True or (0> float(nota) <= 10):
            verificar == False
        else:
            verificar = True
            print('A nota é : {}'.format(nota))