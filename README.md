ANALISI CORSE TAXI  

Il programma prevede l'analisi delle corse dei Taxi nella città di New York.
L'analisi fatta sui file forniti prevede la realizzazione delle seguenti richieste:
1)Quanto durano i viaggi? 
2)In quali zone si svolgono viaggi più lunghi? E invece più corti? 

L'esecuzione del programma prevede che siano digitati sulla linea di comando:
python main.py -y year -m month -b borough

Nel caso in cui non venga inserito alcun borough l'analisi verrà svolta sull'intera città di New York,
altrimenti l'analisi verrà svolta sul borough desiderato. 

Se non specificato alcun valore saranno presi per convenzione i valori di default specificati per anno e mese, rispettivamente (2020,03),
ovvero anno e mese associati al file utilizzato per una prima analisi dei dati.

L'esecuzione del programma prevedrà che nella cartella Output vengano salvati tre file:
-Corse_brevi
-Corse_lunghe
- GraficoTaxi

I file contengono le seguenti informazioni:
-zona,nome_zona,inizio,durata,borough per le tratte in cui la durata del viaggio è maggiore del 25°percentile.
-zona,nome_zona,inizio,durata,borough per le tratte in cui la durata del viaggio è maggiore del 75°percentile.
-un grafico che riporta la durata di tutte le corse sull'intera città di New York, e le durate delle corse brevi e lunghe, attraverso l'utilizzo di tre boxplot.

Chiaramente se l'analisi viene specificata su un particolare borough il grafico riporterà la durata delle corse brevi e lunghe nel borough specificato, altrimenti sull'intera città di New York.

Autori:
Luca Bracaglia, Daniele Mercuri
