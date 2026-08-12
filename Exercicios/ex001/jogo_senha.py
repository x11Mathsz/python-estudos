resposta = ""
tentativa = 0

while resposta != "python":
    resposta = input("Digite a senha: ")
    tentativa += 1

print("A senha correta foi digitada!")
print(f"Foi preciso usar {tentativa} para o acerto.")