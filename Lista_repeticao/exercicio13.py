import pandas as pd
conjuntos = pd.DataFrame(columns= ["Numero" , "Altura(cm)"])

#Caso Gerando dados de teste
"""
from random import randint
for i in range(10):
    Numero = str(i)
    altura = randint(150 , 280)
    conjuntos.loc[i] = [Numero , altura]

"""
#CAso inserir dados

for i in range(10):
    Numero = input('Digite o Numero: ')
    altura = int(input('Digite a altura em cm: '))
    conjuntos.loc[i] = [Numero , altura]


print(conjuntos)


altura_max = conjuntos["Altura(cm)"].max()
print("="*20, "\033[3;35mAluno mais alto\033[m", "="*20)
print(conjuntos.loc[conjuntos["Altura(cm)"]== altura_max])
print("_"*60)

altura_min = conjuntos["Altura(cm)"].min()
print("="*20, "\033[3;34mAluno mais baixo\033[m", "="*20)
print(conjuntos.loc[conjuntos["Altura(cm)"]== altura_min])
print("_"*60)


