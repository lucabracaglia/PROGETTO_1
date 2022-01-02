# -*- coding: utf-8 -*-
"""
Editor: Daniele

Esercizio Gruppo 3

Reserach questions:
   Quanto durano i viaggi? Mettiamo la nostra attenzione sulla durata dei viaggi.
   In quali zone si svolgono viaggi più lunghi? E invece più corti? 
   Fornire un file e un plot. Eseguite questa analisi per New York e per ogni borough. 

Input: anno, mese*, borough*
Output: file, grafico
 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime

"""
fase 1:
    -Leggere i dati (CSV) in ingresso (attualmente usiamo path relativo,
                                       dovremmmo dare la possibilita di
                                       far inserire all' utente il path)
    -Analizzare i dati a disposizione (df.info())
    - !! IL FILE OCCUPA IN MEMORIA 400+ Mb
    - Possibilmente rinominiamo i campi
    
"""
taxi_df = pd.read_csv('./Data/yellow_tripdata_2020-03.csv');

"""
Per soddisfare la prima richiesta:
    - va convertita la data in intero
    -va effettuata la differenza es: differenza = inizio_corsa[2]-inizio_corsa[1]
    -il risultato è in milli secondi quindi dobbimao moltiplicarlo per riportarlo 
    in ore/giorni 

"""
#inizio_corsa = taxi_df["tpep_pickup_datetime"].apply(lambda x: pd.Timestamp(x)).astype('int64')//10**9;
inizio_corsa = taxi_df["tpep_pickup_datetime"]
print(inizio_corsa)

plt.figure(figsize=(5,8))
plt.boxplot(inizio_corsa)
plt.show()