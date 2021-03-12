import csv
from numpy import arange
import numpy as np
import pandas as pd

inter=[]
base= []
dados=[]
with open('/media/aureziano/HD2/auxilio/inter_1.csv') as arquivo_csv:
    leitor = pd.read_csv(arquivo_csv, delimiter=',',dtype=str,usecols=[1,2],names=["NOME","cpf"])
    y = pd.DataFrame(leitor)

ARQUIVO = open(r'/home/aureziano/Documentos/Auxilio/inter_val.csv', "w")
with open('/media/aureziano/HD2/auxilio/ativos.csv') as arquivo_csv:
    for chunk in pd.read_csv(arquivo_csv,chunksize=10000 , usecols=[0,1],delimiter=',',dtype=str):
        # print(chunk['beneficiario'])
        # dados.append(chunk['beneficiario'])
        print(chunk.index)
        # if chunk.index.isnull:
        x = []
        try:
            x = pd.Series(chunk['NOME'])
        except KeyError:
            print(chunk.beneficiario) 

        # x = pd.Series(chunk)
        
        xy = pd.DataFrame(chunk, columns=['NOME','cpf'])
        print(xy['cpf'])
        # print("xy: " + xy['beneficiario'])
        filter = xy[xy['NOME'].isin(y['NOME'])]
        print(filter)
        #salvando dados em Csv
        filter.to_csv(ARQUIVO)

ARQUIVO.close()        


        