#Grupo 22: 81633- Joao Henriques, 81271- Rodrigo Mira
#Jogo 2048

#=============================TAD Coordenada===================================#
def cria_coordenada(l, c):
    """
    Recebe dois numeros, verifica se podem formar uma coordenada e, se sim, devolve a coordenada formada por ambos. Se nao, devolve a string "cria_coordenada: argumentos invalidos" (levanta um erro)
    """    
    if isinstance(l, int) and l in (1, 2, 3, 4) and isinstance(c, int) and c in (1, 2, 3, 4): #verifica se os elementos da coordenada sao inteiros e estao entre 1 e 4
        return (l, c)
    else:
        raise ValueError ('cria_coordenada: argumentos invalidos')

def coordenada_linha(coord):
    """
    Recebe uma coordenada e devolve a linha que lhe corresponde. 
    """    
    return coord[0]

def coordenada_coluna(coord):
    """
    Recebe uma coordenada e devolve a coluna que lhe corresponde.
    """    
    return coord[1]

def e_coordenada(arg):
    """
    Recebe um argumento universal e verifica se e uma coordenada ou nao.  Devolve um valor logico (True ou False)
    """     
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int) and (arg[0] in (1, 2, 3, 4)) and isinstance(arg[1], int) and (arg[1] in (1, 2, 3, 4)) #Verifica se a coordenada e um tuplo, e se os seus elementos sao  inteiros e se estao entre 1 e 4

def coordenadas_iguais(coord1, coord2):
    """
    Recebe duas coordenadas e verifica se sao iguais. Devolve um valor logico(True ou False)
    """    
    return (coordenada_linha(coord1) == coordenada_linha(coord2)) and (coordenada_coluna(coord1) == coordenada_coluna(coord2))

#==========================TAD Tabuleiro=======================================#

def cria_tabuleiro():
    """
    Cria um tabuleiro, com a pontuacao e todas as posicoes a zero. Nao tem input e devolve o tabuleiro criado.
    """    
    return [0, [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        
def tabuleiro_posicao(t, coord):
    """
    Recebe um tabuleiro e uma coordenada e devolve o valor na posicao do tabuleiro correspondente a coordenada.
    """    
    if e_coordenada(coord):
        return t[coordenada_linha(coord)][coordenada_coluna(coord)-1] #-1 devido ao indice da lista comecar no 0
    else:
        raise ValueError('tabuleiro_posicao: argumentos invalidos')
    
def tabuleiro_pontuacao(t):
    """
    Recebe um tabuleiro e devolve a pontuacao do mesmo.
    """    
    return t[0]

def tabuleiro_posicoes_vazias(t):
    """
    Recebe um tabuleiro e devolve uma lista com as coordenadas de todas as posicoes vazias do tabuleiro.
    """    
    lista = []
    for l in range(1, 5): 
        for c in range(1, 5):  
            if tabuleiro_posicao(t, cria_coordenada(l, c)) == 0:
                lista = lista+[cria_coordenada(l, c)]
    return lista

def tabuleiro_preenche_posicao(t, coord, v):
    """
    Recebe uma posicao, uma coordenada e um inteiro e devolve o tabuleiro com o valor do inteiro na coordenada recebida.
    """    
    if e_coordenada(coord) and isinstance(v, int):
        t[coordenada_linha(coord)][coordenada_coluna(coord)-1] = v #-1 devido ao indice da lista comecar no 0
        return t
    else:
        raise ValueError('tabuleiro_preenche_posicao: argumentos invalidos')
    
def tabuleiro_actualiza_pontuacao(t, v):
    """
    Recebe um tabuleiro e um valor v, soma este valor a sua pontuacao e devolve o tabuleiro actualizado.
    """    
    if isinstance(v, int) and (v%4 == 0) and (v >= 0):  
        t[0] = t[0] + v   
        return t    
    else:
        raise ValueError('tabuleiro_actualiza_pontuacao: argumentos invalidos')

import random
def tabuleiro_reduz(t, direccao):
    """
    Recebe um tabuleiro e uma direcao e reduz o tabuleiro conforme essa direcao, devolvendo o tabuleiro resultante.
    """
    tupcads=('N' , 'S', 'E', 'W')   #tupcads=tuplo de cadeias de caracteres de input possiveis
    if direccao in tupcads:#Verifica se a direccao recebida e valida
            tuplorange=(range(1, 5), range(3, 0, -1), range(2, 5) ) #tuplorange = tuplo de ranges possiveis
            #Este conjunto de condicoes atribui valores a variaveis que mudam a direccao das funcoes soma e empurra, consoante a direcao escolhida
            #varlinhas corresponde a linha da coordenada que se vai comparar, consoante a direcao escolhida
            #varcolunas corresponde a coluna da coordenada que se vai comparar, consoante a direcao escolhida            
            if direccao == 'N':        
                varlinhas = -1 
                varcolunas = 0
                rangelinhas = tuplorange[2]             
                rangecolunas = tuplorange[0]
            elif direccao == 'S':
                varlinhas = 1
                varcolunas = 0
                rangelinhas = tuplorange[1]             
                rangecolunas = tuplorange[0]
            elif direccao == 'W':
                varlinhas = 0
                varcolunas = -1
                rangelinhas = tuplorange[0]             
                rangecolunas = tuplorange[2]            
            else:     # direccao == 'E'
                varlinhas = 0
                varcolunas = 1
                rangelinhas = tuplorange[0]             
                rangecolunas = tuplorange[1]            
            def empurra(t):
                """
                Recebe um tabuleiro e empurra os seus elementos para uma determinada direcao.
                """
                for x in range(1, 4):  #Faz o ciclo 3 vezes
                    for l in rangelinhas:
                        for c in rangecolunas:
                            if tabuleiro_posicao(t, cria_coordenada(l+varlinhas, c+varcolunas)) == 0:  #Ve se a coordenada seguinte tem valor zero
                                tabuleiro_preenche_posicao(t, cria_coordenada(l+varlinhas, c+varcolunas), tabuleiro_posicao(t, cria_coordenada(l, c))) #Se tiver, preenche com o valor da cordenada anterior
                                tabuleiro_preenche_posicao(t, cria_coordenada(l, c), 0) #E preenche o seu valor com zero
            def soma(t):
                """
                Recebe um tabuleiro e soma os seus elementos que forem possiveis somar, de acordo com as regras do jogo.
                """
                for l in rangelinhas:
                    for c in rangecolunas:
                        if tabuleiro_posicao(t, cria_coordenada(l+varlinhas, c+varcolunas)) == tabuleiro_posicao(t, cria_coordenada(l, c)):  #Ve se a coordenada asseguir tem o mesmo valor que a coordenada anteriror
                            tabuleiro_preenche_posicao(t, cria_coordenada(l+varlinhas, c+varcolunas), 2*tabuleiro_posicao(t, cria_coordenada(l+varlinhas, c+varcolunas))) #Se tiver soma os dois valores.
                            tabuleiro_preenche_posicao(t, cria_coordenada(l, c), 0) #Preenche a coordenada anterior com o valor zero
                            t=tabuleiro_actualiza_pontuacao(t, tabuleiro_posicao(t, cria_coordenada(l+varlinhas, c+varcolunas))) #Actualiza a pontucao do tabuleiro
                            
            empurra(t)  
            soma(t)      
            empurra(t)   
            return t
    else:   
        raise ValueError('tabuleiro_reduz: argumentos invalidos')

def e_tabuleiro(arg):
    """
    Recebe um argumento universal e verifica se este e um tabuleiro. Devolve um valor logico (True ou False)
    """
    if (not isinstance(arg,list)) or len(arg)!=5 or (not isinstance(arg[0],int)): #verifica se t e uma lista, se tem 5 elementos e se o valor da pontuacao e inteiro
        return False    
    for i in range(1,5):  
        if len (arg[i])!=4 or (not isinstance(arg[i],list)): #verifica se a lista tem 4 listas internas, com os indices todos inteiros
            return False
    return True

def tabuleiro_terminado(t):
    """
    Recebe um tabuleiro e verifica se ainda existem jogadas possiveis.  Devolve um valor logico (True ou False).
    """
    t_copiado = copia_tabuleiro(t)      #Se o tabuleiro for igual ao mesmo tabuleiro reduzido para todas as direcoes e porque ja nao e possivel fazer mais jogadas.
    return tabuleiro_posicoes_vazias(t) == [] and tabuleiros_iguais(t, tabuleiro_reduz(t_copiado, 'N')) and tabuleiros_iguais(t, tabuleiro_reduz(t_copiado, 'S')) and tabuleiros_iguais(t, tabuleiro_reduz(t_copiado, 'W')) and tabuleiros_iguais(t,tabuleiro_reduz(t_copiado, 'E'))

def tabuleiros_iguais(t1,t2):
    """
    Recebe dois tabuleiros e verfica se sao iguais, devolvendo um valor logico (True ou False).
    """
    return t1 == t2

def escreve_tabuleiro(t):
    """
    Recebe um tabuleiro e escreve este na forma de um tabuleiro de jogo de 2048.
    """
    if e_tabuleiro(t):  
        for l in range(1,5):
            strlinha=""
            for c in range(1,5):
                strlinha=strlinha+"[ "+str(tabuleiro_posicao(t,cria_coordenada(l,c)))+" ]"+" "#Adiciona os 4 elementos (1 a 4) da linha a string a escrever
            print (strlinha) #Escreve a string correspondente a linha (1 a 4)
        print ('Pontuacao:', tabuleiro_pontuacao(t))  #Escreve a pontuacao
    else:
        raise ValueError ('escreve_tabuleiro: argumentos invalidos')
    
#================================Funcoes Avancadas=============================#

def pede_jogada():
    """
    Pede uma jogada ao utilizador e devolve essa jogada, se ela for valida
    """
    i = 1
    while i == 1:   #Criamos u ciclo infinito para so parar quando a jogado introduzida for uma direcao possivel
        j = input('Introduza uma jogada (N, S, E, W): ')
        if j in ('N', 'S', 'E', 'W'):
            return j
        else:
            print ('Jogada invalida.')
            
def jogo_2048():
    """
    E a funcao responsavel pelo correr do jogo (nao tem input nem output)
    """
    t = cria_tabuleiro() 
    preeenche_posicao_aleatoria(t)
    preeenche_posicao_aleatoria(t)  #O jogo do 2048 original comeca com 2 casas ja preenchidas
    escreve_tabuleiro(t)           
    x = 0
    while x != 1:                       # Criamos um ciclo infinito de preposito para so parar quando o tabuleiro tiver terminado
        t_copiado = copia_tabuleiro(t)
        direccao = pede_jogada()        
        tabuleiro_reduz(t, direccao)    #Se possivel reduz o tabuleiro na direcao pedida
        if not tabuleiros_iguais(t,t_copiado):              #Se ainda for possivel continuar a jogar
            preeenche_posicao_aleatoria(t)  #Preenche outra posicao aleatoria
        escreve_tabuleiro(t)           
        if tabuleiro_terminado(t):   #Se o tabuleiro tiver terminado a funcao para e o jogo tambem
            break
        
#================================Funcoes Sugeridas=============================#
def preeenche_posicao_aleatoria(t):
    """
    Recebe um tabuleiro, preenche uma posicao aleatoria, como valor de 2 ou 4, escolhido aleatoriamente conforme as probabilidades e devolve o tabuleiro resultante.
    """
    coord_aleatoria=tabuleiro_posicoes_vazias(t)[int(random.random()*(len(tabuleiro_posicoes_vazias(t))-1))] # escolhe uma posicao vazia aleatoria 
    if random.random()<0.8: # a probabilidade de ser 2 e de 80%
        rand=2
    else:
        rand=4    # a probabilidade de ser 4 e de 20%
    tabuleiro_preenche_posicao(t,coord_aleatoria,rand)

def copia_tabuleiro(t):
    """
    Recebe um tabuleiro e copia este posicao a posicao, devolvendo um tabuleiro igual ao primeiro.
    """    
    t_copiado=[]
    for l in range(1,5):
        for c in range(1, 5):
            t_copiado = t_copiado + [tabuleiro_posicao(t, cria_coordenada(l,c))] #copia os elementos do tabuleiro 1 a 1  para uma so lista  
    return [tabuleiro_pontuacao(t), t_copiado[0:4], t_copiado[4:8], t_copiado[8:12], t_copiado[12:16]] #organiza os elementos copiados de acordo com a representacao escolhida