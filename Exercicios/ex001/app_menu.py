opcao = 0


while opcao != 3:
    print("1 - Receber um elogio")
    print("2 - Calcular o fatorial")
    print("3 - Sair do sistema")
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        print("Você irá se tornar um Dev")
    elif opcao == 2:
        print("Calcular fatorial!\n")
        numero = int(input("Digite o numero que deseja descobrir o fatorial: "))
        
        fat = numero
        
        for valor in range (1, numero, 1):
            fat = fat * valor
            
        print(f"O fatorial de {numero} é {fat}")
        
    elif opcao == 3:
        print("Saindoo")
        
    else:
        print("Opção invalida")