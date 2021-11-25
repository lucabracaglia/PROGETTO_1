# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:25:43 2021

@author: Luca
"""
"""
progetto creato dal gruppo Bracaglia, Mercuri, Frisenda
leggi il file CSV ed effettua modifiche

"""
import pandas as pd
import numpy as np
import matplotlib as plt

#per allegerire il file abbiamo caricato da file csv solo le prime 20 colonne
taxi_df = pd.read_csv('./Data/yellow_tripdata_2021-05.csv')

taxi_df.info()


taxi_df.rename(columns={
        'tpep_pickup_datetime': 'Inizio_corsa', 
        'tpep_dropoff_datetime': 'Fine_corsa'}, inplace=True)

#aggiungere ai campi vuoti di payment type il valore di unknown

taxi_df['payment_type'].fillna(value='5.0', inplace = True)



