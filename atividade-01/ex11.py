while True:
    login = input("digite sua forma de login: ")
    senha = input("digite sua senha: ")

    if login == senha:
        print("ERRO! Login e senha são iguais")
        pass
    else:
        print("seu login foi realizado com sucesso!")
        break