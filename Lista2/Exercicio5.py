def escolha ():
    print('='*60)
    a = float(input('Digite o primeiro numero: '))
    b = float(input('Digite o segundo número: '))

    escolha = input(""" 
    1-Média Aritimetica entre os numeros
    2-Diferença entre o maior e o menor
    3-Produto dos numeros
    4-DIvisão do primeiro pelo segundo     
    escolha: """)

    if escolha == '1':
        media = (a + b) / 2
        print ('A média de {} e {} é igual á {}'.format(a, b , media))
    elif escolha == '2':
        if a > b:
            diferenca = a - b
            print('A diferença de {} e {} é igual á {}'.format(a, b , diferenca))
        elif b > a:
            diferenca = b - a
            print('A diferença de {} e {} é igual á {}'.format(b, a , diferenca))
        else:
            print('Eles são Iguais a Diferença é 0')

    elif escolha == '3':
        produto= a * b
        print('{} x {} = {}'.format(a, b,produto ))

    elif escolha == '4':
        divisao = a/b
        print('O resultado da Divisão é = {:.2f}'. format(divisao))

    else:
        print("Opção Inválida!")
        escolha()

escolha()
