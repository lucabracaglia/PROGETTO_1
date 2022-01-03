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
#import Utils


'''
parser = Utils.initialize_parser()
'''


"""Leggo tutto il file in ingresso attraverso un path relativo:"""



taxi_df=pd.read_csv('Data/yellow_tripdata_2020-03.csv');
zone_df=pd.read_csv('Data/taxi+_zone_lookup.csv');
#zone_df=pd.read_csv('Data/taxi+_zone_lookup.csv', index_col="LocationID");

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
zone= taxi_df['PULocationID']


'''prima implementazione dell' algoritmo per calcolare la durata di un viaggio'''
date_format = "%Y-%m-%d %H:%M:%S"

conteggio=list()

try:
    i=0
    while i<len(inizio_corsa):
        a = datetime.strptime(inizio_corsa[i], date_format)
        b = datetime.strptime(fine_corsa[i], date_format)
        delta = b - a
        delta = delta.total_seconds()
        conteggio.append(delta)
        i = i + 1
        
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
calcolata la durata di ogni viaggio (conteggio), le inserisco in una series in modo da calcolarne la media e, in seguito creare un dataframe
con tutte le corse che durano più della media.
 '''
differenza = pd.Series(conteggio)
media = differenza.mean()
superiori=list()
inizio=list()
zona=list()
nome_zona=list()



'''
Vorrei associare all' id di una zona il corrispettivo nome sfruttando il legamen in zone_df
 z= zone_df.loc[zone_df['LocationID'] == zona[i]]
 nome = z['Zone']
 nome_zona.append(nome)'''

i=0
while i<len(differenza):
    if differenza[i] > media:
        inizio.append(inizio_corsa[i])
        superiori.append(differenza[i])
        zona.append(zone[i])
        i = i + 1
        

    else: 
        i= i+1
 
        
data = {
            'id_zona': zona,
            #'nome_zona':nome_zona,
            'inizio': inizio,
            'durata': superiori,
        }        

'''il dataframe Corse lunghe contiene l'id zona, l'inizio della corsa e la durata del un viaggio'''

Corse_lunghe = pd.DataFrame(data)

Corse_lunghe.to_csv('Output/Corse_lunghe.csv')




         
    


