# 81633_Joao Henriques

from random import random

##Trabalho 1

def calc_soma(cad_num):
    """
    Recebe uma cadeira de carateres, que corresponde ao numero do cartao, sem o numero de verificaco (ultimo numero).
    """
    N_Inv = ''
    for i in range(len(cad_num)):
        N_Inv = cad_num[i] + N_Inv       # Numero invertido  
      
    N_Inv_Dup = ''
    
    for i in range(len(N_Inv)):   # Mutiplica as posicoes impares do numero invertido
        dig = N_Inv[i]
        if i%2 == 0:   # Posicoes impares = indices pares
            dig = eval(dig)
            dig = dig*2
            if dig > 9:
                dig = dig-9
            dig = str (dig)
        N_Inv_Dup = N_Inv_Dup + dig       # Numero invertido ja mutiplicado
    N_Som = 0    
   
    for i in range(len(N_Inv_Dup)):
        N_Som = N_Som + eval(N_Inv_Dup[i])     
    return N_Som          # Soma dos digitos de acordo com o algoritmo de luhn


def luhn_verifica (cad_ver):
    """
    Recebe uma cadeia de carateres, que representa um numero de cartao e devolve "True" se passar o algoritmo de Luhn. E "False" se nao passar.
    """
    dig_ver = eval(cad_ver[len(cad_ver)-1])
    N3 = cad_ver[:len(cad_ver)-1]
    return (calc_soma(N3) + dig_ver) % 10 == 0


def comeca_por (cad1 , cad2):
    """
  Recebe duas cadeiras de carateres, cad1 e cad2, respetivamente. 
  A funcao devolve "True"  se cad1 comecar por cad2.E "False" em caso contrario.
    """ 
    return cad2 == cad1[:len(cad2)] :


def comeca_por_um (cad , t_cads):
    """
    Recebe uma cadeira de carateres, cad, e um tuplo de cadeiras de carateres t_cads.
    Devolve "True" apenas se cad comecar por um dos elementos do tuplo t_cads. Devolve "False" em caso contrario.
    """   
    for i in range(len(t_cads)):
        if comeca_por (cad, t_cads[i]):
            return True
    return False
        

def valida_iin (cad_cc): 
    """
    Recebe uma cadeira de carateres correspondente ao numero do cartao.
    Devolve a rede emissora do cartao (em cadeia de carateres), se exisitir. 
    Se nao existir devolve uma cadeia de carateres vaiza.
    """   
    if (comeca_por_um (cad_cc , ('34' , '37')) and (len(cad_cc) == 15)): # AE
        return 'American Express'  
    elif (comeca_por_um (cad_cc , ('309' , '36' , '38' , '39')) and (len(cad_cc) == 14)): # DCI
        return 'Diners Club International'
    elif (comeca_por_um (cad_cc , ('65', )) and (len(cad_cc) == 16)): # DC
        return 'Discover Card'
    elif (comeca_por_um (cad_cc , ('5018' , '5020' , '5038')) and (len(cad_cc) in (13,19))): # M
        return 'Maestro'
    elif (comeca_por_um (cad_cc , ('50' ,'51','52','53','54' , '19')) and (len(cad_cc) == 16)): # MC
        return 'Master Card'
    elif (comeca_por_um (cad_cc , ('4026' , '426' , '4405' , '4508')) and (len(cad_cc) == 16)): # VE
        return 'Visa Electron'
    elif (comeca_por_um (cad_cc , ('4024' , '4532' , '4556')) and (len(cad_cc) in (13,16))): # V
        return 'Visa'
    else:
        return ''
 
    
def categoria (cad): # primeiro dig do numero de cartao de credito == MII , define a entidade do cartao de credito
    """
    Recebe uma cadeia de carateres e devolve a entidade do seu cartao de credito (em cadeia de carateres).
    """
    if '1' == cad[0]:
        return 'Companhias aereas'
    elif '2' == cad[0]:
        return 'Companhias aereas e outras tarefas futuras da industria'
    elif '3' == cad[0] :
        return 'Viagens e entretenimento e bancario / financeiro'
    elif '4' == cad[0]:
        return 'Servicos bancarios e financeiros'
    elif '5' == cad[0]:
            return 'Servicos bancarios e financeiros'    
    elif '6' == cad[0]:
        return 'Merchandising e bancario / financeiro'
    elif '7' == cad[0]:
        return 'Petroleo e outras atribuicoes futuras da industria'
    elif '8' == cad[0]:
        return 'Saude, telecomunicacoes e outras atribuicoes futuras da industria'
    elif '9' == cad[0]:
        return 'Atribuicao nacional'
    else:
        return False


def verifica_cc (numcc):   
        """
        recebe um numero correspondete a um cartao de credito. E verfifica se este numero e correto, se for devolve, em cadeia de carateres, a categoria e a rede emissora. Se nao for devolve cartao invalido (em cadeia de carateres).
        """
        numcc = str (numcc)
        
        if luhn_verifica (numcc):
            if valida_iin (numcc) != '':
                return (categoria(numcc), valida_iin(numcc))
        return 'cartao invalido'


##Trabalho 2   
def numeros_random (int_dig):
    """
    Recebe um numero inteiro, que corresponde a quantidade de numeros inteiros random (de 0 a 9) que queremos.
    """
    num_random = ''
    while len(num_random) < int_dig:
        num_random = num_random + str(int(random() * 10))
    return num_random
        
    
def digito_verificacao (num):
    """
    Introduza uma cadeia de carateres que representa um numero de carateres sem o digito de verificacao. 
    A funcao indica o digito de verificacao necessario para o cartao ser valido.
    """
    ult_num = ''
    soma = calc_soma (num)
    
    if soma % 10 == 0:
        ult_num = ult_num + '0'
        return ult_num
    
    else:
        dig = soma % 10
        ult_num = 10 - dig
    return str(ult_num)


t_redes = (('AE' , ('34' , '37') , 15) , 
           ('DCI' , ('309', '36', '38' , '39') , 14) , 
           ('DC' , ('65'), 16) , 
           ('M' , ('5018', '5020', '5038') , (13 , 19)) , 
           ('MC' , ('50' , '51' , '52' , '53' , '54' , '19'), 16) , 
           ('VE' , ('4026', '426', '4405', '4508') , 16) , 
           ('V' , ('4024', '4532', '4556') , (13 , 16)))


def gera_num_cc (Abv):
    """
    Recebe uma cadeia de carates, correspondente a uma abreviatura de uma entidade emissora. E gera um numero valiado para essa entidade.
    """
    cad_IIN = ''
    num_dig = ''
    if Abv == 'AE' or Abv == 'DCI' or Abv == 'DC' or Abv == 'M' or Abv == 'MC' or Abv == 'VE' or Abv == 'V':    
        for tuplo in t_redes:
            if Abv == tuplo[0]:
                if Abv == 'DC':
                    cad_IIN = tuplo[1]
                    num_dig = tuplo[2]
                
                elif Abv == 'M' or Abv== 'V':
                    cad_IIN = tuplo[1][int(random() * 3)]
                    num_dig = tuplo[2][int(random() * 2)]
                  
                else:
                    cad_IIN = tuplo[1][int(random()*len(tuplo[1]))]
                    num_dig = tuplo[2]
        num_somado = cad_IIN + numeros_random(num_dig - 1 - len(cad_IIN))
        return eval( num_somado + digito_verificacao(num_somado))
    else:
        print('Introduza uma abreviatura correspondente a uma rede emissora')