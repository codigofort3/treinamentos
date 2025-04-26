senha_correta = "Veryfloe82"
while True:
    senha = input("Digite a sua senha: ")
    if senha == senha_correta:
        print("Senha correta , acesso permitido!")
        break
    else:
        print(
            "Senha incorreta,para ter acesso à conta você precisa digitar a senha correta!")
