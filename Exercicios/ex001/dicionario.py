# Dados
# Star Wars - Episódio IV - Uma nova esperança, George Lucas, 1977, 775000000.00

# Criação do dicionario
dicionario = {}
print(type(dicionario))

dicionario = {"nome":"Star Wars - Episódio IV - Uma nova esperança", "diretor":"George Lucas", "bilheteria":775000000.00}


# Exibindo o dicionario completo
print(dicionario)

# Exibindo o valor de uma chave
print(dicionario["nome"])

# Inserindo uma nova chave e valor (gênero)
dicionario["gênero"] = "Space Opera"
print(dicionario)

# Método Keys
print(dicionario.keys())
for chave in dicionario.keys():
    print(chave)

# Método values
print(dicionario.values())

for valor in dicionario.values():
    print(valor)
    
# Método items
print(dicionario.items())

for chave, valor in dicionario.items():
    print(f"Chave = {chave} -- Valor = {valor}")
    
    
#Método get
#print(dicionario["publico"]) //retorna um erro pois não temos esse dado
print(dicionario.get("publico")) # retorna none, pois não temos
print(dicionario.get("nome"))

# Método setdefault
dicionario.setdefault("publico", 1000)
print(dicionario)
dicionario.setdefault("publico", 9000) # O publico não vai mudar, pois o setdefault quando percebe que já existe ele não altera o valor
print(dicionario)