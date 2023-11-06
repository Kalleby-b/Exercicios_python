from time import sleep
from tqdm import tqdm
print("="*60)
nome = input('Digite o nome:  ')
idade = input('Digite a idade: ')
salario = input('Digite o salario: ')
Sexo = input('Difite o Sexo(F ou M): ')
Estado_civil = input('Digite o Estado Civil(S , C , V ou D): ')
print("="*60)

Sexo = Sexo.upper()
Estado_civil = Estado_civil.upper()

lista_variaveis = ['NOME', 'IDADE' , 'SALARIO', 'SEXO', 'ESTADO CIVIL']

#================================== Verificando a variavel nome ===============================================================
if len(nome) < 3:
    print('\033[0;34m')
    for i in tqdm(range(6)):
        sleep(0.5)
    print('\033[m')

    print('\033[3;31mErro!! Nome tem menos de 3 caracteres\033[m')
    verificar = False
    while verificar == False:
        nome = input('Digite um nome Valido: ')
        if len(nome) < 3:
            verificar = False
        else:
            verificar = True


#================================== Verificando a variavel idade ===============================================================
if str(idade).isalpha() == True or str(idade).isnumeric() == False or int(idade) <= 0 or int(idade) > 150:
    print('\033[0;34m')
    for i in tqdm(range(6)):
            sleep(0.5)
    print('\033[m')

    print('\033[3;31mErro!! Idade deve ser um numero Inteiro entre 0 e 150!!\033[m')

    verificar = False
    while verificar == False:
        idade = input('Digite uma idade Valida: ')
        if str(idade).isalpha() == True or str(idade).isnumeric() == False or int(idade) <= 0 or int(idade) > 150 :
            verificar = False
        else:
            verificar = True



        
#================================== Verificando a variavel Salário ===============================================================
if str(salario).isalpha() == True or float(salario) <= 0:
    print('\033[0;34m')
    for i in tqdm(range(5)):
            sleep(0.5)
    print('\033[m')       

    print('\033[3;31mErro!! Salario deve ser um NUMERO maior que 0!!\033[m')

    verificar = False
    while verificar == False:
        salario = input('Digite um Salario Valido: ')
        if str(salario).isalpha() == True or float(salario) <= 0:
            verificar = False
        else:
            verificar = True



#================================== Verificando a variavel sexo ===============================================================
if str(Sexo).isnumeric() == True or (Sexo != "F" and Sexo != "M") :
    print('\033[0;34m')
    for i in tqdm(range(3)):
            sleep(0.5)
    print('\033[m')

    print('\033[3;31mErro!! Sexo deve ser "F" ou "M" !!\033[m')

    verificar = False
    while verificar == False:
        Sexo = input('Digite um Sexo Valido: ')
        if  str(Sexo).isnumeric() == True or (Sexo != "F" and Sexo != "M"):
            verificar = False
        else:
            verificar = True



#================================== Verificando a variavel Estado_civil ===============================================================
if str(Estado_civil).isnumeric() == True or (Estado_civil != "C" and Estado_civil != "S" and Estado_civil != "V" and Estado_civil != "D") :
    print('\033[0;34m')
    for i in tqdm(range(3)):
            sleep(0.5)
    print('\033[m')        

    print('\033[3;31mErro!! Estado civil deve ser "S", "C", "V" ou "D" !!\033[m')

    verificar = False
    while verificar == False:
        Estado_civil = input('Digite um Estado civil Valido: ')
        if str(Estado_civil).isnumeric() == True or (Estado_civil != "C" and Estado_civil != "S" and Estado_civil != "V" and Estado_civil != "D"):
            verificar = False
        else:
            verificar = True


print('\033[0;32m')
for i in tqdm(range(6)):
    sleep(0.5)
for i in lista_variaveis:
     print("{} PASSOU...".format(i))
     sleep(0.5)
print('\033[m')