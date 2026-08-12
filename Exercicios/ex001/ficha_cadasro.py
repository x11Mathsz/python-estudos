#Nome
#Peso
#Altura
#Idade
#Tem peso minimo para doar
#Tem idade minima para doar

print("Cadastro de doadores de sangue")

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
peso = float(input("Digite seu peso em kg: "))
altura = int(input("Digite sua altura em cm: "))

idade = 2026 - ano_nascimento

tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16

texto_saida = f"\tNOME: {nome}\n\tPESO: {peso} kg\n\tALTURA: {altura} cm\n\tIDADE: {idade}\n\tTEM PESO MINIMO PARA DOAR: {tem_peso_minimo}\n\tTEM IDADE MINIMA PARA DOAR: {tem_idade_minima}"

print(texto_saida)