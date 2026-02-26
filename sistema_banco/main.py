from banco import *

def menu_principal():
    print("\n=== BANCO PYTHON ===")
    print("1 - Criar conta")
    print("2 - Login")
    print("3 - Sair")

while True:
    menu_principal()
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        senha = input("Senha: ")

        if criar_conta(nome, senha):
            print("Conta criada!")
        else:
            print("Conta já existe!")

    elif opcao == "2":
        nome = input("Nome: ")
        senha = input("Senha: ")

        conta = login(nome, senha)

        if conta:
            print("Login realizado!")

            while True:
                print("\n1 - Depositar")
                print("2 - Sacar")
                print("3 - Ver saldo")
                print("4 - Sair")

                escolha = input("Escolha: ")

                if escolha == "1":
                    valor = float(input("Valor: "))
                    depositar(conta, valor)

                elif escolha == "2":
                    valor = float(input("Valor: "))
                    if sacar(conta, valor):
                        print("Saque realizado!")
                    else:
                        print("Saldo insuficiente!")

                elif escolha == "3":
                    contas = carregar_contas()
                    for c in contas:
                        if c["nome"] == conta["nome"]:
                            print("Saldo:", c["saldo"])

                elif escolha == "4":
                    break
        else:
            print("Login inválido!")

    elif opcao == "3":
        break