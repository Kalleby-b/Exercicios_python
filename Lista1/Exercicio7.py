peso = int(input('Qual o peso do peixe? '))
excesso = peso - 50
if excesso > 0:
    multa = excesso*4
    print('Você foi Multado!\nA multa é de {}\nVocê Ultrapassou {} Kg do limite'.format(multa,excesso))
else:
    print('Parabéns, você não foi multado!')