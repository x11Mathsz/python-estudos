opcao_escolhida = 0
atendimentos_total = 0
atendimentos_resolvidos = 0
atendimentos_pendentes = 0
tempo_total_atendimentos = 0
tempo_total_minutos = 0
tempo_total_horas = 0
minutos_gastos = 0
opcao_atendimento = 0
tipo_problema_str = ""
situacao_atendimento = ""

while opcao_escolhida != 4:
    print("\nControle de Atendimentos!")
    print("1 - Registrar atendimento.")
    print("2 - Consultar prazo estimado.")
    print("3 - Ver resumo do turno.")
    print("4 - Encerrar!")

    # Verficando se o usuário digitou um número inteiro
    try:
        opcao_escolhida = int(input("\nQual opção você deseja escolher? \n--> "))

    except ValueError:
        print("Erro! Digite apenas números para esolher um opção!")
        opcao_escolhida = 0

    # Opções do menu
    match opcao_escolhida:
        case 1:
            # Verifcando se o nome está vazio
            nome_bool = False
            nome = ""
            print("\nRegistrar atendimento!")
            while nome_bool != True:
                nome = input("Nome do solicitante: \n--> ")

                if not nome.strip() or not nome.replace(" ", "").isalpha():
                    print("\nO nome deve conter apenas letras e não pode estar vazio!")
                else:
                    nome_bool = True
                    print(f"Olá {nome} \n")
            # verificando o tipo de atendimento
            tipo_atendimento = False
            while tipo_atendimento != True:

                try:
                    opcao_atendimento = int(
                        input(
                            f"\n{nome} escolha o tipo de atendimento: \n\t1 - Computador \n\t2 - Impressora \n\t3 - Sistema \n\t4 - Rede \n\t5 - Outro \n\t--> "
                        )
                    )
                    if opcao_atendimento >= 1 and opcao_atendimento <= 5:
                        match opcao_atendimento:
                            case 1:
                                print("1 - Computador")
                                tipo_problema_str = "Computador"
                            case 2:
                                print("2 - Impressora")
                                tipo_problema_str = "Impressora"
                            case 3:
                                print("3 - Sistema")
                                tipo_problema_str = "Sistema"
                            case 4:
                                print("4 - Rede")
                                tipo_problema_str = "Rede"
                            case 5:
                                print("5 - Outro")
                                tipo_problema_str = "Outro"

                        tipo_atendimento = True
                    else:
                        print(
                            "Você escolheu um numero que não está na lista! Escolha outro!"
                        )
                except ValueError:
                    print("Digite apenas números para escolher a opção")

            # Usando while até o usuário digitar a opção correta
            quantidade_bool = False
            while quantidade_bool != True:
                # Verificando se o tempo está em inteiros
                try:
                    minutos_gastos = int(
                        input(f"{nome} agora digite o tempo gasto: \n--> ")
                    )

                    # Verficando se os minutos são positivos
                    if minutos_gastos <= 0:
                        print("Digite apenas números inteiros positivos!")
                    else:
                        tempo_total_atendimentos += minutos_gastos
                        quantidade_bool = True
                except ValueError:
                    print("Erro! Digite apenas números!")

            # Verficando se a situação do atendimento está vazio!
            situacao_bool = False
            while situacao_bool != True:
                situacao_atendimento = input(
                    f"{nome} este atendimento foi resolvido? [S] / [N] \n--> "
                )
                if not situacao_atendimento.strip():
                    print(
                        "Campo vazio ou com espaços em brancos! Escolha a opção correta!\n"
                    )
                elif situacao_atendimento.upper() == "S":
                    situacao_atendimento = "Resolvido"
                    atendimentos_resolvidos += 1
                    atendimentos_total += 1
                    situacao_bool = True
                elif situacao_atendimento.upper() == "N":
                    situacao_atendimento = "Não resolvido"
                    atendimentos_pendentes += 1
                    atendimentos_total += 1
                    situacao_bool = True
                else:
                    print("Opção invalida! Escolha a opção correta!")
                    situacao_bool = False

            print(
                f"Atendimento registrado! \nSolicitante: {nome} \nCategoria: {tipo_problema_str} \nTempo gasto: {minutos_gastos} minutos \nSituação: {situacao_atendimento}"
            )
            
        case 2:
            prazo_bool = False
            opcao_prazo = 0
            
            #Verificando se o usuário digitou um numero
            while prazo_bool != True:
                
                try:
                    print("\nConsultar prazo estimado!")
                    print("1 - Baixa \n2 - Média \n3 - Alta \n4 - Crítica")
                    opcao_prazo = int(input("Digite a opção que você deseja \n--> "))
                    if opcao_prazo >= 1 and opcao_prazo <= 4:
                        match opcao_prazo:
                            case 1:
                                print("Baixa: atendimento em até 8 horas")
                            case 2:
                                print("Média: atendimento em até 4 horas")
                            case 3:
                                print("Alta: atendimento em até 1 hora")
                            case 4:
                                print("Crítica: atendimento imediato")
                        
                        prazo_bool = True
                    else:
                        print("Você escolheu uma opção que não está na lista!")
                except ValueError:
                    print("Digite apenas números para escolher a opção")
        case 3:
            
            
            #checando se tem atendimentos para mostrar o resumo
            if atendimentos_total > 0:
                print("\n===== RESUMO DO TURNO =====")
                print(f"Atendimentos registrados: {atendimentos_total}")
                print(f"Resolvidos: {atendimentos_resolvidos}")
                print(f"Pendentes: {atendimentos_pendentes}")
                if tempo_total_atendimentos >= 61:
                    tempo_total_horas = tempo_total_atendimentos // 60
                    tempo_total_minutos = tempo_total_atendimentos % 60
                    print(f"Tempo total gasto: {tempo_total_horas} horas e {tempo_total_minutos} minutos")
                else:
                    print(f"Tempo total gasto: {tempo_total_atendimentos} minutos")
                
                
                
                tempo_media_atendimentos = tempo_total_atendimentos / atendimentos_total
                print(f"Média de tempo: {tempo_media_atendimentos} minutos")
            else: 
                print("Nenhum atendimento foi registrado neste turno.")
        case 4:
            print("Encerrando sistema")