import pandas as pd

df = pd.DataFrame(columns=["id" , 'Altura' , 'Peso'])

#============================================Gerando DAdos de Teste================================================================================================
def gerar():
    from random import randint
    for i in range(60):
        id = str(i+1)
        altura = randint(155, 280)
        peso = randint(40, 200)
        df.loc[i] = [id , altura , peso]

#============================================Inserindo Dados================================================================================================
def inserir():
    n = int(input('Quantos alunos são: '))
    for i in range(n):
        id = input('insira o codigo: ')
        altura = int(input('Insira a Altura(cm): '))
        peso = int(input('insira seu peso em Kg: '))
        df.loc[i] = [id , altura , peso]
        if id == 0:
            break

#============================================Mostrando o mais Alto e mais Baixo================================================================================================
def calc_altura():
    maior_altura = df["Altura"].max()
    print("\033[0;31m="*20,"Maior Altura","="*50,'\033[m')
    print('\n')
    print(df.loc[df["Altura"] == maior_altura])
    print('\n')

    menor_altura = df["Altura"].min()
    print("\033[0;32m="*20,"Menor Altura","="*50,'\033[m')
    print('\n')
    print(df.loc[df["Altura"] == menor_altura])
    print('\n')

    med= df["Altura"].mean()
    print("\033[0;34m="*20,"Media de altura","="*50,'\033[m')
    print('\n')
    print("media de altura: {:.2f} ".format(med))
    print('\n')

#============================================Mostrando o pais gordo e o mais magro================================================================================================

def calc_peso():
    maior_peso = df["Peso"].max()
    print("\033[0;31m="*20,"Maior Peso","="*50,'\033[m')
    print('\n')
    print(df.loc[df["Peso"] == maior_peso])
    print('\n')

    menor_peso = df["Peso"].min()
    print("\033[0;32m="*20,"Menor Peso","="*50,'\033[m')
    print('\n')
    print(df.loc[df["Peso"] == menor_peso])
    print('\n')

    med_peso= df["Peso"].mean()
    print("\033[0;34m="*20,"Media de Peso","="*50,'\033[m')
    print('\n')
    print("media de Peso: {:.2f} ".format(med_peso))
    print('\n')

#Chamando funções:
verificar = False
while verificar == False:
    n  = input('Gerar Dados ou inserir? (G/I)')
    if n == 'G':
        verificar = True
        gerar()
        calc_altura()
        calc_peso()
    elif n == 'I':
        verificar = True
        inserir()
        calc_altura()
        calc_peso()
    else:
        print('Opção inválida! Tente novamente...')
        verificar = False
    