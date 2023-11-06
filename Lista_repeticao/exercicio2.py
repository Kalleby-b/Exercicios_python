print("="*60)
user = input('Digite o nome de Usuario:  ')
password = input('Digite a senha: ')
print("="*60)
user = user.strip()
password = password.strip()

if password == user:
    verificar = False
    while verificar == False:
        print('Senha não pode ser igual ao usuario!!')
        user = input('Digite o nome de Usuario:  ')
        password = input('Digite a senha: ')
        print("="*60)
        user = user.strip()
        password = password.strip()
        if password == user:
            verificar == False
        else:
            verificar = True
            print("="*60)
            print('Seja bem vindo')