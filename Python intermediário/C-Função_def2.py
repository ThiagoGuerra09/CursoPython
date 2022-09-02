"""Funções parte 2"""

"""*args e **kwargs"""
def func(*args,**kwargs):#aqui passamos o *args, pois não sabemos a quantidade de valores que serão passados
    print(args) #* siginifica empacotamento, chamar sem o * siginificada desempacotamento
    print(kwargs['nome'])#se nãopassar nada entre [] vem tudo, se passar escolhe oq vc passou
    print(kwargs.get('sobrenome'))#outra forma de pegar o atributo
var = func(1,2,3,4,5,5, nome='antonio', sobrenome='lucco')#esse antonio, é um argumento nomeado, logo ele precisa ser chamado como keyword agrs

"""Global e local conceitos"""

variavel='guilherme'#escopo global pode ser acessado por função

def func1():
    print(variavel) #aqui vai printar a global pois não tem outra dentro, mas se tivesse a preferência é da local
func1()    

def func2():
    variavel='lucaco' #aqui ele deu prioridade pra local do que pra global
    print(variavel)
func2()    

def func3():
    global variavel #defini global para pegar a global
    variavel='lucaco' #alterei o valor da global
    print(variavel)#não é uma boa prática alterar a global no local
func3()    

print(variavel)#a global foi alterada na func3