

def menu_chamados():
    chamados = []
    
    
    opcao = 0
    while opcao != 4:
        print("\nControle de Chamados de T.I")
        print("1 - Registrar chamado")
        print("2 - Consultar prioridade")
        print("3 - Calcular tempo médio")
        print("4 - Sair")
        
        opcao = verificador_inteiro("--> ", "Erro! Digite apenas números para escolher uma opção.")
        
        match opcao:
            case 1:
                
                novo_chamado = registrar_chamado()
                chamados.append(novo_chamado)
                
            case 2:
                #Checando se tem chamado registrado
                if chamados:
                    for chamado in chamados:
                        quantidade_pessoas = chamado["quantidade"]
                        problema = chamado["problema"]
                        prioridade = calcular_prioridade(quantidade_pessoas, problema)
                        print(f"Nome: {chamado['nome']} \nPrioridade: {prioridade}")
                else:
                    print("Nenhum chamado foi registrado, voltando para o menu!")
                
            case 3:
                tempo_total_chamados = 0
                #Checando se tem chamado
                if chamados:
                    #tempo_medio = tempo_total_chamados / total_chamados
                    #print(f"Tempo medio {tempo_medio}")
                    
                    #Usando for para percorrer a lista para coletar o tempo
                    for chamado in chamados:
                        tempo_total_chamados += chamado["tempo"]
                    
                    tempo_medio = tempo_total_chamados /len(chamados)
                    print(f"Tempo medio {tempo_medio:.2f} minutos")
                    
                else:
                    print("Nenhum chamado foi registrado, voltando para o menu!")
            case 4:
                print("Saindo...")
            case _:
                print("Opção invalida!")
        
        
def verificador_inteiro(mensagem, mensagem_erro):
    while True:
        
        try:
            numero = int(input(mensagem))
            if numero > 0:
                
                return numero
            print("Digite numeros positivos")
        
        except ValueError:
            print(mensagem_erro)
        
def registrar_chamado():
    print("Registrar Chamado.")
    nome = verificar_nome("Digite o nome do solicitante: ")
    quantidade_pessoas = verificador_inteiro("Quantas pessoas foram afetadas: ", "Erro! Digite uma quantidade válida.")
    problema_afeta = verificar_sim_nao("O problema impede o trabalho? [S/N] ")
    tempo_estimado = verificador_inteiro("Digite o tempo: ", "Erro! Digite o tempo em minutos válidos.")
    
    
    print(f"\nChamado Registrado \nNome {nome} \nQuantidade: {quantidade_pessoas} \nProblema: {problema_afeta} \nTempo estimado: {tempo_estimado}")
    
    #Registrando o chamado, dicionario precisa ser algo como dic = {"nome": nome, "quantidade":, quantidade}
    novo_chamado = {"nome": nome,"quantidade": quantidade_pessoas,"problema": problema_afeta,"tempo": tempo_estimado}
    
    return novo_chamado
    
def calcular_prioridade(pessoas_afetadas, problema):
    pontos = 0
    
    if pessoas_afetadas > 10:
        pontos += 2
    else:
        pontos += 1
    if problema == "S":
        pontos += 2
    else:
        pontos += 1
        
    if pontos >= 4:
        return "Alta"
    else:
        return "Media"
    
    
def verificar_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
        
        if resposta == "S" or resposta == "N":
            return resposta
        
        print("Digite apenas S ou N")
    
def verificar_nome(mensagem):
    #Verificando se uma string está vazia ou com numeros
    while True:
        nome = input(mensagem)
        
        if not nome.strip() or not nome.replace(" ", "").isalpha():
            print("Deve contar apenas letras e não pode estar vazio!")
        else:
            
            return nome
    
        
        
menu_chamados()
#prioridade = calcular_prioridade(9,"N")
#print(prioridade)
