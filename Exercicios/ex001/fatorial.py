
    
numero = int(input("Informe o numero"))

fat = numero

for valor in range (1, numero, 1):
    fat = fat * valor
    
print(f"O fatorial de {numero} é {fat}")