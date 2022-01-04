import numpy as np
import pandas as pd

class Corse():

    durata=list()
    inizio=list()
    zona=list()
    nomi_zone=list()

    def __init__(self, percentuale, differenza, inizio_corsa, zone, zone_df):
        self.percentuale = percentuale
        self.differenza = differenza
        self.inizio_corsa = inizio_corsa
        self.zone = zone
        self.zone_df=zone_df


    def durata_corsa(self, upper_lower):
        i=0
        while i<len(self.differenza):
            if upper_lower == 'upper':
                if self.differenza[i] >= self.percentuale:
                    self.inizio.append(self.inizio_corsa[i])
                    self.durata.append(self.differenza[i])
                    self.zona.append(self.zone[i])
                    self.nome_zona=self.zone_df.loc[self.zone[i]]['Zone']
                    self.nomi_zone.append(self.nome_zona)
                    i = i + 1
            
                else: 
                    i= i + 1

            elif upper_lower == 'lower':
                 while i<len(self.differenza):
                    if self.differenza[i] <= self.percentuale:
                        self.inizio.append(self.inizio_corsa[i])
                        self.durata.append(self.differenza[i])
                        self.zona.append(self.zone[i])
                        self.nome_zona=self.zone_df.loc[self.zone[i]]['Zone']
                        self.nomi_zone.append(self.nome_zona)
                        i = i + 1
                
                    else: 
                        i= i + 1

        data = {   
                'id_zona': self.zona,
                'nome_zona':self.nomi_zone,
                'inizio': self.inizio,
                'durata': self.durata,
                }          
        
        return data




