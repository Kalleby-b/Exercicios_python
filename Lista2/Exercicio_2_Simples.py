def caixa():
    print('='*30)
    print('O caixa não trabalha com moedas, portanto digite um valor Inteiro!')
    valor = int(input('Digite o Valor do saque: '))
    notas = [100, 50, 20, 10, 5, 2]
    saque = [  0 , 0,  0,  0, 0, 0]
    if valor < 5 or valor > 1000:
        print(' O caixa não Trabalha com valores menores que 5\n ou valores maiores que 1000')
        caixa()

    va = str(valor)
    tamanho = len(va)
    ultimo = va[(tamanho-1)]

    if ultimo == "1" or ultimo == "3":
        va = va[:(tamanho-1)]
        va = int(va) * 10
        val = valor - (va-5)
        valor = valor - val
        for i in range(len(notas)):
            saque[i] = valor// notas[i]
            valor = valor % notas[i]
        saque[4] = 1
        saque[5] = int(val/2)


        for z in range(len(notas)):
            print('Serão entregues {} notas de {}'.format(saque[z], notas[z]))

        retorna()

    else:
        if valor%2 != 0 :
            for i in range(len(notas)):
                saque[i] = valor// notas[i]
                valor = valor % notas[i]

            for z in range(len(notas)):
                print('Serão entregues {} notas de {}'.format(saque[z], notas[z]))
            retorna()
        else:
            if valor < 10:
                n2 = valor/2
                print('Serão fornecidas\n{:.0f} notas de 2 R$'.format(n2))
            elif valor>=10:
                va = va[:(tamanho-1)]
                va = int(va) * 10
                val = valor - (va)
                print(va)
                for i in range(len(notas)):
                    saque[i] = va// notas[i]
                    va = va % notas[i]
                saque[5] = int(val/2)
                for z in range(len(notas)):
                    print('Serão entregues {} notas de {}'.format(saque[z], notas[z]))
                

            retorna()


def clear():
    import os
    os.system('cls')

def retorna():
    v = input('Repetir? (s/n)')

    if v == "s":
        clear()
        caixa()
    elif v == "n":
        print('Obrigado por usar!')
    else:
        print("Erro! Digite apenas 's' ou 'n'")
        retorna()
caixa()
       