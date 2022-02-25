import argparse
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def initializeParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", '--year',
                        help="anno in cui si vuole effettuare l'analisi",
                        type=str,
                        default='2020')
    parser.add_argument("-m", "--month",
                        help="mese in cui si vuole svolgere l'analisi",
                        type=str,
                        default='03'
                        )
    parser.add_argument("-b", "--borough",
                        help="la zona di cui si vogliono analizzare i viaggi dei taxi",
                        type=str,
                        default = None)
    return parser.parse_args()
 

def lettura_dati(anno, mese):
     df=pd.read_csv('Data/yellow_tripdata_'+ str(anno)+'-'+ str(mese)+'.csv', usecols=['tpep_pickup_datetime','tpep_dropoff_datetime','PULocationID'])   
     df.rename(columns={
        'tpep_pickup_datetime': 'inizio_corsa',
        'tpep_dropoff_datetime': 'fine_corsa',}, inplace=True)
     
     return df

'''funzione che permette di realizzare una lista contenente la durata di ogni corsa'''
def calcolo_durata(inizio_corsa, fine_corsa):
     date_format = "%Y-%m-%d %H:%M:%S"
     conteggio=[]
     i=0
     while i<len(inizio_corsa):
        a = datetime.strptime(inizio_corsa[i], date_format)
        b = datetime.strptime(fine_corsa[i], date_format)
        delta = b - a
        delta = delta.total_seconds()
        conteggio.append(delta)
        i = i + 1

     return conteggio

'''funzione che permette di realizzare il plot dei diversi dataframe contenenti la durata delle corse'''
def plot_corse(taxi_df, Corse_brevi, Corse_lunghe):
    data1=taxi_df['durata_corse']
    data2=Corse_brevi['durata']
    data3=Corse_lunghe['durata']
    data=[data1,data2,data3]
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_axes([0, 0, 1, 1])
    bp = ax.boxplot(data)
    ax.set_ylim(0,3500)
    plt.xlabel('Divisione corse per durata')
    plt.ylabel('Durata delle corse')
    plt.title('Rappresentazione delle corse per la loro durata')
    a=ax.get_xticks().tolist()
    a[0]='Corse'
    a[1]='Corse_brevi'
    a[2]='Corse_lunghe'
    ax.set_xticklabels(a)
    plt.savefig('./Output/GraficoTaxi', bbox_inches='tight', dpi=150)
    plt.show()

