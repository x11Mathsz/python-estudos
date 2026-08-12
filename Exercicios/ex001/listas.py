calorias = []

resposta = ""

while resposta.upper() != "NÃO":
    caloria = int(input("Quantas calorias você consumiu nesta refeição? "))
    calorias.append(caloria)
    
    resposta = input("Deseja informar as calorias de mais uma refeição? ")
    
total = 0
for caloria in calorias:
    print(f"Nesta refeição foram consumidas {caloria} calorias") 
    total = total + caloria
    
media = total / len(calorias)
print(f"Você consumiu uma média de {media} calorias por refeição")