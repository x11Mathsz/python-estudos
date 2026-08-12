lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for valor in lista_numeros:
        soma += valor
        
    print(f"A soma dos valores é: {soma}")
    media = soma / len(lista_numeros)
    print(f"A media é {media}")
    
except ZeroDivisionError:
    print("Não é possivel dividir por 0")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")