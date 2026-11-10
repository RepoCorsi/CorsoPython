# 4 TIPI DI COMPREHENSION:
#List Comprehension, Set Comprehension, Dict Comprehension, Generator Expression. 
#NON ESISTE TUPLE EXPRESSION MA AL SUO POSTO C'è Generator Expression

#--List Comprehension

# -La struttura generale è: 

# [ESPRESSIONE FOR ELEMENTO IN SEQUENZA O ITERABILE IF CONDIZIONE]

# Per ogni elemento nella sequenza, controlla la condizione; se è vera, applica l'espressione e inserisci il risultato nella nuova lista.

# È una LISTA quindi ci vanno [] le QUADRE. 

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
print(numeri_con_euro) # ['1€', '2€', '3€', '4€', '5€', '6€']
#----------------------------------------------------------

nomi = [" Mario ", " Luigi ", " Anna "]

#Vogliamo togliere gli spazi:

nomi_puliti = [nome.strip() for nome in nomi] # strip() elimina gli spazi all'inizio e alla fine.
print(nomi_puliti) #['Mario', 'Luigi', 'Anna']
#-----------------------------------------------------------

# Vogliamo trasformarli tutti in maiuscolo:
nomi = ["mario", "luigi", "anna"]

nomi_puliti = [nome.strip().upper() for nome in nomi] 
print(nomi_puliti) # Output: ['MARIO', 'LUIGI', 'ANNA']
#----------------------------------------------------------------

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
#------------------------------------------------------------

nomi = ["Mario", "", "Luigi", "", "Anna"]

#Vogliamo eliminare i nomi vuoti.

nomi_validi = [nome for nome in nomi if nome] # if nome significa tieni nome se NON è vuoto.
print(nomi_validi) #['Mario', 'Luigi', 'Anna']
#----------------------------------------------------------

#Solo quelli che iniziano con la lettera "a"
maiuscoli = [nome.upper() for nome in nomi if nome.startswith("a")]
print(maiuscoli) # Output: ['ANNA']

#solo quelli che hanno più di 4 lettere
maiuscoli = [nome.upper() for nome in nomi if len(nome) > 4]
print(maiuscoli) # Output: ['MARIO', 'LUIGI']
#---------------------------------------------------

#solo le maiuscole

maiuscole={c for c in 'aAbBcCdDeE' if c.isupper()}
print(maiuscole)

#--------------------------------------------------

# toglie gli spazi e tiene solo i valori NON VUOTI
lines = [" Ciao ", 
        "  ", 
        "  Mario", 
        "Python  ",  
        "   "]

risultato = [line.strip() for line in lines if line.strip()]
print(risultato)

#-------------------------------------------------------------
# Temperatura sottozero:
temperature = [22, 15, -3, 31, 0, -8, 12]
sottozero=[x for x in temperature if x<0]
print(sottozero) #[-3, -8]

#-------------------------------
# Teniamo solo i picchi di traffico superiori a 100 accessi
visualizzazioni = [120, 45, 300, 89, 12, 450]

accessi_mag_100 = [v for v in visualizzazioni if v > 100]

print(accessi_mag_100)  # [120, 300, 450]
#---------------------------------------------------------

# solo i numeri dispari moltiplicati per 3
numeri = [1, 2, 3, 4, 5]

risultato = [x * 3 for x in numeri if x % 2 == 1]
print(risultato) #[3, 9, 15]

#-------------------------------------
#Sconto del 10% (moltiplica per 0.9) solo ai prodotti che costano più di 30 euro.
prezzi=[10, 25, 50, 80]

scontati=[x*0.9 for x in prezzi if x>30]
print(scontati) #[45.0, 72.0]
#---------------------------------------------

# Tenere solo le parole che iniziano con la lettera "p" e trasformarle tutte in maiuscolo.

animali = ["cane", "gatto", "pesce", "topo", "pitecantropo", "triceratopo"]

lista=(x.upper() for x in animali if x.startswith("p"))
print (list(lista)) #['PESCE', 'PITECANTROPO']

#------------------------------------------------
#Solo per i numeri positivi: calcolare il 22% di (IVA) e convertirli in dollari. TASSO: 1.10 (prezzo X 1.10)
prezzi_grezzi = [10, -5, 100, 0, 50, -12, 20]

# Mantiene i dati come numeri decimali (float)
risultato = [round((x * 1.22) * 1.10, 2) for x in prezzi_grezzi if x > 0]

print(risultato)
# Output: [13.42, 134.2, 67.1, 26.84]
#------------------------------------------------------

#generator expression:
frase="il pitecantropo e il triceratopo si sono estinti"
a,e,i,o,u=(frase.count(x) for x in "aeiou")
print (a,e,i,o,u) #2 4 7 6 0

#--Altro esempio
password="Ciao123!"

#generator expression
print(list((c.isupper() for c in password)))#contiene maiuscole [True, False, False, False, False, False, False, False]
print(list((c.islower() for c in password))) #contiene minuscole [False, True, True, True, False, False, False, False]
print(list((c.isdigit() for c in password)))#contiene solo numeri [False, False, False, False, True, True, True, False]
print(list((c.isalnum() for c in password)))#contiene solo lettere o numeri. NO SPAZIO O SIMBOLI !*#@ [True, True, True, True, True, True, True, False]

print("*"*30)

#controllare ciascun caratteri con Any:
print(any(c.isupper() for c in password)) #ALMENO 1 carattere è maiuscolo? True
print(any(c.islower() for c in password)) #ALMENO 1 carattere è minuscolo? True
print(any(c.isdigit() for c in password)) #ALMENO 1 carattere è un numero? True
print(any(c.isalnum() for c in password)) #ALMENO 1 carattere è una lettera o numeri. NO SPAZIO O SIMBOLI !*#@? True

print("*"*30)

#controllare tutti i caratteri con Any:
print(all(c.isupper() for c in password)) #TUTTI i caratteri sono maiuscoli? False
print(all(c.islower() for c in password)) #TUTTI i caratteri sono minuscoli? False
print(all(c.isdigit() for c in password)) #TUTTI i caratteri sono numeri? False
print(all(c.isalnum() for c in password)) #TUTTI i caratteri sono lettere o numeri. NO SPAZIO O SIMBOLI !*#@? False


#-----------------------------------------------------------
#Condizioni Multiple (if concatenati)
#[espressione for elemento in iterabile if cond1 if cond2 if cond3... ]

## Vogliamo solo i numeri che sono PARI e DIVISIBILI PER 5
numeri = [14, 22, 35, 40, 55, 60, 77, 80]

# Vogliamo solo i numeri SIA PARI SIA DIVISIBILI per 5
risultato = [n for n in numeri if n % 2 == 0 if n % 5 == 0] #la and è opzionale
# si può scrivere anche così:
risultato = [n for n in numeri if n % 2 == 0 and n % 5 == 0] #Esempio con and

print(risultato)  # [40, 60, 80]

# -- Stesso esempio col for
risultato=[]

for n in numeri:
    if n % 2 == 0:
        if n % 5 == 0:
            risultato.append(n)
print(risultato)

risultato=[]
for n in numeri:
    if n % 2 == 0 and n % 5 == 0:
            risultato.append(n)
print(risultato)

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
#------------------------------------------------------------

numeri=[1,2,3,4,5,6,8,10]

doppi_o_tripli=[x*2 if x%2==0 else x*3 for x in numeri if x>=3 and x<=10]

print(doppi_o_tripli)

#--------------------------------------------------------

#Set comprehension -> elimina i duplicati 

numeri = [1, 2, 2, 3, 4, 4, 5, 5, 5]

risultato = {x * 2 for x in numeri}
print(risultato) #{2, 4, 6, 8, 10}


#----------------------------------------------------

#Dict comprehension:

#Con un dizionario possiamo costruire coppie chiave → valore:

numeri = [1, 2, 3, 4]
#"Per ogni x dentro numeri, crea una coppia dove la chiave è x e il valore è x * 2."

#dizionario
doppi = {x: x * 2 for x in numeri} #{1: 2, 2: 4, 3: 6, 4: 8}
print(doppi)

#set compreension:
#doppi={ f"il doppio di {x}: è {x*2}"  for x in numeri} #non è più un dict perchè la chiave e valore è dentro le "" e non viene riconosciuto come dizionario 
#----------------------------------------------------------------
numeri = [1, 2, 3, 4, 5, 6]

quadrati = {
    x: x ** 2
    for x in numeri
    if x % 2 == 0 #Prendiamo solo i pari
}
print(quadrati) #{2: 4, 4: 16, 6: 36}
#-------------------------------------------------------
nomi = ["Mario", "Luca", "Anna"]

#Un dizionario in cui la chiave è il nome e il valore è la lunghezza:

lunghezze = {
    nome: len(nome)
    for nome in nomi
}

print(lunghezze) #{'Mario': 5, 'Luca': 4, 'Anna': 4}

#-----------------------------------------------------
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
print(scontati) #{'kiwi': 2.7, 'pitecantropo': 3.6}
#-------------------------------------------------------------

#Confrontiamo le tre forme
numeri = [1, 2, 2, 3, 3, 3, 4]

#List comprehension
ris=[x * 2 for x in numeri]
print(ris) #→ crea una lista [2, 4, 4, 6, 6, 6, 8]


#Set comprehension NON é ORDINATO!!!
ris={x * 2 for x in numeri}
print(ris) #→ crea un set {8, 2, 4, 6} NON é ORDINATO!!!


#Dict comprehension
ris={x: x * 2 for x in numeri}
print(ris) #→ crea un dizionario {1: 2, 2: 4, 3: 6, 4: 8}
#------------------------------------------------------------------
#associare 2 liste
prodotti = ["mela", "banana", "kiwi", "pitecantropo"]
prezzi = [1,2,3,4]

dizionario=dict(zip(prodotti, prezzi))
print (dizionario)
#Se una lista è più corta dell'altra, zip() si ferma automaticamente all'ultimo elemento della lista più corta senza mandare il programma in crash

# Uniamo e filtriamo in un colpo solo!
prezzoMag2 = {prodotto: prezzo for prodotto, prezzo in zip(prodotti, prezzi) if  prezzo> 2}

print(prezzoMag2)  # Output: {'kiwi': 3, 'pitecantropo': 4}

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
#---------------------------------------------------------------------
#oppure
risultato = [c+n for c in 'ABC' for n in '123']
print(risultato)  #['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

risultato = []
for c in 'ABC':
    for n in '123':
        risultato.append(c+n)
print(risultato) #['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']


#-----------------------------------------------------------

# ESEMPIO MALVAGIO. Non è subito chiaro che il SECONDO for contiene una condizione falsa che invalida anche il primo for e risulta in una lista vuota.
numeri = [1, 2, 3, 4, 5, 6]
altri = [10, 20, 30, 40, 50, 60]

#Per ogni x positivo, per ogni y minore di 10, inserisci x + y.

risultato = [
    x + y  
    for x in numeri  if x > 0
    for y in altri if y < 10 #nessun valore è <10 quindi risulta tutto vuoto alla fine
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

numeri = [12, -4, 7, 20, 3, -8, 15]

# Obiettivo:
# ignorare i numeri negativi;
# ignorare lo zero;
# se il numero è pari, moltiplicarlo per 2;
# se è dispari, moltiplicarlo per 3;
# tenere solo i risultati maggiori di 20.
# Una possibile list comprehension sarebbe:

risultato = [
    x * 2 if x % 2 == 0 else x * 3
    for x in numeri
    if x > 0 and (x * 2 if x % 2 == 0 else x * 3) > 20
]

print(risultato) #[24, 21, 40, 45]

#Stesso codice col ciclo for:
# MOTTO ZEN di Python: la leggibilità è più importante della concisione.

risultato = []

for x in numeri:
    if x <= 0:
        continue

    if x % 2 == 0:
        valore = x * 2
    else:
        valore = x * 3

    if valore > 20:
        risultato.append(valore)
print(risultato) #[24, 21, 40, 45]

# non tutto quello che si può fare con una list comprehension va fatto con una list comprehension.
#---------------------------------------------------------------

# La regola pratica che ti consiglio è:

# Usa una list comprehension quando vuoi creare una nuova lista in modo semplice e leggibile. Usa un for normale quando devi fare più operazioni, prendere decisioni, modificare qualcosa o quando la comprehension diventa difficile da leggere.

# 1. Quando la list comprehension è perfetta
# Se devi trasformare tutti gli elementi di una lista:

numeri = [1, 2, 3, 4]

doppi = [x * 2 for x in numeri]

# È molto leggibile. Con un for normale dovresti scrivere:

doppi = []

for x in numeri:
    doppi.append(x * 2)

# 2. Anche per filtrare Se vuoi prendere solo alcuni elementi:

numeri = [1, 2, 3, 4, 5, 6]

pari = [x for x in numeri if x % 2 == 0]

# Molto chiaro: "Dammi x per ogni x in numeri, se x è pari."

# 3. Trasformazione + filtro
# Anche questo è un ottimo caso:

numeri = [1, 2, 3, 4, 5, 6]

risultato = [x * 10 for x in numeri if x > 3]



# 4. Quando è meglio un for normale
# Immagina di avere questa situazione:

numeri = [1, 2, 3, 4, 5]

risultato = []

for x in numeri:
    if x % 2 == 0:
        y = x * 10
        print("Ho trovato:", y)

        if y > 20:
            risultato.append(y)

# Qui un for normale è decisamente meglio.

# Potresti teoricamente cercare di trasformarlo in una comprehension, ma diventerebbe un pasticcio.



#-----------------------------------------------------
#ESERCIZI:
# 1. Data una lista di parole ["casa", "albero", "sole", "cane", "bottiglia", "computer", "cielo"] 
# crea una lista di parole MAIUSCOLE che contenga solo le parole che hanno più di 4 lettere ed iniziano per "c" 

parole=["casa", "albero", "sole", "cane", "bottiglia", "computer", "cielo"] 

ris=[x.upper() for x in parole if len(x)>4 if x.startswith("c")]
print(ris) #['COMPUTER', 'CIELO']

#-------------------------------------------------------
#2. #Data una lista di 10 voti scolastici casuali da 1 a 10, crea una lista di stringhe dove ogni voto ≥ 6 diventa "promosso" e ogni voto < 6 diventa "bocciato".
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

#-----------------------------------

#ESEMPIO COMPLETO:
#dato una lista di 5 voti scolastici casuali da 1 a 10, e una lista 5 di nomi 
#crea una dizionario dove ogni voto >=6 diventa "promosso" e ogni voto <6 diventa "bocciato":
#output un dizionario fatto così:
# mario: promosso con 6
# laura: pronossa con 7
# gigi: bocciato con 4

import random
nomi=["a","b","c","d","e"]
voti=[random.randint(1,10) for _ in range(1,6)]
print(voti) # [8, 5, 1, 9, 9]

ris={nome: f"promosso con {x}" if x>=6 else f"bocciato con {x}" for nome,x in zip(nomi,voti)}
print(ris)

# Ciclo for usando .items()
for nome, risultato in ris.items():
    print(f"Studente {nome}: {risultato}")

#output:
# {'a': 'promosso con 8', 'b': 'bocciato con 5', 'c': 'bocciato con 1', 'd': 'promosso con 9', 'e': 'promosso con 9'}
# Studente a: promosso con 8
# Studente b: bocciato con 5
# Studente c: bocciato con 1
# Studente d: promosso con 9
# Studente e: promosso con 9

#------------------------------------
# Esempio raggruppato:

ris_raggruppato = {
    "PROMOSSO": {nome: f"promosso con {x}" for nome,x in zip(nomi,voti) if x>=6},
    "RESPINTO": {nome: f"bocciato con {x}" for nome,x in zip(nomi,voti) if x<6}
}
print(ris_raggruppato) #{'PROMOSSO': {'a': 'promosso con 8', 'd': 'promosso con 9', 'e': 'promosso con 9'}, 'RESPINTO': {'b': 'bocciato con 5', 'c': 'bocciato con 1'}}


#Ciclo per separare le categorie su righe diverse
for stato, studenti in ris_raggruppato.items():
    print(f"{stato.upper()}: {studenti}")

#output:
# PROMOSSO: {'a': 'promosso con 8', 'd': 'promosso con 9', 'e': 'promosso con 9'}
# RESPINTO: {'b': 'bocciato con 5', 'c': 'bocciato con 1'}


#oppure più formattato:
for stato, studenti in ris_raggruppato.items():
    print(f"\n--- ELENCO {stato.upper()} ---")
    for nome, dettaglio in studenti.items():
        print(f"  Studente {nome}: {dettaglio}")

#output:
# --- ELENCO PROMOSSO ---
  # Studente a: promosso con 8
  # Studente d: promosso con 9
  # Studente e: promosso con 9

# --- ELENCO RESPINTO ---
  # Studente b: bocciato con 5
  # Studente c: bocciato con 1