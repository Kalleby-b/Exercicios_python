cpf_completo = input("digite seu cpf comtraçoes e pontos: ")
cpf = cpf_completo.replace('.','')
cpf = cpf.split('-')
digitos = []

#separando os digitos

for i in cpf[0]:
    digitos.append(i)

#realixando a soma
soma = 0
multiplicador = 2
digitos.reverse()
for i in range(len(digitos)):
    soma += int(digitos[i])*multiplicador 
    multiplicador+=1


#adquirindo o verificador
verificador = soma %11
verificador = 11 - verificador
if verificador == 10 or verificador == 11: 
    verificador = 0

#segunda parte
cpf2= int(cpf[0])*10+ verificador
cpf2 = str(cpf2)
digitos2 = []

#separando os digitos
for i in cpf2: 
    digitos2.append(i)


#realixando a soma 2

soma = 0
multiplicador = 2
digitos2.reverse()

for i in range(len(digitos)):
    soma+= int(digitos2[i])*multiplicador
    multiplicador+=1


verificador2 = soma%11
verificador2 = 11 - verificador2

if verificador2 == 10 or verificador2 == 11: 
    verificador2 = 0

verificador_final = str(verificador)+str(verificador2) 

if verificador_final == cpf[1]:
    print('O CPF {} é Valido!'.format(cpf_completo))

else:
    print('O CPF {} NÂO é Valido!'.format(cpf_completo))
