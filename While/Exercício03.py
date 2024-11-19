senha = input("Digite a senha: ")
confirme_senha = input("Confirme a senha: ")

while confirme_senha != senha:
    print("Senha errada, digite novamente.")
    confirme_senha = input("Confirme a senha: ")
    if confirme_senha == senha:
        print("Senha confirmada, parabéns!")