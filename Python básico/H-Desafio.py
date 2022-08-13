"""
Criar variavéis para o nome, idade, altura e peso de uma pessoa
Criar variavél com ano atual
Obter o ano de nascimento da pessoa
Obter o IMC com duas casas decimais 
Exibir um texto com todos os valores na tela usando F-Strings usando {}

"""
nome='Luiz'
idade=32
altura=1.8
peso=80.0

imc=peso/altura**2
born=2022-idade



print('{} tem {} anos, {} de altura e pesa {}kg'.format(nome, idade, altura, peso))
print(f'O imc de {nome} é {imc:.2f}')
print('{0} nasceu em {1}'.format(nome, born))