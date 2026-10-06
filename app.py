import random

saldo = 0
usuario = ""
senha = ""

cadastrado = False
executando = True

while executando:

    print("\n============ - ENTRAR - ============")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")
    print("====================================")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\n===== - CADASTRO - =====")

        usuario = input("Digite um usuário: ")
        senha = input("Digite uma senha: ")
        saldo = random.uniform(50, 1000)

        cadastrado = True

        print("\nUsuário cadastrado com sucesso!")
        print(f"Seu saldo inicial é: R$ {saldo:.2f}")


    elif opcao == "2":
        if not cadastrado:
            print("\nNenhum usuário cadastrado!")
            print("Faça o cadastro primeiro.")

        else:
            print("\n===== - LOGIN - =====")

            usuario2 = input("Usuário: ")
            senha2 = input("Senha: ")

            if usuario2 == usuario and senha2 == senha:
                print("\nLogin realizado com sucesso!")
                print(f"Bem-vindo, {usuario2}!")
                
                logado = True
                
                while logado:
                    print(f"===== - {usuario2} - =====")
                    print("1 - Perfil")
                    print("2 - Saldo")
                    print("3 - Alterar Senha")
                    print("4 - Sair da Conta")
                    print(f"=======================")
                    
                    opcao_usuario = input("\nEscolha uma opção: ")
                    
                    if opcao_usuario == "1":
                        print("===== - SEU PERFIL - =====")
                        print(f"Usuario: {usuario2}")
                        print(f"Saldo: R$ {saldo:.2f}")
                    
                    elif opcao_usuario == "2":
                        print("===== - SEU SALDO - =====")
                        print(f"Seu saldo é: R$ {saldo:.2f}")
                    
                    elif opcao_usuario == "3":
                        print("===== - ALTERAR SENHA - =====")
                        senha_atual = input("Digite sua senha atual: ")
                        
                        if senha_atual == senha:
                            senha_nova = input("Digite sua nova senha: ")
                            senha = senha_nova
                            print("Senha alterada com sucesso!")
                            
                        else:
                            print("Senha atual incorreta!")
                    
                    elif opcao_usuario == "4":
                        print("Saindo da conta...")
                        
                        logado = False

            else:
                print("\nUsuário ou senha incorretos!")


    elif opcao == "3":
        print("\nSaindo do sistema...")
        print("Obrigado por usar o sistema!")

        executando = False

    else:
        print("\nOpção inválida!")
        print("Escolha 1, 2 ou 3.")
