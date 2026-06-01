tentativas=3
login_cadastrado=input ("Cadastre um login: ")
senha_cadastrada=input ("Cadastre uma senha: ")

while tentativas != 0:
    login_digitado=input("Digite o seu login: ")
    senha_digitada=input("Digite o sua senha: ")
    if login_digitado == login_cadastrado and senha_digitada == senha_cadastrada:
        print("Login e senha corretos. Acesso permitido. ")
        break
    else:
            tentativas = tentativas - 1
            print("Tentativas restantes: ", tentativas)
else:
    print("Número máximo de tentativas excedido. Acesso negado!")            