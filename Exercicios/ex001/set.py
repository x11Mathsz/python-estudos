# Criando um set vazio
conjunto = set()
print(type(conjunto))

# Criando um set a partir de uma lista
lista = ["Matheus", "David", "Cebolinha", "Matheus"]
print(lista)
conjunto2 = set(lista)

print(conjunto2)

# Criando um set com valores
conjunto3 = {"Cebolinha", "Magali", "Mônica", "Cascão", "Cebolinha"}
print(conjunto3)

# Adicionando um elemento (add)
conjunto3.add("Franjinha")
print(conjunto3)

# Removendo elementos que estão em outro set (difference_update)
conjunto4 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto5 = {"Playstation", "Nintendo64", "Sega Saturn", "Dreamcast"}

print(f"O primeiro set contém {conjunto4}")
print(f"O segundo set contém {conjunto5}")

conjunto4.difference_update(conjunto5)
print(f"O primeiro set contém {conjunto4}")

# Remover um elemento específico do set (remove)
conjunto4 = {"Mega Drive", "Super Nintendo", "Playstation"}
print(conjunto4)
conjunto4.remove("Mega Drive")
print(conjunto4)
# Se tentar remover o mesmo elemento que já foi removido irá acontecer um erro
#conjunto4.remove("Mega Drive")

# Remover um elemento específico do set (discard) com proteção
conjunto4.discard("Super Nintendo")
print(conjunto4)
# Se tentar remover o mesmo elemento, não irá acontecer erro
conjunto4.discard("Super Nintendo")
print(conjunto4)