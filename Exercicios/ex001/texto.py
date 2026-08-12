texto1 = "Este texto quebra de linha aqui \nPorém aqui temos uma \ttabulação."
print(texto1)

texto2 = "texto em minusculas AINDA É texto"
print(texto2.capitalize())
print(texto2.upper())
print(texto2.lower())

#verficando o começo de um texto
print(texto2.startswith("Tex")) #False

#Verificando o final de um texto
print(texto2.endswith("o"))

#verficando se uma variavel contem um determinado caracter
#Forma 1 usando count para contar
print(texto2.count("@")) 
#Forma 2 verificando se possui dentro da variavel
print("em" in texto2) #True

#Substituindo uma palavra dentro de uma variavel
print(texto2.replace("AINDA", "com certeza"))