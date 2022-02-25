import numpy as np
import pandas as pd
from Utils.corse import Corse
import utilities

# passo come parametri l' anno e il mese in cui voglio effettuare l' analisi 
args = utilities.initializeParser()

'''lettura dati'''
taxi_df = utilities.lettura_dati(args.year, args.month)
zone_df = pd.read_csv('Data/taxi_zone_lookup.csv', index_col="LocationID")

taxi_df=taxi_df.head(2000)

'''si creano due series diverse:
    - una per l' inizio delle corse
    - per la fine delle corse'''  
    
inizio_corsa= taxi_df['inizio_corsa']
fine_corsa= taxi_df['fine_corsa']
zone= taxi_df['PULocationID']

'''calcolo le durate di tutti i viaggi'''
conteggio=utilities.calcolo_durata(inizio_corsa, fine_corsa)

'''
calcolata la durata di ogni viaggio (conteggio), le inserisco in una series in modo da calcolarne la media e, in seguito creare un dataframe
con tutte le corse che durano più della media.
 '''
durata_corse = pd.Series(conteggio)
taxi_df['durata_corse']=durata_corse
media = durata_corse.mean()
upper_quartile=np.percentile(durata_corse, 75)
lower_quartile=np.percentile(durata_corse, 25)

'''istanza delle diverse corse'''
corsa_lunga = Corse(upper_quartile, durata_corse, inizio_corsa, zone, zone_df)
corsa_breve = Corse(lower_quartile, durata_corse, inizio_corsa, zone, zone_df)

'''crazione di due dizionari per la realizzazione di due dataframe'''
data_upper= corsa_lunga.durata_corsa('upper', args.borough)
data_lower= corsa_breve.durata_corsa('lower', args.borough)


'''il dataframe Corse lunghe contiene l'id zona, l'inizio della corsa e la durata del un viaggio'''
Corse_lunghe = pd.DataFrame(data_upper)

'''il dataframe Corse brevi contiene l'id zona, l'inizio della corsa e la durata del un viaggio'''
Corse_brevi = pd.DataFrame(data_lower)

'''plot'''
utilities.plot_corse(taxi_df, Corse_brevi, Corse_lunghe)


'''salvataggio dei dati'''

Corse_lunghe.to_csv('Output/Corse_lunghe.csv')
Corse_brevi.to_csv('Output/Corse_brevi.csv')

