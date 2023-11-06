def caixa():
    print('='*30)
    print('O caixa não trabalha com moedas, portanto digite um valor Inteiro!')
    valor = int(input('Digite o Valor do saque: '))
    dv100 = valor//100
    dv50 = valor//50
    dv20 = valor//20
    dv10 = valor//10
    if valor < 5 or valor > 1000:
        print(' O caixa não Trabalha com valores menores que 5\n ou valores maiores que 1000')
        caixa()
    #valores menores que 100
    if dv100 == 0:
        #Valores menores que 50
        if dv50 == 0:
            #Valores menores que 20
            if dv20 == 0 :
                #Valores menores que 10
                if dv10 == 0:
                    men10(val = valor)
                
                else:
                    #Valores entre 10 e 15 IMPARES  
                    if (0 < valor%10 <5 and (valor%10)%2 != 0) :
                        resto = (valor) - 5
                        n2 = (abs(resto)) / 2
                        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                    #valores entre 15 e 20 IMPARES
                    elif 5 <= valor%10  and (valor%10)%2 != 0:
                        resto = (valor%10) - 5
                        n2 = resto/ 2
                        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
            else:
                men20(val= valor)      
        else:
            men50(val = valor)

    else:
        #Valores entre 100 e 105 IMPARES
        if (0<= valor%100 < 5) and (valor%50)%2 != 0 and valor<105:
            resto = valor - 95
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n2 notas de 20 R$\n1 nota de 50 R$'.format(n2))
        #Valores entre 100 e 105 PARES
        elif(0<= valor%100 <5) and (valor%50)%2 == 0 and valor < 105:
            resto = valor - 100
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 100 R$'.format(n2))
        if valor < 200:
            r = valor-100
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('1 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('1 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('1 nota de 100')
                else:
                    men20(val= r)  
                    print('1 nota de 100')    
            else:
                men50(val = r)
                print('1 nota de 100')
        elif valor <300:
            r = valor-200
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('2 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('2 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('2 nota de 100')
                else:
                    men20(val= r)  
                    print('2 nota de 100')    
            else:
                men50(val = r)
                print('2 nota de 100')
        elif valor <400:
            r = valor-300
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('3 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                         
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('3 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('3 nota de 100')
                else:
                    men20(val= r)  
                    print('3 nota de 100')    
            else:
                men50(val = r)
                print('3 nota de 100')
        elif valor <500:
            r = valor-400
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('4 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('4 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('4 nota de 100')
                else:
                    men20(val= r)  
                    print('4 nota de 100')    
            else:
                men50(val = r)
                print('4 nota de 100')
        elif valor <600:
            r = valor-500
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('5 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('5 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('5 nota de 100')
                else:
                    men20(val= r)  
                    print('5 nota de 100')    
            else:
                men50(val = r)
                print('5 nota de 100')
        elif valor <700:
            r = valor-600
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('6 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('6 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('6 nota de 100')
                else:
                    men20(val= r)  
                    print('6 nota de 100')    
            else:
                men50(val = r)
                print('6 nota de 100')
        elif valor <800:
            r = valor-700
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('7 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('7 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('7 nota de 100')
                else:
                    men20(val= r)  
                    print('7 nota de 100')    
            else:
                men50(val = r)
                print('7 nota de 100')
        elif valor <900:
            r = valor-800
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('8 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('8 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('8 nota de 100')
                else:
                    men20(val= r)  
                    print('8 nota de 100')    
            else:
                men50(val = r)
                print('8 nota de 100')
        elif valor >900 and valor <1000:
            r = valor-900
            di50 = r//50
            di20 = r//20
            di10 = r//10
            if di50 == 0:
                #Valores menores que 20
                if di20 == 0 :
                    #Valores menores que 10
                    if di10 == 0:
                        men10(val = r)
                        print('9 nota de 100')
                    else:
                        #Valores entre 10 e 15 IMPARES  
                        if (0 < r%10 <5 and (r%10)%2 != 0) :
                            resto = (r) - 5
                            n2 = (abs(resto)) / 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
                            print('9 nota de 100')
                        #Valores entre 15 e 20 IMPARES
                        elif 5 <= r%10  and (r%10)%2 != 0:
                            resto = (r%10) - 5
                            n2 = resto/ 2
                            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$'.format(n2))
                            print('9 nota de 100')
                else:
                    men20(val= r)  
                    print('9 nota de 100')    
            else:
                men50(val = r)
                print('9 nota de 100')
        else:
            print('10 notas de 100')
    print('='*30)
    v = input('Repetir? (s/n)')

    if v == "s":
        clear()
        caixa()
    elif v == "n":
        print('Obrigado por usar!')
    else:
        print("Erro! Digite apenas 's' ou 'n'")
        v = input('Repetir? (s/n)')


def men10(val):
    #Valores entre 5 e 10 PARES
    if val%2 == 0:
        n2 = val/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$'.format(n2))
    #Valores entre 5 e 10 IMPARES
    else:
        resto = val - 5
        n2 = resto/ 2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$'.format(n2))
    

def men20(val):
        #vales entre 10 e 20 PARES
        if (0 <= val%10 <5 and (val%10)%2 == 0) or (5 <= val%10  and (val%10)%2 == 0 and val<20):
            resto = val - 10
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 10 R$'.format(n2))
            
        #vales entre 20 e 25 IMPARES
        elif(0< val%20 <5 ) and (val%20)%2 != 0 and val < 40 :
            resto = (val - 15)
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10'.format(n2))       
        #vales entre 25 e 35 IMPARES
        elif(5<= val%20<15 ) and (val%20)%2 != 0 and val < 40:
            resto = val - 25
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 20 R$'.format(n2))       
        #vales entre 35 e 45 IMPARES
        elif((15<= val%20 <=19) and (val%20)%2 != 0) or ((0 < val%20 <5 ) and (val%20)%2 != 0 and val>40):
            resto = val - 35
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 nota de 10 R$\n1 nota de 20 R$'.format(n2))
        #valews entre 45 e 50 IMPARES
        elif((5<= val%20) and (val%20)%2 != 0) and val> 40:
            resto = val - 45
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n2 nota de 20 R$'.format(n2))
        #vales entre 20 e 30 PARES
        elif(0<= val%20 <10) and (val%20)%2 == 0 and val<40:
            resto = val - 20
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 20 R$'.format(n2))
        #vales entre 30 e 40 PARES
        elif(10<= val%20 <=18) and (val%20)%2 == 0:
            resto = val - 30
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 10 R$\n1 nota de 20 R$'.format(n2))
        #vales entre 40 e 50 PARES
        elif(0<= val%20 <10) and (val%20)%2 == 0 and val>40:
            resto = val - 40
            n2 = resto/2
            print('Serão fornecidas\n{:.0f} notas de 2 R$\n2 nota de 20 R$'.format(n2))

def men50(val):
    #Valores entre 50 e 55 IMPARES
    if(0<= val%50 <5) and (val%50)%2 != 0:
        resto = val - 45
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n2 notas de 20 R$'.format(n2))
    #vales entre 55 e 65 IMPARES
    elif(5<= val%50 <15) and (val%50)%2 != 0:
        resto = val-55
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 notas de 50 R$'.format(n2))
    #vales entre 65 e 75 IMPARES
    elif (15<= val%50 <25) and (val%50)%2 != 0:
        resto = val - 65
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 notas de 10 R$\n1 nota de 50 R$'.format(n2))
    #vales entre 75 e 85 IMPARES   
    elif (25<= val%50 <35) and (val%50)%2 != 0:
        resto = val - 75
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 notas de 20 R$\n1 nota de 50 R$'.format(n2)) 
    #vales entre 85 e 95 IMPARES
    elif (35<= val%50 <45) and (val%50)%2 != 0:
        resto = val - 85
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n1 notas de 10 R$\n1 nota de 20 R$\n1 nota de 50 R$'.format(n2))
    #vales entre 95 e 100 IMPARES
    elif (45<= val ) and (val%50)%2 != 0:
        resto = val - 95
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 5 R$\n2 nota de 20 R$\n1 nota de 50 R$'.format(n2))
    #vales entre 50 e 60
    elif(0<= val%50 <10) and (val%50)%2 == 0:
        resto = val - 50
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 notas de 50 R$'.format(n2))
    #vales entre 60 e 70
    elif(10<= val%50 <20) and (val%50)%2 == 0:
        resto = val - 60
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 10 R$\n1 notas de 50 R$'.format(n2))
    #valores entre 70 e 80
    elif(20<= val%50 <30) and (val%50)%2 == 0:
        resto = val - 70
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 20 R$\n1 notas de 50 R$'.format(n2))
    #valores entre 80 e 90
    elif(30<= val%50 <40) and (val%50)%2 == 0:
        resto = val - 80
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n1 nota de 10 R$\n1 notas de 20 R$\n1 nota de 50 R$'.format(n2))
    #valores entre 90 e 100
    elif(40<= val%50 ) and (val%50)%2 == 0:
        resto = val - 90
        n2 = resto/2
        print('Serão fornecidas\n{:.0f} notas de 2 R$\n2 nota de 20 R$\n1 notas de 50 R$'.format(n2))

def clear():
    import os
    os.system('cls')
caixa()