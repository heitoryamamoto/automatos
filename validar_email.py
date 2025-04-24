import re

def validar_email(email):
    # Expressão regular para validar e-mails
    padrao = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
   
    # Verifica se o e-mail corresponde ao padrão
    if re.match(padrao, email):
        return "E-mail válido"
    else:
        return "E-mail inválido"

# Teste do programa
while True:
    email = input("Digite um e-mail (ou 'sair' para encerrar): ")
    if email.lower() == 'sair':
        break
    print(validar_email(email))