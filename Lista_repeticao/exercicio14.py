import pandas as pd

df = pd.DataFrame(columns=["Codigo_da_Cidade", "NUm_Veiculos_passeio", "NUm_Acidentes_Com_Vitimas"])

#==========================================================Gerando Dados de Teste=============================================================================================
"""
#gerardados de teste
from random import randint

for i in range (5):
    codigo_cidade = str(i)
    num_veiculos_passeio = randint(150, 4000)
    num_acidentes_com_vitimas = randint(3, 70)
    df.loc[i] = [codigo_cidade , num_veiculos_passeio, num_acidentes_com_vitimas]
"""
for i in range (5):
    codigo_cidade = input('Digite o codigo da cidade: ')
    num_veiculos_passeio = int(input('Digite o numero de carros de passeio: '))
    num_acidentes_com_vitimas = int(input('Digite o numero de acidentes com vitimas: '))
    df.loc[i] = [codigo_cidade , num_veiculos_passeio, num_acidentes_com_vitimas]

print(df)
print('\n')
print('-'*80)

#==========================================================Calculando o maior e menor indicies=============================================================================================

maior_indice = df["NUm_Acidentes_Com_Vitimas"].max()
print("\033[0;31m="*20,"Maior numero de Acidentes","="*50,"\033[m")
print('\n')
print(df.loc[df["NUm_Acidentes_Com_Vitimas"] == maior_indice])
print('\n')


menor_indice = df["NUm_Acidentes_Com_Vitimas"].min()
print("\033[0;32m="*20,"Menor Numero de Acidentes","="*50,'\033[m')
print('\n')
print(df.loc[df["NUm_Acidentes_Com_Vitimas"] == menor_indice])

#==========================================================Calculando a media de veiculos=============================================================================================

print("\n")
print('\033[0;34m='*20,'Media de veiculos nas cidades',"="*50,'\033[m')
print('\n')
print('media = ',round(df["NUm_Veiculos_passeio"].mean()))

#==========================================================Media de acidentes em cidades com menos de 2000 veiculos de passeio=============================================================================================

cidades_veiculos = df.loc[df["NUm_Veiculos_passeio"]<2000]
print("\n")
print('\033[0;35m='*20,'Media de acidentes em cidades com menos de 2000 veiculos',"="*20,'\033[m')
print('\n')
print("media = ",round(cidades_veiculos["NUm_Acidentes_Com_Vitimas"].mean()))
print('\n')
