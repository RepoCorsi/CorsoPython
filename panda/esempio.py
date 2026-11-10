import pandas as pd

#Puoi creare una tabella partendo da un semplice dizionario
# Creiamo un piccolo dizionario con i dati di alcuni prodotti
dati = {
    'Prodotto': ['Mela', 'Banana', 'Arancia', 'Fragola', 'Kiwi'],
    'Prezzo': [1.20, 0.80, 1.50, 3.00, 2.10],
    'Disponibile': [True, True, False, True, False]
}

# Convertiamo il dizionario in un DataFrame di Pandas
df = pd.DataFrame(dati)

#Per dare una rapida occhiata alla struttura e alle righe del tuo DataFrame:
print(df.head(3))  # Mostra solo le prime 3 righe
print(df.shape)   # Restituisce il numero di (righe, colonne) -> (5, 3)
print(df.info())  # Mostra i tipi di dati (numeri, stringhe, booleani)

#stampa tutto:
print(df)

#Selezionare e Filtrare i Dati
#Puoi estrarre singole colonne o righe specifiche in base a determinate condizioni
#Isolare una colonna:
print(df['Prodotto'])  # Estrae solo la colonna dei nomi

#Filtrare per condizione (es. prodotti che costano più di 1 euro):
prodotti_cari = df[df['Prezzo'] > 1.00]
print(prodotti_cari)

#Filtrare per condizioni multiple (usando & per "e" oppure | per "o"):
# Prodotti disponibili che costano meno di 2 euro
filtro = df[(df['Disponibile'] == True) & (df['Prezzo'] < 2.00)]
print(filtro)


#Calcoli Rapidi e Statistiche
#Pandas esegue calcoli matematici sull'intera colonna all'istante:
prezzo_medio = df['Prezzo'].mean()  # Calcola la media dei prezzi
prezzo_massimo = df['Prezzo'].max() # Trova il prezzo più alto

print(f"Prezzo medio: {prezzo_medio}€")
print("*"*30)
print(df.describe())  # Genera un riepilogo statistico automatico

#Modificare la Tabella
#Aggiungere o aggiornare colonne è immediato
# Aggiungiamo una colonna con la quantità in magazzino
df['Quantita'] = [100, 150, 0, 50, 0]

# Creiamo una colonna calcolata (Prezzo ivato al 22%)
df['Prezzo_IVA'] = df['Prezzo'] * 1.22
print("*"*30)

#stampiamo tutto
print(df)

#Salvare il Lavoro
#Una volta modificati i dati, puoi esportarli in un nuovo file in un secondo
df.to_csv('prodotti_aggiornati.csv', index=False) # index=False evita di salvare la colonna dei numeri di riga

