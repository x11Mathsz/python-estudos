op = 0

ficha = {}

while op != 4:
    print("\nFICHA CADASTRAL!")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informações da ficha")
    print("3 - Exibir a ficha completa")
    print("4 - Sair")
    op = int(input("Informe a opção deseja: "))
    
    if op == 1:
        # Inserir dados
        chave = input("Informe o campo que deseja cadastrar na ficha: ")
        valor = input("Informe o dado que deseja cadastrar neste campo: ")
        
        #ficha[chave] = valor
        # O mais correto é sempre usarmos os métodos ao inves de acessar direto o valor
        ficha.update({chave:valor})
        print(ficha)
    elif op == 2:
        # Recuperar dados
        #print(f"Os comandos diposniveis na ficha são {ficha.keys()}")
        print("Os campos disponiveis na ficha são:")
        for campos in ficha.keys():
            print(f"{campos}")
            
        # Exibindo somente o dado que o usuario digitar
        chave = input("Informe qual campo você gostaria de visualizar: ")
        
        if chave in ficha.keys:
            print(f"O campo {chave} contém o dado {ficha.get(chave)}")
        else:
            print("Valor inexistente!")
            
        #print(ficha.get(chave))
            
    elif op == 3:
        # Exibir dados
        print("Ficha Cadastral")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} -> {dado}")
    elif op == 4:
        print("Saindo do sistema")
        break
    else:
        print("Opção invalida")