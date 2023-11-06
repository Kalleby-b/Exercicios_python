
def resistencia():
    tipo = input('Qual o tipo de circuito?(S/P) ')
    if tipo == "S":
        R1 = int(input('Qual a primeira Resistencia? '))
        R2 = int(input('Qual a segunda Resistencia? '))

        Req = R1 + R2
        print("A resistencia equivalente do sistema é {} Ohm's ".format(Req))
    elif tipo == "P":
        R1 = int(input('Qual a primeira Resistencia? '))
        R2 = int(input('Qual a segunda Resistencia? '))

        Req = (R1+R2)/(R1*R2)
        print("A resistencia equivalente do sistema é {:.2f} Ohm's ".format(Req))

    else:
        print ("Erro Fatal! digite P para Paralelo ou S para Serie ")
        resistencia()

    voltar = input('Digite R para realizar outro calculo: ')
    if voltar == "R":
        resistencia()
    else:
        print('Obrigado por usar!')

resistencia()