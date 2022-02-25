import sys
class Corse():



    def __init__(self, percentuale, differenza, inizio_corsa, zone, zone_df):
        self.percentuale = percentuale
        self.differenza = differenza
        self.inizio_corsa = inizio_corsa
        self.zone = zone
        self.zone_df=zone_df


    def durata_corsa(self, upper_lower, borough):
        
        durata=list()
        inizio=list()
        zona=list()
        nomi_zone=list()
        borough_lista=list()
        i=0
        '''se il borough non viene specificato si fa un analisi sulle corse in tutte le zone di New York'''
        if borough == None:
            while i<len(self.differenza):
                if upper_lower == 'lower':
                    
                    if self.differenza[i] <= self.percentuale :
                        inizio.append(self.inizio_corsa[i])
                        durata.append(self.differenza[i])
                        zona.append(self.zone[i])
                        self.nome_zona=self.zone_df.loc[self.zone[i]]['Zone']
                        nomi_zone.append(self.nome_zona)
                        borough_zona=self.zone_df.loc[self.zone[i]]['Borough']
                        borough_lista.append(borough_zona)
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
                        borough_zona=self.zone_df.loc[self.zone[i]]['Borough']
                        borough_lista.append(borough_zona)
                        i = i + 1
                
                    else: 
                        i= i + 1
                else:
                    print('Va specificato upper/lower')
                    sys.exit()
                    
            data = {   
                    'id_zona': zona,
                    'nome_zona':nomi_zone,
                    'inizio': inizio,
                    'durata': durata,
                    'borough':borough_lista
                    }
            
            '''altrimenti se il borough viene specificato elaboriamo le informazioni solo se la zona d'interesse appartiene al Borough specificato '''
        else:
            while i<len(self.differenza):
                if self.zone_df.loc[self.zone[i]]['Borough']== borough:
                    if upper_lower == 'lower':
                        
                        if self.differenza[i] <= self.percentuale :
                            inizio.append(self.inizio_corsa[i])
                            durata.append(self.differenza[i])
                            zona.append(self.zone[i])
                            self.nome_zona=self.zone_df.loc[self.zone[i]]['Zone']
                            nomi_zone.append(self.nome_zona)
                            borough_zona=self.zone_df.loc[self.zone[i]]['Borough']
                            borough_lista.append(borough_zona)
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
                            borough_zona=self.zone_df.loc[self.zone[i]]['Borough']
                            borough_lista.append(borough_zona)
                            i = i + 1
                    
                        else: 
                            i= i + 1
                    else:
                        print('Va specificato upper/lower')
                        sys.exit()
                else:
                    i= i + 1
            if len(durata)==0:
                print('nel Borough:' , borough, 'non ci sono corse che soddisfano la richiesta')
                sys.exit()
            else:        
                data = {   
                        'id_zona': zona,
                        'nome_zona':nomi_zone,
                        'inizio': inizio,
                        'durata': durata,
                        'borough':borough_lista
                        }
            
                    
        return data

    