def calcular_desconto(preco_produto, desconto):
    #Transformando o valo do desconto em porcentagem
    porcento = desconto / 100
    preco_final = preco_produto - (preco_produto * porcento)
    return preco_final

preco = float(input("Digite o preço do produto: "))
desconto_pro = float(input("Digite quanto você quer dar de desconto: "))

valor_final = calcular_desconto(preco, desconto_pro)
print(valor_final)