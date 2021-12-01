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

#per allegerire il file abbiamo caricato da file csv solamente le series utili al progetto
taxi_df = pd.read_csv('./Data/yellow_tripdata_2021-05.csv',usecols=['tpep_pickup_datetime','tpep_dropoff_datetime', 'trip_distance', 'PULocationID', 'DOLocationID'])

zone_df = pd.read_csv('./Data/taxi_zone_lookup.csv')

taxi_df.rename(columns={
        'tpep_pickup_datetime': 'Inizio_corsa', 
        'tpep_dropoff_datetime': 'Fine_corsa'}, inplace=True)

taxi_df["Inizio_corsa"].apply(lambda x: pd.Timestamp(x)).astype('int64') // 10**9
taxi_df["Fine_corsa"].apply(lambda x: pd.Timestamp(x)).astype('int64') // 10**9

#nel caso in cui una distanza sia nulla riempio con la media delle distanze presente nel file 
distance = taxi_df['trip_distance']
distance_mean=distance.mean()
taxi_df.fillna(distance_mean, inplace=True)





