pedir_senha = str(input("Digite sua senha: "))
pedir_senha2 = str(input("Confirme sua senha: "))

def verificar_tamanho(pedir_senha, pedir_senha2):
   if len(pedir_senha) < 8:
      print("Senha deve ter pelo menos 8 caracteres") 
      pedir_senha = str(input("Digite sua senha: "))
      pedir_senha2 = str(input("Digite sua senha novamente: "))

def verificar_maiuscula(pedir_senha, pedir_senha2):
   if pedir_senha.isupper() == True:
      print("Senha deve ter pelo menos uma letra maiúscula")
      pedir_senha = str(input("Digite sua senha: "))
      pedir_senha2 = str(input("Digite sua senha novamente: "))

def verificar_minuscula(pedir_senha, pedir_senha2):
   if pedir_senha.islower() == True:
      print("Senha deve ter pelo menos uma letra minúscula")
      pedir_senha = str(input("Digite sua senha: "))
      pedir_senha2 = str(input("Digite sua senha novamente: "))

def verificar_numero(pedir_senha, pedir_senha2):
   if pedir_senha.isdigit() == True:
      print("Senha deve ter pelo menos um número")
      pedir_senha = str(input("Digite sua senha: "))
      pedir_senha2 = str(input("Digite sua senha novamente: "))

def verificar_igualdade(pedir_senha, pedir_senha2):
    if pedir_senha != pedir_senha2:
       print("Senhas devem ser iguais")
       pedir_senha = str(input("Digite sua senha: "))
       pedir_senha2 = str(input("Digite sua senha novamente: "))

verificar_igualdade(pedir_senha, pedir_senha2)
verificar_tamanho(pedir_senha, pedir_senha2)
verificar_maiuscula(pedir_senha, pedir_senha2)
verificar_minuscula(pedir_senha, pedir_senha2)
verificar_numero(pedir_senha, pedir_senha2)