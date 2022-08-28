"""
o desafio consiste em validar um cpf 
cpf exemplo:168.995.350-09
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9


"""
#meu codigo
entrada=input('Digite um CPF, somente os numeros:\n')

if not entrada.isnumeric():
    print('digite somente numeros, sem "." ou "-"')
else: 
    if not len(entrada)==11:
        print('esta faltando numero')
    else:
        contador=0 #contador para passar de letra em letra na string entrada
        acumulador=0 #acumulador que guarda os resultados das multiplicações
        for x in range(10,1,-1):
            entrada_int=int(entrada[contador])
            acumulador=acumulador+(entrada_int*x)
            contador+=1
        #primeiro digito
        result=11-(acumulador%11)
        if result>9:
            primeiro=0
        else:
            primeiro=result
        #juntando com o resto da string
        primeiro=str(primeiro)
        cpfvalidado=entrada[0:9]+primeiro
        contador=0
        acumulador=0
        for n in range(11,1,-1):
            cpfvalidadoInt=int(cpfvalidado[contador])
            acumulador=acumulador+(cpfvalidadoInt*n)
            contador+=1
        #segundo digito
        result=11-(acumulador%11)
        if result >9:
            segundo=0
        else:
            segundo=result
        #juntando o segundo digito com o resto da string
        segundo=str(segundo)
        cpfvalidado=cpfvalidado+segundo

        if entrada==cpfvalidado:
            print('Esse CPF é verdadeiro')
        else:
            print('Esse CPF não existe')

#codigo do professor
 # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')

        