def login():
    print("\nFaça seu login")
    user = input("Digite seu usuário: ")
    senha = int(input("Digite sua senha: "))
    if user in lista_user:
        if senha in lista_senha:
            if lista_user.index(user) == lista_senha.index(senha):
                conta(user)
            else:
                print("Usuário ou senha incorreta! Tente novamente")
                login()
        else:
            print("Usuário ou senha incorreta! Tente novamente")
            login()
    else:
        print("Usuário ou senha incorreta! Tente novamente")
        login()


def cadastro():
    print("Banco de Diadema\n")
    print("1 - Realizar Login")
    print("2 - Realizar Cadastro")
    print("3 - Sair")
    entrada = int(input("\nEscolha uma opção: "))
    if entrada == 1:
        login()
    elif entrada == 2:
        a = input("Digite seu nome: ")
        b = int(input("Digite sua senha: "))
        lista_user.append(a)
        lista_senha.append(b)
        lista_saldo.append(300)
        print("Cadastrado!")
        login()
    elif entrada == 3:
        print("\nAté mais!")
    else:
        print("Opção inválida! Tente novamente")
        cadastro()


def conta(user): #função quando usuário entra na conta
    print("______________________________\n")
    print(f"Bem-vindo, {user}\n")
    print("1 - Consultar o saldo")
    print("2 - Realizar saque")
    print("3 - Realizar depósito")
    print("4 - Sair")
    opc = int(input("\nEscolha uma opção: "))
    var = lista_user.index(user)
    if opc == 1:
        print("R$", lista_saldo[var])
        conta(user)
    elif opc == 2:
        saque = float(input("\nDigite a quantia do seu saque: R$ "))
        if saque <= lista_saldo[var]:
            lista_saldo[var] -= saque
            print("\nSaque concluído com sucesso!")
            conta(user)
        else:
            print("\nSaldo insuficiente!")
            conta(user)
    elif opc == 3:
        deposito = float(input("\nQuanto deseja depositar: R$ "))
        lista_saldo[var] += deposito
        print("Depósito concluído!\n")
        conta(user)
    elif opc == 4:
        print(f"\nAté mais, {user}!")
    else:
        print("\nOpção inválida! Tente novamente")
        conta(user)
        
lista_user = ["Rudy", "Brian", "Dexter"] 
lista_senha = [1234, 4321, 1221]
lista_saldo = [352, 1023, 587]
cadastro()