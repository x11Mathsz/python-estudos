#1. Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

#numero = int(input("Digite um número: "))

#if numero % 2 == 0 :
#    print(f"O número {numero} que você digitou é par!")
#else:
#    print(f"O número {numero} que você digitou é impar!")
"""
#2. Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos; Adolescente: 13 a 18 anos; Adulto: acima de 18 anos.

idade = int(input("Digite sua idade: "))

if idade <= 11:
    print("Criança")
elif 12 <= idade <= 17:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else:
    print("Valor invalido!")
"""
"""
3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
"""

usuarioNovo = input("Digite seu nome de usuário para criar um novo: ")
senhaNovo = input("Digite uma senha para esse usuário: ")
print("Usuário Criado\n")

usuario_teste = input("Digite seu usuário: ")
senha_teste = input("Digite sua senha: ")
print("Verificando...\n")

if usuario_teste == usuarioNovo and senha_teste == senhaNovo:
    print("Acesso autorizado, Bem-vindo :) ")
else:
    print("Verifique os valores digitados e tente novamente!")