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
                equipamento_novo = cadastrar_equipamento()
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
                
                
                
#função para cadastrar equipemamento, um equipamento deve possuir patrimonio, tipo, setor, status
def cadastrar_equipamento():
    print("\nCadastrar Equipamento!")
    patrimonio = verificador_inteiros("Digite o patrimônio do equipamento: ", "Erro! Digite apenas números para registrar o patrimônio!")
    tipo = verificador_palavras("Digite o tipo do equipamento: ")
    setor = verificador_palavras("Digite o nome do setor: ")
    status = escolher_status()
    
    #Exibindo mensagem de criação 
    print(f"\n\tEquipamento Registrado! \n\tPatrimônio: {patrimonio} \n\tTipo do Equipamento: {tipo} \n\tSetor: {setor} \n\tStatus: {status}\n")
    
    novo_equipamento = {"patrimonio": patrimonio, "tipo": tipo, "setor": setor, "status": status}
    
    #retornando o equipamento
    return novo_equipamento


    
    
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