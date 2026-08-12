def calcular_media(nota_a, nota_b, nota_c):
    media = (nota_a + nota_b + nota_c) / 3
    return media

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
def pedir_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            
            if nota >= 0 and nota <= 10:
                return nota
            
            print("A nota deve estar entre 0 e 10.")
            
        except ValueError:
            print("Digite apenas numeros!")

nota_um = pedir_nota("Digite a primeira nota: ")
nota_dois = pedir_nota("Digite a segunda nota: ")
nota_tres = pedir_nota("Digite a terceira nota: ")

media_final = calcular_media(nota_um, nota_dois, nota_tres)
situacao = verificar_situacao(media_final)

print(f"Sua média foi {media_final:.2f} - Situação: {situacao}")

