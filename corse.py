import numpy as np
import pandas as pd

class Corse():

    durata=list()
    inizio=list()
    zona=list()
    nomi_zone=list()

    def __init__(self, quartile, differenza, inizio_corsa , zone, zone_df):
        self.quartile = quartile
        self.differenza = differenza
        self.inizio_corsa = inizio_corsa
        self.zone = zone
        self.df=zone_df

    def durata_corsa(self):
        i=0
        while i<len(self.differenza):
            if self.differenza[i] < self.quartile:
                self.inizio.append(self.inizio_corsa[i])
                self.durata.append(self.differenza[i])
                self.zona.append(self.zone[i])
                self.nome_zona=self.zone_df.loc[self.zone[i]]['Zone']
                self.nomi_zone.append(self.nome_zona)
                i = i + 1
                
            else: 
                i= i+1

        data = {
                    'id_zona': self.zona,
                    'nome_zona':self.nomi_zone,
                    'inizio': self.inizio,
                    'durata': self.durata,
                    }          
        
        return data   



