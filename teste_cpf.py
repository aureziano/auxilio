#Teste CPF
import csv
from numpy import arange
import numpy as np
import pandas as pd

inter=[]
base= []
dados=[]
y=[]
with open('/media/aureziano/HD2/auxilio/inter_val.csv') as arquivo_csv:
    # leitor = np.genfromtxt(arquivo_csv, delimiter=',',dtype=str,usecols=[2])
    leitor = pd.read_csv(arquivo_csv, usecols=[1,2],delimiter=',',dtype=str,names=['nome','cpf'])
    col_nome = pd.Series(leitor['nome'])
    y = pd.DataFrame(leitor)
    y['cpf'] = y['cpf'].str.slice(-8,-2)

ARQUIVO = open(r'/home/aureziano/Documentos/Auxilio/cpf_tratado.csv', "w")
with open('/media/aureziano/HD2/auxilio/ativos_1.csv') as arquivo_csv:
    # leitor = np.genfromtxt(arquivo_csv, delimiter=',',dtype=str,usecols=[1],names=['NOME'])
    row = pd.read_csv(arquivo_csv, usecols=[0,1],delimiter=',',dtype=str)
    x=[]
    col_nome = pd.Series(row['NOME'])
    col_cpf = pd.Series(row['cpf'])
    # x = [col_nome,col_cpf]
    x = pd.DataFrame(x)
    x['NOME']= col_nome
    x['cpf'] = col_cpf.str.slice(-8,-2)
    # xy = pd.DataFrame(x, columns=['NOME','cpf'])
    print("--------------------------------------------------------")
    # print(x)
    filter = x[x['cpf'].isin(y['cpf'])]
    filter1 = x[x['NOME'].isin(y['nome'])]
    x = filter & filter1
    print(x)
    # #salvando dados em Csv
    filter.to_csv(ARQUIVO)

ARQUIVO.close()        

        