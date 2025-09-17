produtos = []
opcao = 0

while opcao != 4:
    print("\n ===== MENU =====")
    print("1- Cadastrar produto")
    print("2- Listar produto")
    print("3- Remover produto")
    print("4- Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            produto = input("Digite nome do produto: ")
            produtos.append(produto)
            print(f"Produto {produto} cadastrado!")
        elif opcao == 2:
            if len (produtos) == 0:
                print("Nenhum produto cadastrado")
            else:
                print("\n === LISTA DE PRODUTOS ===")
                for i, p in enumerate(produtos, start = 1):
                    print(f"{i}. {p}")
        elif opcao == 3:
            if len (produtos) == 0:
                print("Nenhum produto para remover")
            else:
                for i, p in enumerate (produtos, start=1):
                    print(f"{i}.{p}")
                try:
                    indice = int(input("Digite o numero do produto para remover: "))
                    if 0 <= indice < len (produtos):
                        removido = produtos.pop(indice)
                        print(f"Produto '{removido}' removido!")
                    else:
                        print("Numero invalido!")
                except ValueError:
                    print ("Digite apenas números.")
        elif opcao == 4:
            print("Saindo do programa...")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Digite apenas números.")



        
