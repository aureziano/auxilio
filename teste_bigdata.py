# -*- coding: utf-8 -*-
import csv
from numpy import arange
import numpy as np
import pandas as pd


dado=[]
base= []
inter=[]
inter_x=[]
teste=[]
#https://brasil.io/dataset/govbr/auxilio_emergencial/

with open('/media/aureziano/HD2/auxilio/ativos.csv') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv, delimiter=',')
    for row in leitor:
        base.append(row)
        pd.array(base)

# base = leitor[:,0]
print(len(base))
with open('/media/aureziano/HD2/auxilio/dados.csv') as arquivo_csv:
    for chunk in pd.read_csv(arquivo_csv,chunksize=10000 , usecols=[6],delimiter=',',dtype=str,header=None):
        for row in chunk:
            dado.append(row)
            pd.array(dado)
        # inter = set(base).intersection(set(chunk))
        inter = np.intersect1d(base,dado)
        for f in inter:
            inter_x.append(f)
        AMOSTRAS_inter = len(inter_x)

        #salvando dados em Csv
        ARQUIVO = open('/home/aureziano/Documentos/Auxilio/inter.csv', "w")
        writer = csv.writer(ARQUIVO, delimiter='\t',quotechar='"', quoting=csv.QUOTE_ALL)
        for i in range (0,AMOSTRAS_inter):
            writer.writerow([inter_x[i]])
        ARQUIVO.close()
        