

opcao_escolhida = 0

while opcao_escolhida != 4:
    print("Menu Chamados FHC " \
    "\n\t1 - Abrir chamado. " \
    "\n\t2 - Consultar orientações. " \
    "\n\t3 - Calcular prioridade. " \
    "\n\t4 - Encerrar")
    
    
    try:
        opcao_escolhida = int(input("\t-> "))
        
        if opcao_escolhida == 1:
                print("\nAbertura de chamado!")
                nome = input("Digite seu nome: ")
                setor = input("Digite seu setor: ")
                problema = input("Informe seu problema: ")
        
                print(f"\nChamado aberto! \nSolicitante: {nome}\nSetor: {setor} \nProblema: {problema}\n")
        
        elif opcao_escolhida == 2:
                print("\nConsultar orientações!")
                opcao_consultar = int(input("\t1 - Computador sem internet. " \
                "\n\t2 - Impressora não imprime." \
                "\n\t3 - Sistema não abre." \
                "\n\t4 - Telefone com problema. \n\t-> "))
        
                match opcao_consultar:
                    case 1:
                        print("PC SEM NET")
                    case 2:
                        print("Impressora")
                    case 3:
                        print("Sistema")
                    case 4:
                        print("Telefone")
                    case _:
                        print("Opção invalida!")
        
        elif opcao_escolhida == 3:
                print("\nCalcular prioridade.")
                quantidade = False
                while quantidade != True:
                    
                    try:
                        pessoas_afetadas = int(input("Quantas pessoas foram afetas? \n->"))
                        if pessoas_afetadas < 0:
                            
                            print("Digite apenas numeros inteiros positivos")
                        else:
                            quantidade = True
                    except ValueError:
                        print("Você precisa digitar apenas numeros inteiros!")
                    
                impede_trabalho = input("O problema impede totalmente o trabalho? [S/N] \n->")
                setor_critico = input("O setor é crítco? [S/N]  \n->")
        
                pontos = 0
        
                if pessoas_afetadas > 10:
                    pontos += 2
        
                if impede_trabalho.upper() == "S":
                    pontos += 2
        
                if setor_critico.upper() == "S":
                    pontos += 2
        
                #Classificação
                if pontos <= 1:
                    print(f"Prioridade baixa, {pontos}")
                elif pontos >= 2 and pontos <= 3:
                    print(f"Prioridade média, {pontos}")
                elif pontos >= 4 and pontos <= 5:
                    print(f"Prioridade alta, {pontos}")
                elif pontos >= 6:
                    print(f"Prioridade critica, {pontos}")
            
        elif opcao_escolhida == 4:
            print("Encerrando")   
        else:
            print("Opção invalida!")   
    except ValueError:
        print("Digite apenas numeros inteiros!")    
        

    

    

    

    

    
