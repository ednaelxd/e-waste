import pandas as pd
import numpy as np

###########################################################
# remoção do texto demasiadamente longo EN e PT-BR
###########################################################

def text_reducer(lista_de_colunas,language):
    # Lista contendo as colunas do dataframe
    if language == 'pt':
        cont = 2 
        for itens in lista_de_colunas[2:]:
            if '[' in itens[:-1]:
                #print(cont)
                init = itens.find(':')
                pos = itens.find('Esta estratégia')
                #print(itens[:init]+ ':' + ' '+ itens[pos:])
                lista_de_colunas.values[cont] = (itens[:init]+ ':' + ' '+ itens[pos:])
            cont+=1

    if language == 'en':     
        cont = 2 
        for itens in lista_de_colunas[2:]:
            if '[' in itens[:-1]:
                #print(cont)
                init = itens.find(':')
                pos = itens.find('This strategy')
                #print(itens[:init]+ ':' + ' '+ itens[pos:])
                lista_de_colunas.values[cont] = (itens[:init]+ ':' + ' '+ itens[pos:])
            cont+=1
###########################################################

def padroniza_nomeclatura(vetor_colunas):
    cont = 0
    num = 1 
    for itens in vetor_colunas[0:]:
        if '[' in itens[:-1]:
            #print(cont)
            init = itens.find('.')
            #print(itens[:init]+ ':' + ' '+ itens[pos:])
            vetor_colunas.values[cont] = ('M'+itens[0:init]+'.'+str(num))
            #print(num,cont)
            if ((cont-1)%10==0) & ((cont-1)!=0):
                num=1
                #print(num,cont)
            else:
                num+=1
        cont+=1
    return(vetor_colunas)

###########################################################
def organiza_localizacao(frase):
    separadores = ['-',',','.',';','--','_','/',' e ']
    for sep in separadores:
        if sep in frase:
            frase = frase.split(sep)
    cont=0
    for it in frase:
        for sep in separadores:
            if sep in it:
                frase[cont] = it.split(sep)
        cont+=1
    return frase

###########################################################
# ENCODERS-INIT
###########################################################

# A

def ordinal_encoder(termo):
    if termo == 'Muito baixo' or termo == 'Very low'  or termo=='Very Low' or termo == '1' or termo == 'Molto basso':
        termo = 1
    if termo == 'Baixo' or termo == 'Low' or termo == 'Basso':
        termo = 2
    if termo == 'Neutro' or termo == 'Neutral' or termo=='Medium':
        termo = 3
    if termo == 'Alto' or termo == 'High':
        termo = 4
    if termo == 'Muito alto' or termo == 'Very high' or termo == 'Molto alto':
        termo = 5
    if termo == 'Sim' or termo == 'Yes':
        termo = 1
    if termo == 'Não' or termo == 'No':
        termo = 0
    return(termo)

# B
def patternizer(x):
    x=str(x)
    if ('Grande' in x) or ('Big' in x) or ('Large' in x) or ('30000' in x) or ('grandi' in x) or ('Global company' in x):
        x='Grande'
    if ('Média' in x) or ('Medium' in x) or ('medie' in x):
        x='Média'
    if ('Pequena' in x) or ('Small' in x) or  ('piccole' in x):
        x='Pequena'
    if ('até 10' in x) or ('until  10' in x):
        x='Micro'
    if ('Individual' in x) or ('individuale' in x):
        x='Individual'
    if ('Não' in x) or ('não' in x) or ('No se aplica' in x) or ('no' in x) or ('Na' in x) or ('nan' in x) or (x=='0'):
        x='Sem empresa'
    if ('Universidade' in x) or ('universidade' in x) or ('Pesquisador' in x) or ('estudante' in x) or ('under education' in x) or ('Student' in x) or ('Reseacherl' in x) or ('student' in x) or ('University' in x) or ('students' in x):
        x='Acadêmico'
    return (x)

# C


###########################################################
# ENCODERS-END
###########################################################

