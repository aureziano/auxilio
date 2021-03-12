import csv
from numpy import arange
import numpy as np
import pandas as pd

inter=[]
base= []
dados=[]
with open('/media/aureziano/HD2/auxilio/ativos.csv') as arquivo_csv:
    leitor = np.genfromtxt(arquivo_csv, delimiter=',',dtype=str,usecols=[0])
    for row in leitor:
        np.char.upper(row)
        base.append(row)
y = pd.Series(sorted(base))
ARQUIVO = open(r'/home/aureziano/Documentos/Auxilio/inter.csv', "w")
with open('/media/aureziano/HD2/auxilio/dados.csv') as arquivo_csv:
    for chunk in pd.read_csv(arquivo_csv,chunksize=10000 , usecols=[5,6],delimiter=',',dtype=str):
        # print(chunk['beneficiario'])
        # dados.append(chunk['beneficiario'])
        print(chunk.index)
        # if chunk.index.isnull:
        x = []
        try:
            x = pd.Series(chunk['beneficiario'])
        except KeyError:
            print(chunk.beneficiario) 

        # x = pd.Series(chunk)
        # print(x)
        xy = pd.DataFrame(chunk, columns=['beneficiario','cpf_beneficiario'])
        # print("xy: " + xy['beneficiario'])
        filter = xy[xy['beneficiario'].isin(y)]
        #salvando dados em Csv
        filter.to_csv(ARQUIVO)
        # for i in filter:
        #     writer.writerow(i)
ARQUIVO.close()        

        