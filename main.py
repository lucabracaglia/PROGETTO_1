import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime
from Utils.corse import Corse


'''
parser = Utils.initialize_parser()
'''


"""Leggo tutto il file in ingresso attraverso un path relativo:"""



taxi_df=pd.read_csv('Data/yellow_tripdata_2020-03.csv');
#zone_df=pd.read_csv('Data/taxi+_zone_lookup.csv');
zone_df=pd.read_csv('Data/taxi+_zone_lookup.csv', index_col="LocationID");

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
   
except:
    print('Rilevati problemi con formattazione dati inserite (dd/mm/aaa)')


'''
calcolata la durata di ogni viaggio (conteggio), le inserisco in una series in modo da calcolarne la media e, in seguito creare un dataframe
con tutte le corse che durano più della media.
 '''
durata_corse = pd.Series(conteggio)
media = durata_corse.mean()
upper_quartile=np.percentile(durata_corse, 75)
lower_quartile=np.percentile(durata_corse, 25)

'''istanza delle diverse corse'''
corsa_media = Corse(media, durata_corse, inizio_corsa, zone, zone_df)
corsa_lunga = Corse(upper_quartile, durata_corse, inizio_corsa, zone, zone_df)
corsa_breve = Corse(lower_quartile, durata_corse, inizio_corsa, zone, zone_df)

'''crazione di due dizionari per la realizzazione di due dataframe'''
data_upper= corsa_lunga.durata_corsa('upper')
data_lower= corsa_breve.durata_corsa('lower')


'''il dataframe Corse lunghe contiene l'id zona, l'inizio della corsa e la durata del un viaggio'''

Corse_lunghe = pd.DataFrame(data_upper)

'''il dataframe Corse brevi contiene l'id zona, l'inizio della corsa e la durata del un viaggio'''

Corse_brevi = pd.DataFrame(data_lower)

'''il codice successivvo è qualora l analisi si volesse svolgere dalla media invece che dai quartili superiroe ed inf'''
#data_mediaup= corsa_media.durata_corsa('upper')
#data_medialow= corsa_media.durata_corsa('lower')
#Corse_medieu = pd.DataFrame(data_mediaup)
#Corse_mediel = pd.DataFrame(data_medialow)



'''salvataggio dei dati'''

Corse_lunghe.to_csv('Output/Corse_lunghe.csv')
Corse_brevi.to_csv('Output/Corse_brevi.csv')