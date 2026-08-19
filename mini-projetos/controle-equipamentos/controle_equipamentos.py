def menu_controle_equipamentos():
    #Criando lista para equipamentos
    equipamentos = []
    
    #variavel para acessar o menu
    opcao = 0
    
    while opcao != 7:
        print("Controle de Equipamentos T.I")
        print("1 - Cadastrar equipamento")
        print("2 - Listar equipamentos")
        print("3 - Buscar equipamentos")
        print("4 - Alterar Status")
        print("5 - Mostrar resumo")
        print("6 - Deletar equipamento")
        print("7 - Sair")
        
        opcao = verificador_inteiros("--> ", "Erro! Digite apenas número para escolher a opção correta!")
        
        match opcao:
            case 1:
                equipamento_novo = cadastrar_equipamento(equipamentos)
                equipamentos.append(equipamento_novo)
                
            case 2:
                #listar equipamentos
                #verificando a lista de equipamentos está vazia
                if equipamentos:
                    for equipamento in equipamentos:
                        patrimonio_eqt = equipamento["patrimonio"]
                        tipo_eqt = equipamento["tipo"]
                        setor_eqt = equipamento["setor"]
                        status_eqt = equipamento["status"]
                        print(f"\nPatrimônio: {patrimonio_eqt} \nTipo: {tipo_eqt} \nSetor: {setor_eqt} \nStatus: {status_eqt}\n")
                else:
                    print("\nNenhum equipamentos foi registrado! Voltando para o menu!\n")
            case 3:
                #Buscar patrimonio
                #verificando se a lista está vazia
                if equipamentos:
                    
                    while True:
                        id_patrimonio = verificador_inteiros("Digite o número do patrimônio que deseja buscar: ", "Erro! Digite apenas números para realizar a busca!")
                    
                        equipamento_encontrado = buscar_equipamento(id_patrimonio, equipamentos)
                    
                        if equipamento_encontrado is not None:
                            print(f"\nPatrimônio: {equipamento_encontrado["patrimonio"]} \nTipo: {equipamento_encontrado["tipo"]} \nSetor: {equipamento_encontrado["setor"]} \nStatus: {equipamento_encontrado["status"]}\n")
                            break
                        else:

                            resposta = verificador_sim_nao("Não foi encontrado patrimonio digitado!\nDeseja retornar para o menu? [S/N] \n--> ")
                        
                            if resposta == "S":
                                print("\nVoltando...")
                                break
                        
                            
                else:
                    print("\nNenhum equipamentos foi registrado! Voltando para o menu!\n")
            
            case 4:
                #verificando se a lista está vazia
                if equipamentos:
                    
                    while True:
                        id_patrimonio = verificador_inteiros("Digite o número do patrimônio do equipamento que deseja realizar a alteração de status: ", "Erro! Digite apenas números para realizar a busca!")
                        
                        equipamento_encontrado = buscar_equipamento(id_patrimonio, equipamentos)
                        if equipamento_encontrado is not None:
                            print(f"\nPatrimônio: {equipamento_encontrado["patrimonio"]} \nTipo: {equipamento_encontrado["tipo"]} \nSetor: {equipamento_encontrado["setor"]} \nStatus: {equipamento_encontrado["status"]}\n")
                            #verificando se o usuário realmente quer realizar a alteração
                            resposta = verificador_sim_nao("Você deseja realmente realizar a alteração de status? [S/N]\n--> ")
                            if resposta == "S":
                                novo_status = escolher_status()
                                equipamento_encontrado["status"] = novo_status
                                print(f"Status do patrimônio {id_patrimonio} alterado para: {novo_status}")
                                break
                            else:
                                print("Voltando para o menu...")
                                break
                            
                        else:
                            resposta = verificador_sim_nao("Não foi encontrado patrimonio digitado!\nDeseja retornar para o menu? [S/N] \n--> ")
                                                    
                            if resposta == "S":
                                print("\nVoltando...")
                                break
                            
                    
                else:
                    print("\nNenhum equipamentos foi registrado! Voltando para o menu!\n")
            case 5:
                if equipamentos:
                    resumo = mostrar_resumo(equipamentos)
                    print(resumo)
                else:
                    print("\nNenhum equipamentos foi registrado! Voltando para o menu!\n")
                    
                
                
                
#função para cadastrar equipemamento, um equipamento deve possuir patrimonio, tipo, setor, status
def cadastrar_equipamento(equipamentos):
    print("\nCadastrar Equipamento!")
    patrimonio = verificador_inteiros("Digite o patrimônio do equipamento: ", "Erro! Digite apenas números para registrar o patrimônio!")
    
    
    #Verificando se possui patrimonio registrado
    while True:
        duplicado = verificador_duplicado(patrimonio, equipamentos)
            
        if duplicado:
            print("\nEste patrimonio já está em uso!")
            patrimonio = verificador_inteiros("\nDigite o patrimônio do equipamento: ", "Erro! Digite apenas números para registrar o patrimônio!") 
        else:
            break
    
    tipo = verificador_palavras("Digite o tipo do equipamento: ")
    setor = verificador_palavras("Digite o nome do setor: ")
    status = escolher_status()
    
    #Exibindo mensagem de criação 
    print(f"\n\tEquipamento Registrado! \n\tPatrimônio: {patrimonio} \n\tTipo do Equipamento: {tipo} \n\tSetor: {setor} \n\tStatus: {status}\n")
    
    novo_equipamento = {"patrimonio": patrimonio, "tipo": tipo, "setor": setor, "status": status}
    
    #retornando o equipamento
    return novo_equipamento

#função para mostrar resumo
def mostrar_resumo(equipamentos):
    #criando variaveis para contar
    count_equipamento = 0
    count_uso = 0
    count_manutencao = 0
    count_disponivel = 0
    
    for equipamento in equipamentos:
        count_equipamento += 1
        if equipamento["status"] == "Em uso":
            count_uso += 1
        elif equipamento["status"] == "Em manutenção":
            count_manutencao += 1
        elif equipamento["status"] == "Disponível":
            count_disponivel += 1
    
    return f"Total de equipamentos: {count_equipamento} \nEm                              uso: {count_uso} \nEm manutenção: {count_manutencao} \nDisponível: {count_disponivel}"
    

#função para verfificar o patrimonio registrado
def buscar_equipamento(patrimonio, equipamentos):
    for equipamento in equipamentos:
        if patrimonio == equipamento["patrimonio"]:
            return equipamento
    return None

#verificando sim ou não
def verificador_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
        
        if resposta == "S" or resposta == "N":
            return resposta
        
        print("Digite apenas S ou N")

#função para verificar se já temos um patrimonio registrado
def verificador_duplicado(patrimonio, equipamentos):
    for equipamento in equipamentos:
        if patrimonio == equipamento["patrimonio"]:
            return True
    
    return False

    
    
#função para escolher status espefico
def escolher_status():
    
    while True:
        options = verificador_inteiros("1 - Em uso \n2 - Em manutenção \n3 - Disponível \n--> ", "Erro! Digite apenas números para esolher a opção correta!")
        
        if options == 1:
            return "Em uso"
        elif options == 2:
            return "Em manutenção"
        elif options == 3:
            return "Disponível"
        print("Opção invalida! Tente novamente!")
        
        
    
#função para aceitar somento numeros inteiros
def verificador_inteiros(mensagem, mensagem_erro):
    while True:
        try:
            numero = int(input(mensagem))
            
            #verificando se o numero digitado é positivo
            if numero > 0:
                
                #se for, retorna o numero digitado e sai do programa
                return numero
            #não tem necessidade do else, então posso colocar um print caso seja digitado um numero negativo e 
            # o programa vai ficar executando até cair no return
            print("Digite apenas números positivos!")
            
        #caso seja digitado letras vamos cair no except
        except ValueError:
            print(mensagem_erro)
            
#função para verificar se possuem somente letras ou se não está vazia
def verificador_palavras(mensagem):
    while True:
        palavra = input(mensagem)
        
        if not palavra.strip() or not palavra.replace(" ", "").isalpha():
            print("Deve conter apenas letras, não pode estar vazio!")
        else:
            return palavra
        
        
        
menu_controle_equipamentos()