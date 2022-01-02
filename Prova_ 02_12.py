# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:23:51 2021

@author: Daniele
"""

"""
Progetto Daniele Mercuri - luca Bracaglia - Alessandro Frisenda

Legge i CSV di un file esterno e ne effettua alcune modifiche
"""

import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime

"""Leggo tutto il file in ingresso attraverso un path relativo:"""

taxi_df=pd.read_csv('./yellow_tripdata_2020-03.csv');

"""verifico l'esistenza dei duplicato, la variabile è vuota se non esistono duplicati"""
temp_df= taxi_df.drop_duplicates(inplace= True, keep = False)

"""verifico l' esistenza di campi nulli, !DEVO DECIDERE SE ELIMINARLI O SOSTITUIRE IL VALORE MANCANTE:"""

campi_vuoti= taxi_df.isnull().sum()
TX=taxi_df.dropna()
campi_vuoti1= TX.isnull().sum()
taxi_df['VendorID'].fillna('1.0' , inplace= True)
campi_vuoti2=taxi_df.isnull().sum()

"""chiudo la variabile con tutti i record per liberare spazio in memoria e riapro il file prendendo 
solo le prime 20 righe"""
taxi_df = taxi_df.head(20)


"""Rinomino le colonne del dataframe"""
taxi_df.rename(columns={
'tpep_pickup_datetime': 'inizio_corsa',
'tpep_dropoff_datetime': 'fine_corsa',}, inplace=True)

'''si creano due series diverse:
    - una per l' inizio delle corse
    - per la fine delle corse'''
    

inizio_corsa= taxi_df['inizio_corsa']
fine_corsa= taxi_df['fine_corsa']


'''prima implementazione dell' algoritmo per calcolare la durata di un viaggio'''
date_format = "%Y-%m-%d %H:%M:%S"
differenza = pd.Series()
conteggio=list()

try:
    i=0
    while i<len(inizio_corsa):
        a = datetime.strptime(inizio_corsa[i], date_format)
        b = datetime.strptime(fine_corsa[i], date_format)
        delta = b - a
        delta = delta.total_seconds()
        conteggio.append(delta)
        print(a,b,delta)
        i = i+1
        
        '''if b < a:
            delta = b - a
            conteggio=conteggio.append(delta)
            print(conteggio)
            continue
        else:
            print ('La differenza tra le due date è di giorni.')
            continue'''
        
    
except:
    print('Rilevati problemi con formattazione dati inserite (dd/mm/aaa)')


'''
date_format = "%d/%m/%Y"
ask_a = input('Inserisci prima data (dd/mm/aaaa) o premi Enter per oggi:\n')
if not ask_a:
   ask_a = datetime.now().strftime(date_format)
   print ("\033[FOggi:",ask_a)
ask_b = input('Inserisci seconda data (dd/mm/aaaa):\n')
try:
    a = datetime.strptime(ask_a, date_format)
    b = datetime.strptime(ask_b, date_format)
    if a > b:
        delta = a - b
    else:
        delta = b - a
    print ('La differenza tra le due date è di',delta.days,'giorni.')
except:
    print('Rilevati problemi con formattazione dati inserite (dd/mm/aaa)')'''
