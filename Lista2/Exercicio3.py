def clear():
    import os
    os.system('cls')

def desG(litr):
    if litr <= 20:
        preco_cheio = litr * 6.4
        desconto = litr * 0.256
        valor = preco_cheio - desconto
        print('Deverá pagar {:.2f}'.format(valor))
        print('='*60)
        retorna()
    elif(litr > 20):
        preco_cheio = litr * 6.4
        desconto = litr * 0.384
        valor = preco_cheio - desconto
        print('Deverá pagar {:.2f}'.format(valor))
        print('='*60)
        retorna()

def desA(litr):

    if litr <= 20:
        preco_cheio = litr * 4.8
        desconto = litr * 0.144
        valor = preco_cheio - desconto
        print('Deverá pagar {:.2f}'.format(valor))
        print('='*60)
        retorna()
    elif(litr > 20):
        preco_cheio = litr * 4.8
        desconto = litr * 0.24
        valor = preco_cheio - desconto
        print('Deverá pagar {:.2f}'.format(valor))
        print('='*60)
        retorna()

def retorna():
    v = input('Repetir? (s/n)')

    if v == "s":
        clear()
        escolha()
    elif v == "n":
        print('Obrigado por usar!')
    else:
        print("Erro! Digite apenas 's' ou 'n'")
        retorna()

def escolha():
    print('='*60)
    combustivel = input('Qual o Combustivel? Gasolina(G) ou Alcool(A)?')

    if combustivel == "G":
        litros = float(input('Quantos litros? '))
        desG(litr= litros)
    elif combustivel == "A":
        litros = float(input('Quantos litros? '))
        desA(litr= litros)
    else:
        print('DIGITE APENAS G OU A')
        escolha()

escolha()