import os
restaurantes = ["Pizza", "Lasanha"]

def exibir_nome():
    print(""" 
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█ \n
      """)


def menu():
    print("1. Adicionar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair do app\n")


def finalizar_app():
    exibir_subtitulo("Saindo do app...")
    
def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar para a tela principal! ")
    main()
    
    
    
def exibir_subtitulo(texto):
    os.system('cls') #Limpar tela
    print(texto)
    print()
    


def opcao_inavalida():
    print("Opção invalida\n")
    voltar_ao_menu_principal()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes!")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"O restaurente {nome_restaurante} foi cadastro com sucesso!")
    voltar_ao_menu_principal()
    
    
def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes cadastrados!")
    
    for restaurante in restaurantes:
        print(f"{restaurante}")
        
        
    voltar_ao_menu_principal()


"""
def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção:\n"))
    # opcao_escolhida = int(opcao_escolhida)
    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurante")
    elif opcao_escolhida == 3:
        print("Ativar restaurante")
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_inavalida()
"""


# Escolhe opção usando try
def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção:\n"))
        # opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_inavalida()
    except:
        opcao_inavalida()
        
def escolher_opcao_while():
    opcao_escolhida = 0
    
        

"""
def escolher_opcao_match():
    opcao_escolhida = int(input("Escolha uma opção:\n"))
    match opcao_escolhida:
        case 1:
            print("Adicionar restaurante.")
        case 2:
            print("Listar restaurante.")
        case 3:
            print("Ativar restaurante.")
        case 4:
            finalizar_app()
        case _:
            print("Opção inválida.")
"""


def main():
    os.system("cls")
    exibir_nome()
    menu()
    escolher_opcao()
    # escolher_opcao_match()


if __name__ == "__main__":
    main()
