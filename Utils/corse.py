class Corse():



    def __init__(self, percentuale, differenza, inizio_corsa, zone, zone_df):
        self.percentuale = percentuale
        self.differenza = differenza
        self.inizio_corsa = inizio_corsa
        self.zone = zone
        self.zone_df=zone_df


    def durata_corsa(self, upper_lower):
        
        durata=list()
        inizio=list()
        zona=list()
        nomi_zone=list()
        i=0
        while i<len(self.differenza):
                if upper_lower == 'lower':
                    
                    if self.differenza[i] <= self.percentuale :
                        inizio.append(self.inizio_corsa[i])
                        durata.append(self.differenza[i])
                        zona.append(self.zone[i])
                        self.nome_zona=self.zone_df.loc[self.zone[i]]['Zone']
                        nomi_zone.append(self.nome_zona)
                        i = i + 1
                
                    else: 
                        i= i + 1
                elif upper_lower == 'upper':
                    if self.differenza[i] >= self.percentuale :
                        inizio.append(self.inizio_corsa[i])
                        durata.append(self.differenza[i])
                        zona.append(self.zone[i])
                        self.nome_zona=self.zone_df.loc[self.zone[i]]['Zone']
                        nomi_zone.append(self.nome_zona)
                        i = i + 1
                
                    else: 
                        i= i + 1
                    
        data = {   
                'id_zona': zona,
                'nome_zona':nomi_zone,
                'inizio': inizio,
                'durata': durata,
                }  
        
        return data

