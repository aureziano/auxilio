# -*- coding: utf-8 -*-
import csv
from numpy import arange, fft, angle
import numpy as np
# import matplotlib.pyplot as plt


dado=[]
base=[]
inter=[]
inter_x=[]
teste=[]
#https://brasil.io/dataset/govbr/auxilio_emergencial/
with open('/media/aureziano/HD2/auxilio/dados.csv') as arquivo_csv:
    leitor = np.genfromtxt(arquivo_csv,delimiter=',',usecols=(4,5),dtype=str )
    # leitor = csv.DictReader(arquivo_csv, delimiter=',')
    #leitor.__next__()
    # for row in leitor:
    #     dado.append(row['cpf_beneficiario'])
        # dado.append((row['beneficiario'],row['cpf_beneficiario']))
        # dado.append(row['cpf_beneficiario'])
# teste = np.delete(dado,[1],1)
# print(leitor[:,1])
dado = leitor[:,1]

with open('/media/aureziano/HD2/auxilio/base.csv') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv, delimiter=',',usecols=(0),dtype=str)
    #leitor.__next__()
    # for row in leitor:
    #     base.append(row['beneficiario'])
base = leitor[:,0]
AMOSTRAS = len(dado) 
AMOSTRAS_base = len(base)              
# Definição de parametros
inter = set(base).intersection(set(dado))
for f in sorted(inter):
     inter_x.append(f)
AMOSTRAS_inter = len(inter_x)

#salvando dados em Csv
ARQUIVO = open('/home/aureziano/Documentos/Auxilio/inter.csv', "w")
writer = csv.writer(ARQUIVO, delimiter='\t',quotechar='"', quoting=csv.QUOTE_ALL)
for i in range (0,AMOSTRAS_inter):
  writer.writerow([inter_x[i]])
ARQUIVO.close()