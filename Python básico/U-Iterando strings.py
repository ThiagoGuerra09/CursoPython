"""Iteraçaõ de strings
Iterar é básicamente passar por cada indice de uma string
String original é imutavel, a gnt altera é as outras 
"""
#exemplo padrão
frase='o rato roeu a roupa do rei de roma'
tamfrase=len(frase)
contador=0
novastring=''
while contador<10:
    print(frase[contador])
    novastring+=frase[contador] #concatenando cada letra da "frase" na nova string 
    contador +=1
    print(novastring)

#aqui fiz um exemplo que pega as letras minusculas do r em R maiusculo
frase='o rato roeu a roupa do rei de roma'
tamfrase=len(frase)
contador=0
novastring=''
while contador<tamfrase:
    letra= frase[contador] 
    if letra =="r":
        novastring+='R'
    else:
        novastring+=letra
    contador +=1
print(novastring)
