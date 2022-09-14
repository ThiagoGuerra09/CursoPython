"""
Em dicionário você cria o indice da lista, que é chamada chave
"""
d2=dict(chave='ola', chave2='pedro', chave3='queixada')
d1= {'chave1': 'conteudo'}
d1['chave2']= 'conteudo2' #tem como usar o metodo d1.update({'nova': 'valor'}) para atribuit valores e chaves também
print((d1))
print(d2['chave2'])#retorna pedro

if 'chave1' in d1:
    print('chave1')

print('chave' in d2.keys())#se tiver uma chave com esse nome volta true
print('ola' in d2.values())# se tiver um valor com esse nome volta true

for k in d2.items():#vem a chave e o valor
    print(k)