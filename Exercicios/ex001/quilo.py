print("Quilão do Matheuzao")

preco_quilo = float(input("Digite o preço cobrado por quilo: "))
peso_prato = float(input("Digite o peso do prato do cliente: (em kg) "))

preco_prato = preco_quilo * peso_prato

print(f"O valor do do prato é R${preco_prato:.2f}")

if peso_prato > 1:
    print("Como o peso do prato do prato do cliente ultrapassou 1kg, ele deve pagar apenas o valor fixo de R$80,00")