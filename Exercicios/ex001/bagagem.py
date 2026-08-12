"""
Uma companhia aera permite que seus cliente do tipo premium despache bagagens de até 32kg sem nenhum custo adicional,
enquanto os clientes do tipo gold podem levar malas de até 28kg sem nenhum custo adicional
e todos os demais devem pagar por qualquer bagagem despachada.
"""

tipo_cliente = input("Por favor, informe o tipo de cliente: \n\tPREMIUM \n\tGOLD \n\tREGULAR \n\t-> ")
peso_bagagem = float(input("Informe o peso da bagagem que o cliente deseja despachar: "))

if tipo_cliente.upper() == "PREMIUM":
    #o que acontece se o cliente for premium
    if peso_bagagem <= 32:
        #Exibi msg avisando que pode levar
        print(f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido! Não é necessário pagar nenhum valor para despachá-la")
    else:
        peso_excedente = peso_bagagem - 32
        #exibe msg avisando sobre o peso
        print(f"Os cliente {tipo_cliente} tem o direito a despacharem bagagens de até 32kg. A bagagem atual excede este peso em {peso_excedente}kg. Dirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional.")
elif tipo_cliente.upper() == "GOLD":
        #O que acontece se for gold
        if peso_bagagem <= 28:
            print(f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido! Não é necessário pagar nenhum valor para despachá-la")
        else:
            peso_excedente = peso_bagagem - 28
            #exibe msg sobre o peso
            print(f"Os cliente {tipo_cliente} tem o direito a despacharem bagagens de até 28kg. A bagagem atual excede este peso em {peso_excedente}kg. Dirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional.")
else:
    #se for regular
    print(f"Os cliente {tipo_cliente} não tem direito a bagagem gratuita. Dirija-se ao balcão de cobranças para realizar o pagamento pela bagagem.")