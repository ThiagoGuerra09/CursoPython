"""Formatação de strings"""

'''Exemplo anterior'''
nome='Luis'
idade=56
altura=1.8
peso=80
imc=peso/altura**2

print(nome, 'tem', idade,'anos e o imc é:',imc)
#modo atualizado
print(f'{nome} tem {idade} anos e o imc é:{imc}')
#se quiser delimitar casas decimais do float do imc
print(f'{nome} tem {idade} anos e o imc é:{imc:.2f}')
#outra função, .format()
print('{} tem {} anos e o imc é: {}'.format(nome,idade,imc))
print('{p} tem {n} anos e o imc é: {i}'.format(p=nome,n=idade,i=imc))
print('{0} tem {1} {1} anos e o imc é: {0}{2}'.format(nome,idade,imc))



