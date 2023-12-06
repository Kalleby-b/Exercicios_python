
def clear():
    import os
    os.system('cls')



def bindec(num):
    numero = 0
    print('='*50)
    num = str(num)
    sep = num.split('.')
    #convertendo a parte inteira===============================================================
    z = len(sep[0])-1
    for i in sep[0]:
        numero = numero + int(i)*(2**z)
        z-=1
    #convertendo a fracionaria se existir=====================================================================================================================
    if sep[1] != 0:
        z = 1
        for i in sep[1]:
            numero = numero +int( i)*(2**-z)
            z += 1

    print(numero)
    # Pergunta de retorno =====================================================================================================================
    print('='*80)
    usr = input('usar novamente? ')
    if usr == 's':
        clear()
        chamar()
    elif usr == 'n':
        print('obrigado por usar!!')

    else:
        from time import sleep
        print('erro...')
        sleep(1)
        print('resetando...')
        sleep(1)
        clear()
        chamar()


def decbin(num):
    binario =[]
    binario2 = []
    numero = 0
    print('='*50)
    n = []
    inteiro = 0
    fracional = 0

    n = str(num).split('.')
    # dividindo inteiro e fracional =====================================================================================================================
    inteiro = int(n[0])
    fracional = int(n[1])/(10**len(str(n[1])))

    #convertendo a parte inteira =====================================================================================================================
    while inteiro !=0 :
        binario.append(inteiro%2)
        inteiro = inteiro//2
    binario.reverse()
    #convertendo o fracionario =====================================================================================================================
    i = 0
    a = int(input('Quantas casas decimais? '))
    while i < a :
        temp = str(fracional*2).split('.')
        binario2.append(temp[0])
        fracional = int(temp[1])/(10**len(temp[1]))
        i+=1
    tempo = ''
    for i in range(len(binario)):
        tempo = tempo + str(binario[i])
    tempo2 = ''
    for i in range(len(binario2)):
        tempo2 = tempo2 + str(binario2[i])
    
    # juntando ambas =====================================================================================================================
    numero = tempo + '.'+tempo2

 
    print(numero ,'\n')
    print('='*80)
    usr = input('usar novamente? ')
    if usr == 's':
        clear()
        chamar()
    elif usr == 'n':
        print('obrigado por usar!!')

    else:
        from time import sleep
        print('erro...')
        sleep(1)
        print('resetando...')
        sleep(1)
        clear()
        chamar()

def chamar ():
    chamado = int(input('chamar: '))

    if chamado == 1:
        print('Decimal para Binario')
        conv = float(input('Digite o numero a ser convertido: '))
        decbin(conv)
    elif chamado == 2:
        print('Binario para Decimal  ')
        conv = float(input('Digite o numero a ser convertido: '))
        bindec(conv)

    else:
        print('ERRO!! DIGITE APENAS 1 OU 2')
        chamar()

chamar()
