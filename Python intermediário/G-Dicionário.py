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

#dicionários dentro de dicionários:

cliente = {
    'cliente1': {
        'nome': 'antonio',
        'sobrenome': 'frio'
    },
    'cliente2':{
        'nome': 'oligar',
        'sobrenome': 'abrao'
    }
}
for keys, values in cliente.items(): 
    print(f'Exibindo {keys} ')
    for k,v in values.items():
        print(f'O {k} = {v}')

#para copiar um dicionário, não basta atribuir a outro, pois vai aletrar o original
# o jeito certo é usando o .copy()

v=d1.copy()
v['chave1']='peido'
print(d1)
print(v)

d2.pop('chave2')
print(d2)
