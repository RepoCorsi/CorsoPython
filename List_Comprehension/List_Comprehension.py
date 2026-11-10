#--List Comprehension
# -La struttura generale è: 
#[espressione for elemento in sequenza o iterabile if condizione]
#Crea una lista mettendo dentro espressione, per ogni elemento della sequenza, se condizione è vera
# È una LISTA quindi ci vanno [] le QUADRE. Sono gli ARRAY negli altri linguaggi.

# Creare una lista:
lista = []
for i in range(7):
    lista.append(i)
print(lista) 

#con list comprehension
lista = [i for i in range(7)]
print(lista)  # Output: [0, 1, 2, 3, 4, 5, 6]

# Con operazioni nelle espressioni:
numeri = [1, 2, 3, 4, 5, 6]

doppi = [numero * 2 for numero in numeri]
print(doppi)  # Output: [2, 4, 6, 8, 10, 12]

#Lo stesso normalmente scritto con un ciclo for
doppi = []
for numero in numeri:  
    doppi.append(numero * 2)
print(doppi)  # Output: [2, 4, 6, 8, 10, 12]
#------------------------------------------------------

# Se volessi aggiungere "€" ad ogni numero
numeri = [1, 2, 3, 4, 5, 6]
numeri_con_euro = [f"{x}€" for x in numeri]
print(numeri_con_euro)

#-------------------------------------------------------
#---Con IF--- (List Comprehension con condizione)
doppi = [numero * 2 for numero in numeri if numero % 2 == 0]
#--Per ogni numero dentro numeri, se numero è pari, metti numero * 2
print(doppi)  # Output: [4, 8, 12]

#Lo stesso normalmente scritto con un ciclo for
doppi = []

for numero in numeri:
    if numero % 2 == 0:
        doppi.append(numero * 2)
print(doppi)  # Output: [4, 8, 12]

#----------------------------------------------------------
#-  Possiamo anche modificare gli elementi
nomi = ["mario", "luigi", "anna"]
# Vogliamo trasformarli tutti in maiuscolo:
maiuscoli = [nome.upper() for nome in nomi]
print(maiuscoli)  # Output: ['MARIO', 'LUIGI', 'ANNA']

#Solo quelli che iniziano con la lettera "a"
maiuscoli = [nome.upper() for nome in nomi if nome.startswith("a")]
print(maiuscoli) # Output: ['ANNA']

#solo quelli che hanno più di 4 lettere
maiuscoli = [nome.upper() for nome in nomi if len(nome) > 4]
print(maiuscoli) # Output: ['MARIO', 'LUIGI']

#-------------------------------------------------------------
# Temperatura sottozero:
temperature = [22, 15, -3, 31, 0, -8, 12]
sottozero=[x for x in temperature if x<0]
print(sottozero)

#-------------------------------
# Teniamo solo i picchi di traffico superiori a 100 accessi
visualizzazioni = [120, 45, 300, 89, 12, 450]

accessi_mag_100 = [v for v in visualizzazioni if v > 100]

print(accessi_mag_100)  # [120, 300, 450]

#-------------------------------------
#Sconto del 10% (moltiplica per 0.9) solo ai prodotti che costano più di 30 euro.
prezzi=[10, 25, 50, 80]

scontati=[x*0.9 for x in prezzi if x>30]
print(scontati)
#---------------------------------------------

# una lista di stringhe. Vuoi tenere solo le parole che iniziano con la lettera "p" e trasformarle tutte in maiuscolo.

animali = ["cane", "gatto", "pesce", "topo", "pitecantropo", "triceratopo"]

lista=(x.upper() for x in animali if x.startswith("p"))
print (list(lista))

#------------------------------------------------
#Solo per i numeri positivi: calcolare il 22% di (IVA) e convertirli in dollari X 1.10
prezzi_grezzi = [10, -5, 100, 0, 50, -12, 20]

# Mantiene i dati come numeri decimali (float)
risultato = [round((x * 1.22) * 1.10, 2) for x in prezzi_grezzi if x > 0]

print(risultato)
# Output: [13.42, 134.2, 67.1, 26.84]
#------------------------------------------------------

#generator expression:
frase="il pitecantropo e il triceratopo si sono estinti"
a,e,i,o,u=(frase.count(x) for x in "aeiou")
print (a,e,i,o,u)

#-----------------------------------------------------------
#Condizioni Multiple (if concatenati)
#[espressione for elemento in iterabile if cond1 if cond2 if cond3... ]

## Vogliamo solo i numeri che sono SIA pari SIA divisibili per 5
numeri = [14, 22, 35, 40, 55, 60, 77, 80]

# Vogliamo solo i numeri che sono sia pari SIA divisibili per 5
risultato = [n for n in numeri if n % 2 == 0 if n % 5 == 0] #la and è opzionale
# si può scrivere anche così:
risultato = [n for n in numeri if n % 2 == 0 and n % 5 == 0] #la and è opzionale

print(risultato)  # [40, 60, 80]

#--------------------------------------------------------
#Vogliamo moltiplicarli per 2

risultato = [n*2 for n in numeri if n % 2 == 0 if n % 5 == 0]

print(risultato)  # [80, 120, 160]
#----------------------------------------------------------
import random

# 50 numeri casuali da 1 a 100
numeri_casuali = [random.randint(1, 100) for x in range(1, 51)]

print(numeri_casuali)

# divisibili per 3 e magg di 20
risultato = [n for n in numeri_casuali if n % 3 == 0 if n > 20]

print("\nNumeri filtrati (multipli di 3 e maggiori di 20):")
print(risultato)

#----------------------------------
#col for equivalente è:
import random

# 1. Generiamo 50 numeri casuali da 1 a 100
numeri_casuali = []

for x in range(1, 51):
    numero = random.randint(1, 100)
    numeri_casuali.append(numero)

print(numeri_casuali)


# 2. Filtriamo i numeri multipli di 3 e maggiori di 20
risultato = []

for n in numeri_casuali:
    if n % 3 == 0:
        if n > 20:
            risultato.append(n)

print("\nNumeri filtrati (multipli di 3 e maggiori di 20):")
print(risultato)

#------------------------------------------------------------
#Trasformazione Condizionale (if-else all'inizio)
#se succede A fai X, altrimenti fai Y
#Esempio guida: Sostituire o categorizzare i dati (es. flagging di anomalie).

# Se il numero è positivo lascia invariato, se è negativo trasformalo in 0

valori = [10, -3, 25, 0, -8, 14]

# Se il numero è positivo lascia invariato, se è negativo trasformalo in 0
valori_puliti = [x if x >= 0 else 0 for x in valori]

print(valori_puliti)  # [10, 0, 25, 0, 0, 14]

#---------------------------------------------

#Solo i maggiori di zero
valori_puliti = [x if x >= 0 else 0 for x in valori if x>0]

print(valori_puliti)  # [10, 0, 25, 0, 0, 14]
#----------------------------------------------------
#Dict comprehension:
studenti = [
    {"nome": "Anna", "eta": 20, "voto": 28},
    {"nome": "Marco", "eta": 22, "voto": 25},
    {"nome": "Elena", "eta": 21, "voto": 30}
]

studenti_bravi = [s for s in studenti if s["voto"] >= 28]
print(studenti_bravi)
# Output: [{'nome': 'Anna', 'eta': 20, 'voto': 28}, {'nome': 'Elena', 'eta': 21, 'voto': 30}]
#-----------------------------------------------------

# Dictionary Comprehension che applica uno sconto del 10% solo ai prodotti che costano più di 2 euro.
prodotti = ["mela", "banana", "kiwi", "pitecantropo"]
prezzi = [1, 2, 3, 4]

# Creiamo il nostro dizionario scontato
scontati = {prodotto: prezzo * 0.9 for prodotto, prezzo in zip(prodotti, prezzi) if prezzo > 2}
print(scontati)

#----------------------------------------------
# più condizioni e più operazioni:
a = [1, 2]
b = ["A", "B"]

risultato = [(x, y) for x in a for y in b] #2 elementi di a per 2 elementi di b = 4 combinazioni totali.Prodotto cartesiano
print(risultato)  # Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

risultato = []

# Equivale a:
for x in a:
    for y in b:
        risultato.append((x, y))
print(risultato)  # Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

#-----------------------------------------------------------

# ESEMPIO MALVAGIO. Non è subito chiaro che il SECONDO for contiene una condizione falsa che invalida anche il primo for e risulta in una lista vuota.
numeri = [1, 2, 3, 4, 5, 6]
altri = [10, 20, 30, 40, 50, 60]

risultato = [
    x + y
    for x in numeri
    if x > 0
    for y in altri
    if y < 10 #nessun valore è <10 quindi risulta tutto vuoto alla fine
]

print(risultato) #lista vuota perché non ci sono elementi in "altri" che soddisfano la condizione y < 10

# -- Con il for equivale a:
for x in numeri:
    if x > 0:
        for y in altri: #nessun loop
            if y < 10: # Qui si vede bene che la condizione è falsa, quindi non viene popolata la lista
                risultato.append(x + y)
print(risultato)
#----------------------------------------------------

# Quando puoi descrivere l'operazione con una frase semplice: "Dammi X trasformato, per ogni X, se condizione." allora usa la list comprehension.
# Quando la frase diventa:
# "Per ogni X, prima fai questo; se succede questo fai quest'altro; poi controlla quest'altra cosa; eventualmente continua; poi fai quest'altra operazione..." Allora usa il for.

# La regola è che se devi spiegare una list comprehension per cinque minuti per convincere qualcuno che è leggibile, probabilmente era meglio scrivere un for.

# Obiettivo: creare una nuova lista chiamata risultato contenente esclusivamente le persone maggiorenni con un'età valida e il nome in maiuscolo

'''
# Passi da fare:
1. Scartare le righe vuote: Ignora i record senza testo o composti solo da spazi (grazie a if riga.strip()).
2. Separare i dati: Prende ogni riga valida e la "spezza" in due parti usando la virgola come separatore, assegnando i valori alle variabili nome e eta.
3. Controlla la validità e l'età: Verifica che l'età sia un numero composto solo da cifre (scartando errori come "abc") e che il valore numerico sia maggiore o uguale a 18 anni (if eta.isdigit() and int(eta) >= 18).
4. Trasforma il formato finale: Per i record che superano tutti i controlli, converte il nome in lettere maiuscole, trasforma l'età in un numero intero (int) e salva la coppia all'interno di una tupla.

'''

righe = [
    "Mario,25",
    "Luca,17",
    "",
    "Anna,31",
    "Paolo,abc",
    "Giulia,28"
]

risultato = [
    (nome.upper(), int(eta))
    for riga in righe #<--lista
    if riga.strip()
    
    for nome, eta in [riga.strip().split(",")] #<--lista
    if eta.isdigit() and int(eta) >= 18
]
print(risultato)
#[('MARIO', 25), ('ANNA', 31), ('GIULIA', 28)]

#------------------------------------------------
#Stesso codice col ciclo for:
# MOTTO ZEN di Python: la leggibilità è più importante della concisione.

righe = [
    "Mario,25",
    "Luca,17",
    "",
    "Anna,31",
    "Paolo,abc",
    "Giulia,28"
]

risultato = []

for riga in righe:
    if riga.strip():
        nome, eta = riga.strip().split(",")

        if eta.isdigit() and int(eta) >= 18:
            risultato.append((nome.upper(), int(eta)))

print(risultato)

# non tutto quello che si può fare con una list comprehension va fatto con una list comprehension.

#-----------------------------------------------------
#ESERCIZI:
# 1. Data una lista di parole ["casa", "albero", "sole", "cane", "bottiglia", "computer", "cielo"] 
# crea una lista di parole MAIUSCOLE che contenga solo le parole che hanno più di 4 lettere ed iniziano per "c" 

parole=["casa", "albero", "sole", "cane", "bottiglia", "computer", "cielo"] 

ris=[x.upper() for x in parole if len(x)>4 if x.startswith("c")]
print(ris)

#-------------------------------------------------------
#2. #Data una lista di voti scolastici da 1 a 10, crea una lista di stringhe dove ogni voto ≥ 6 diventa "promosso" e ogni voto < 6 diventa "bocciato".
import random
voti=[random.randint(1,10) for x in range(1,11)]
print(voti)

ris=["promosso" if x>=6 else "respinto" for x in voti]
print(ris)

#-----------------
#dict comprehension:
#Le chiavi sono univoche e non vengono duplicate!
ris={x: "promosso" if x>=6 else "respinto" for x in voti}
print(ris)

#Esempio con duplicati:
ris_raggruppato = {
    "promosso": [x for x in voti if x >= 6],
    "respinto": [x for x in voti if x < 6]
}
print(ris_raggruppato)

