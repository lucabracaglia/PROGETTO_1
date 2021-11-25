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

"""Leggo tutto il file in ingresso attraverso un path relativo:"""

taxi_df=pd.read_csv('./Data/yellow_tripdata_2020-03.csv');

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
df = taxi_df.head(20)


"""Rinomino le colonne del dataframe"""
df.rename(columns={
'tpep_pickup_datetime': 'inizio_corsa',
'tpep_dropoff_datetime': 'fine_corsa',}, inplace=True)

