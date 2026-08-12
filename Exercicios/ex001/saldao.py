#Pagamento no boleto 5% de desconto sobre o valor da compra
#Pagemento no cartao ciente pode escolher parcelar a compra em até 12x

print("Saldão da alegria!")

total_compra = float(input("Digite o valor total da compra do cliente: "))
forma_pagamento = int(input("Selecione a forma de pagmento: \n\t1 - Boleto \n\t2 - Cartão \n-> "))

if forma_pagamento == 1:
    valor_com_desconto = total_compra - (total_compra * 0.05)
    print(f"O valor final da sua compra foi de R${valor_com_desconto:.3f}")
else:
    parcelas = int(input("Informe o numero de parcelas desejadas: "))
    valor_parcela = total_compra / parcelas
    print(f"O totalda compra de R${total_compra:.3f} será pago em {parcelas} parcelas de R${valor_parcela:.2f}")