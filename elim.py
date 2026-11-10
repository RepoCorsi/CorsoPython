
print("a","b","c", sep="-")

# Qual è il motivo di usare list in questo caso, se le stringhe sono già naturalmente "scorribili" con un for perché sono comunque una sequenza? E qual è l'uso più comune che si fa di list? mi fai degli esempi di utilizzo, così posso capire in quali casi è utile usarlo?
# stringa = "ciao"

# #array_caratteri = list(stringa) 

# for lettera in stringa:
#     print(lettera)
    
    
parole=["cane","gatto","pesce","topo","pitecantropo","triceratopo"]
maiuscole=list(map(str.upper,parole))
print (maiuscole)

# Ma map si usa solo per le liste?

# censuratore senza list
parola = "segreto"
parola = parola.replace("e", "*")
parola = parola.replace("o", "*")
print(parola)

# Vedere una versione ancora più corta di questo esperimento usando le funzioni lambda (funzioni anonime su una sola riga)
# Ma map come primo argomento accetta quello che viene chiamata una funzione di callback?

# programma che conta quante vocali ci sono in una frase:
# Non conosco bene python e ho tirato fuoriquesta soluzione. Non so se mi sono complicato troppo la vita, o se c'è un metodo più semplice 😂
# frase="il pitecantropo e il triceratopo si sono estinti"
# a,e,i,o,u=(frase.count(x) for x in "aeiou")
# print (a,e,i,o,u)

#--------------------------------
from collections import Counter

frase = "il pitecantropo e il triceratopo si sono estinti"

# Counter conta TUTTI i caratteri della frase in un colpo solo
frequenze = Counter(frase.lower())
print(frequenze)

# Estraiamo solo i dati che ci interessano per le vocali
a, e, i, o, u = (frequenze[x] for x in "aeiou")
print(a, e, i, o, u)  # Output: 2 4 5 6 0

print("*"*30)
frase = "il pitecantropo e il triceratopo si sono estinti"

# Usiamo str.count legato alla nostra frase tramite una lambda "al volo"
a, e, i, o, u = map(lambda x: frase.count(x), "aeiou")

print(a, e, i, o, u)  # Output: 2 4 5 6 0
#----------------------------------------------------------

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Modo A: Con una funzione normale
def è_pari(x):
    return x % 2 == 0  # Restituisce True se il numero è pari

# filter() fa il ciclo invisibile su 'numeri' e applica la callback
numeri_pari = list(filter(è_pari, numeri))
print(numeri_pari)  # Output: [2, 4, 6, 8, 10]


# ma list, come logica, fa una cosa del genere?  
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari_dispari=list(x for x in numeri if è_pari(x) )
print (pari_dispari)

print("*"*30)

# solo positivi:
numeri = [10, -5, 0, 3, -1, 8]
positivi=list(filter(lambda x: x>0,numeri))
print (positivi)

print("TUTTO","*" *30)

prezzi_grezzi = [10, -5, 100, 0, 50, -12, 20]
# scartare i prezzi errati e, sui prezzi validi rimasti, applicare un aumento del 22% (calcolare il prezzo con IVA) trasformandoli in dollari [dollaro = 1.10€].

validi=list(filter(lambda x: x>0, prezzi_grezzi))
print (validi)

aumento=list(map(lambda x: (x*.22)+x, validi))
print(aumento)

dollari=list(map(lambda x: x*1.10, aumento))

for x in dollari:
    print(f"dollari: {x:.2f} ")

#print(f"dollari: {dollari:.2f} ")

# nel tuo esempio non hai applicato il 22% di iva.
# La soluzone potrebbe essere questa:
prezzi_grezzi = [10, -5, 100, 0, 50, -12, 20]
aumento=list(
    map(
        lambda x: x*1.10, 
            map(lambda x: (x*.22)+x,         
                filter(lambda x: x>0, prezzi_grezzi)        
                ))        
    )
for x in aumento:
    print(f"dollari: {x:.2f} ")

# La lambda può fare più calcoli di fila:
# Moltiplichiamo il prezzo prima per 1.22 (IVA) e poi il risultato per 1.10 (Dollari)
prezzi_grezzi = [10, -5, 100, 0, 50, -12, 20]

aumento_ottimizzato = list(
    map(
        lambda x: (x * 1.22) * 1.10, filter(lambda x: x > 0, prezzi_grezzi)
    )
)
for x in aumento_ottimizzato:
    print(f"dollari: {x:.2f} ")
    
#con list comprehension
con_comprehension=[(x * 1.22) * 1.10 for x in prezzi_grezzi if  x > 0]
for x in con_comprehension:
    print(f"dollari: {x:.2f} ")

con_comprehension=((x * 1.22) * 1.10 for x in prezzi_grezzi if  x > 0)
for x in con_comprehension:
    print(f"dollari: {x:.2f} ")
#--------------------------------------------------
print("*"*30)
import sys

# # IMPOSTIAMO IL LIMITE A 10 MILIONI
# limite = 10000000

# print("--- METODO 1: LIST COMPREHENSION ---")
# # Crea una lista FISICA con tutti i 10 milioni di numeri già pronti
# lista_numeri = [x for x in range(limite)]
# memoria_lista = sys.getsizeof(lista_numeri)
# somma_lista = sum(lista_numeri)

# print(f"Somma calcolata: {somma_lista}")
# print(f"Memoria occupata in RAM: {memoria_lista:,} byte (circa {memoria_lista / 1024 / 1024:.2f} MB)")


# print("\n--- METODO 2: GENERATOR EXPRESSION ---")
# # Crea solo la REGOLA ("pigra") per generare i numeri uno alla volta
# generatore_numeri = (x for x in range(limite))
# memoria_generatore = sys.getsizeof(generatore_numeri)
# # sum() consuma il generatore prendendo un numero alla volta
# somma_generatore = sum(generatore_numeri)

# print(f"Somma calcolata: {somma_generatore}")
# print(f"Memoria occupata in RAM: {memoria_generatore:,} byte (circa 0.00 MB)")

print  ("".join(['c', 'i', 'a', 'o']))#diventa "ciao"


numeri = [1, 2, 3, 4, 5, 6]
doppi = [numero * 2 for numero in numeri if numero % 2 == 0]
print(doppi)


doppi=list(map(lambda numero: numero * 2 ,filter(lambda numero: numero % 2 == 0,numeri)))
print(doppi)


import operator
from functools import partial

numeri = [1, 2, 3, 4, 5, 6]

# Creiamo una funzione che controlla se il resto della divisione per 2 è uguale a 0
# (Equivale a: lambda x: x % 2 == 0)
è_pari = partial(lambda x: x % 2 == 0) # Nota: qui la logica del modulo richiede comunque un controllo

# Per il map invece è facilissimo: fissiamo il secondo argomento di mul a 2 (moltiplica per 2)
raddoppia = partial(operator.mul, 2)

# più condizioni e più operazioni:
a = [1, 2]
b = ["A", "B"]

risultato = [(x, y, "ciao","miao","bau") for x in a for y in b]
print(risultato)  # Output: [(1, 'A', 'ciao', 'miao', 'bau'), (1, 'B', 'ciao', 'miao', 'bau'), (2, 'A', 'ciao', 'miao', 'bau'), (2, 'B', 'ciao', 'miao', 'bau')]

nomi = ["Anna", "Luca", "Marco"]
ruoli = ["Admin", "User", "Guest"]

# zip() crea coppie ordinate basate sulla posizione. 
#Accetta qualunque numero di liste, non solo 2
accoppiati = list(zip(nomi, ruoli))

print(accoppiati)  
# Output: [('Anna', 'Admin'), ('Luca', 'User'), ('Marco', 'Guest')]

for nome, ruolo in zip(nomi, ruoli):
    print(f"{nome} è un {ruolo}")


# zip con 3 liste
nomi = ["Anna", "Luca", "Marco"]
eta = [25,30,35]
citta = ["Torino", "Roma", "Catania"]

associati=list(zip(nomi, eta, citta))
print(associati)

for nome, eta, citta in zip(nomi, eta, citta):
    print(f"{nome} ha {eta} anni e abita a {citta}")
    
#-----

# Creiamo il nostro generatore pigro
generatore = (x for x in range(3))  # Contiene virtualmente: 0, 1, 2
generatore_lista = [x for x in range(3)]  # Contiene virtualmente: 0, 1, 2

print("--- Primo utilizzo (con sum) ---")
print(sum(generatore))  # Output: 3 (0 + 1 + 2)

print("--- Primo utilizzo (con sum) con lista---")
print(sum(generatore_lista))  # Output: 3 (0 + 1 + 2)

print("\n--- Secondo utilizzo (con un ciclo for) ---")
for numero in generatore:
    print(numero)  # Non stamperà NULLA!

print("\n--- Secondo utilizzo (con un ciclo for con lista) ---")
for numero in generatore_lista:
    print(numero) 

# Se volessi aggiungere "€" ad ogni numero
numeri = [1, 2, 3, 4, 5, 6]
numeri_con_euro=[str(x)+"€" for x in numeri]
print(numeri_con_euro)

#oppure più facile
# Usiamo la f-string f"{x}€" che trasforma in automatico x in stringa
# Se volessi aggiungere "€" ad ogni numero
numeri = [1, 2, 3, 4, 5, 6]
numeri_con_euro = [f"{x}€" for x in numeri]
print(numeri_con_euro)

#print ([f"{x}€" for x in numeri]) senza variabile numeri_con_euro

#------------------FUNZIONI------------------------------

#Passare una lista ad una funzione:
# MODO ERRATO (NON FARLO): def aggiungi_materia(nome, lista=[]):

# MODO CORRETTO (Usando None):
def aggiungi_materia(nome, lista_materie=None):
    # Se l'utente non ha passato una lista, ne creiamo una nuova NUOVA in quel momento
    if lista_materie is None:
        lista_materie = []
        
    lista_materie.append(nome)
    return lista_materie

# Test
studente1 = aggiungi_materia("Matematica")
print(studente1)  # Output: ['Matematica']

studente2 = aggiungi_materia("Fisica")
print(studente2)  # Output: ['Fisica'] 
# (Se avessimo usato [], studente2 conterrebbe anche 'Matematica'!)


def crea_profilo(nome, **informazioni):
    # 'informazioni' diventa un dizionario: {'ruolo': 'Admin', 'citta': 'Roma'}
    print(f"Utente: {nome}")
    for chiave, valore in informazioni.items():
        print(f"- {chiave}: {valore}")

crea_profilo("Elena", ruolo="Admin", citta="Roma")
# Output:
# Utente: Elena
# - ruolo: Admin
# - citta: Roma

print("*"*30)
def registra_evento(livello, *messaggi, **dettagli):
    print(f"[{livello.upper()}]")
    
    # 1. Uniamo tutti i messaggi passati in *args usando il .join() che conosci!
    if messaggi:
        print(f"Messaggio: {' - '.join(messaggi)}")
    
    # 2. Stampiamo tutti i dettagli extra passati in **kwargs (dizionario)
    if dettagli:
        print("Dettagli Extra:")
        for chiave, valore in dettagli.items():
            print(f"  -> {chiave}: {valore}")
    print("-" * 20)

# Utilizzo 1: Solo livello e un messaggio
registra_evento("info", "Avvio del sistema completato")

# Utilizzo 2: Livello, più messaggi posizionali (*args) e dettagli con nome (**kwargs)
registra_evento(
    "errore", 
    "Connessione al database fallita", "Timeout dopo 30 secondi", # Finiscono in *args
    codice=500, utente="amministratore", ip="192.168.1.1"        # Finiscono in **kwargs
)

def crea_panino(tipo_pane, *ingredienti, **opzioni):
    # Scrivi qui il tuo codice per stampare il riepilogo del panino!
    #All'interno della funzione, prova a stampare un riepilogo del panino ordinato.
    print(f"Panino pronto con pane di tipo {tipo_pane}")
    if ingredienti:
        print("questi sono gli ingredienti:")
        print(f"{",".join(ingredienti)}")
    if opzioni:
        print("Hai scelto queste opzioni aggiuntive:")
        for chiave, valore in opzioni.items():
            print(f"  -> {chiave}: {valore}")
    print("-" * 20)
        

# Fai un test chiamando la funzione in questo modo:
crea_panino("Integrale", "Prosciutto", "Mozzarella", "Pomodoro", salsa="Maionese", tostato=True)
crea_panino("Con semi di sesamo", "Speck", "Brie", mozzarella="Bufala", asporto="Si")

#------------------FUNZIONI------------------------------
print("-" * 20)
#--------------------------

# PILA (LIFO)
# Last in first out
# l'ultimo che entra è il primo che esce
#
# In Python non serve una classe apposita: una normale lista si comporta
# già perfettamente come una pila, perché append() e pop() lavorano
# entrambi sull'ULTIMO elemento della lista.

p = [] #lista vuota
#append aggiunge alla fine
p.append("piatto1") #aggiunge alla fine
p.append("piatto2")
p.append("piatto3")
p.append("piatto4")

p.insert(1,"ciao") #inserisce nella posizione indicata dall'indice

print(p)

print("il primo elemento inserito al fondo della lista è:",p[0]) # restituisce il primo elemento, al fondo della pila
print("L'ultimo elemento inserito in cima alla lista è:",p[-1])  # restituisce l'ultimo elemento, in cima alla pila

print(f"elimino l'ultimo elemento inserito in cima alla lista {p[-1]}")
p.pop()  # rimuove l'elemento in cima alla pila (l'ultimo)

print(p)

print(f"elimino l'elemento indicato dall'indice o dal nome:")
p.remove(p[1]) #secondo elemento perchè parte da zero
#p.remove("ciao") #funziona sia con la posizione che col nome
print(p)

#---------------------------------------------------------
print("*"*30)
# Scrivere una Dictionary Comprehension che applica uno sconto del 10% solo ai prodotti che costano più di 2 euro.
prodotti = ["mela", "banana", "kiwi", "pitecantropo"]
prezzi = [1,2,3,4]
risultato= {prodotto: prezzo for prodotto, prezzo  in zip(prodotti, prezzi) if  prezzo> 2}
print(list(map(lambda x: x-x*.1,risultato.values())))

# Scrivere una Dictionary Comprehension che applica uno sconto del 10% solo ai prodotti che costano più di 2 euro.
risultato= {prodotto: prezzo-prezzo*.1  for prodotto, prezzo  in zip(prodotti, prezzi) if  prezzo> 2}
print(risultato)

# Se avessi voluto stampare il prezzo su una nuova riga, di conseguenza non avrei più accesso a prezzo e dovrei ricavarmelo in modo indipendente, giusto?

risultato= {prodotto: prezzo for prodotto, prezzo  in zip(prodotti, prezzi) if  prezzo> 2}
#prezzo su una nuova riga
print(list(map(lambda x: x-x*.1,risultato.values())))

'''
abbiamo visto che le [] sono liste, mentre () è un generatore.
ma come capire che si tratta di un generatore? le parentesi tonde () sono parte del comando join
'''
prodotti = ["mela", "banana", "kiwi", "pitecantropo"]
prezzi = [1,2,3,4]
risultato= {prodotto: prezzo for prodotto, prezzo  in zip(prodotti, prezzi) if  prezzo> 2}
# Creiamo una stringa unica dove ogni prezzo scontato è separato da un'andata a capo
stampa_prezzi = "\n".join(f"{prezzo * 0.9:.2f} €" for prezzo in risultato.values())
stampa_prezzi = list(prezzo * 0.9 for prezzo in risultato.values())
print(stampa_prezzi)

prodotti = ["mela", "banana", "kiwi", "pitecantropo"]
prezzi = [1, 2, 3, 4]

# Creiamo il nostro dizionario scontato
scontati = {prodotto: prezzo * 0.9 for prodotto, prezzo in zip(prodotti, prezzi) if prezzo > 2}
print(scontati)






a = "ciao a tutti"
for i in a:
    print(i)


frase = "Ciao a tutti oggi è una bella giornata"
numero_spazi = 0
for carattere in frase:
    if carattere == ' ':
        numero_spazi += 1
print("Spazi= " ,numero_spazi)

altezza = 175
# Assegnamento con operatore ternario
tipologia = "alto" if altezza >= 180 else "normale"
print(f"Tipologia altezza: {tipologia}")


altezza = 375
# Assegnamento con operatore ternario
print( "Tipologia altezza","alto" if altezza >= 180 else "normale")

from datetime import datetime
data_con_ora = datetime.now().weekday() #di nuovo tutta la data
print("Data con ora:", data_con_ora)

# Giorno della settimana
# datetime.now().isoweekday() restituisce un numero da 1 (Lunedì) a 7 (Domenica)
giorno = datetime.now().isoweekday()
giorno = datetime.now().weekday()  #inizia da 0  datetime.now().isoweekday() inizia da 1

print(f"Numero del giorno della settimana: {giorno}")

match giorno:
    case 0:
        print("Oggi è Lunedì")
    case 1:
        print("Oggi è Martedì")
    case 2:
        print("Oggi è Mercoledì")
    case 3:
        print("Oggi è Giovedì")
    case 4:
        print("Oggi è Venerdì")
    case 5:
        print("Oggi è Sabato")
    case 6:
        print("Oggi è Domenica")
    case _: # Il carattere '_' funge da 'default'
        print("Errore nella data")
        
print("*"*30)

#---Con if normale
print(giorno)
if giorno == 0:
    print("Oggi è Lunedì")
elif giorno == 1:
    print("Oggi è Martedì")
elif giorno == 2:
    print("Oggi è Mercoledì")
elif giorno == 3:
    print("Oggi è Giovedì")
elif giorno == 4:
    print("Oggi è Venerdì")
elif giorno == 5:
    print("Oggi è Sabato")
else:
    print("Oggi è Domenica")
    
    
a = 10
b = 20
max_uguali_str = (
    f"Il più grande è {a}" if a > b else
    "i numeri sono uguali" if a == b else
    f"Il più grande è {b}"
)
print(max_uguali_str)


# Prendiamo il dizionario dei prodotti scontati che abbiamo generato prima e salviamolo riga per riga in un file chiamato catalogo_scontato.txt.
prodotti = ["mela", "banana", "kiwi", "pitecantropo"]
prezzi = [1, 2, 3, 4]

# Creiamo il nostro dizionario scontato
scontati = {prodotto: prezzo * 0.9 for prodotto, prezzo in zip(prodotti, prezzi) if prezzo > 2}

# APRIAMO IL FILE IN MODALITÀ SCRITTURA ('w' sta per write)
with open("catalogo_scontato.txt", "w", encoding="utf-8") as file:
    for prodotto, prezzo_scontato in scontati.items():
        # Scriviamo una riga per ogni prodotto, aggiungendo il carattere andata a capo \n
        file.write(f"Prodotto: {prodotto} -> Prezzo Scontato: {prezzo_scontato:.2f}€\n")

print("File salvato con successo!")


#---------------------
#usare  .join() al posto del ciclo for
testo_da_salvare = "\n".join(f"{p}: {pr * 0.9:.2f}€" for p, pr in zip(prodotti, prezzi) if pr > 2)

with open("catalogo_veloce.txt", "w", encoding="utf-8") as file:
    file.write(testo_da_salvare)

#----Lettura file ---------

# Apriamo il file in modalità lettura ('r' è il comportamento predefinito)
with open("catalogo_scontato.txt", "r", encoding="utf-8") as file:
    for riga in file:
        # .strip() rimuove spazi extra e il carattere invisibile \n di fine riga
        print(riga.strip())

#--------------------------
#salvare di nuovo in una lista
with open("catalogo_scontato.txt", "r", encoding="utf-8") as file:
    righe_salvate = [riga.strip() for riga in file]

print(righe_salvate)
#-------------------------------------------------------------------------
import random

frase = "ciao a tutti"
parole_della_frase = frase.split(" ")  # lista di 3 elementi: ciao, a, tutti
print(parole_della_frase)

# Per tornare a una stringa unisci i caratteri con .join  -> "separatore".join(lista_da_unire)
nuova_stringa = " ".join(parole_della_frase)
print(nuova_stringa)  # Output: ciao a tutti

#posso scegliere il separatore che voglio
nuova_stringa = "*".join(parole_della_frase)
print(nuova_stringa)  # Output: ciao a tutti

nuova_stringa = "\n".join(parole_della_frase)
print(nuova_stringa)  # Output: ciao a tutti

# Se provi a fare: stringa[0] = "m" -> Python ti darà un ERRORE (TypeError)

# Soluzione con list():
# array_caratteri = list(stringa)  # Diventa ['c', 'i', 'a', 'o']
# array_caratteri[0] = "m"         # Modifica permessa! Diventa ['m', 'i', 'a', 'o']

tupla_colori = ("rosso", "verde", "blu")
#tupla_colori[0] = "nero"  # TypeError: 'tuple' object does not support item assignment
#-------------------------------------------------------------------
autori = {}

# libri degli autori
x = ["a", "b", "c"]  # libri dell'autore 1
y = ["d", "e", "f"]  # libri dell'autore 2
z = ["g", "h", "i"]  # libri dell'autore 3

autori["autore1"] = x
autori["autore2"] = y
autori["autore3"] = z

for autore in autori.keys():
    print("Autore:", autore, "Libri", autori[autore])
    
for autori, libri in autori.items():
    print("Autore:", autore,"\nlibri:",end=" ")
    for libro in libri:
        print(libro,end=" ")
    print()


#associare 2 liste
prodotti = ["mela", "banana", "kiwi", "pitecantropo"]
prezzi = [1,2,3,4]

dizionario=dict(zip(prodotti, prezzi))
print (dizionario)


#ritornare da dizionario alle 2 liste :

prodotti=list(dizionario) #ritorna le chiavi in modi predefinito
print(prodotti)
prezzi=list(dizionario.values()) #ritorna i valori
print(prezzi)

#------------------------------------------------------------------------
import random
a = [1, 2]
b = ["A", "B"]

risultato = [(x, y) for x in a for y in b] #2 elementi di a per 2 elementi di b = 4 combinazioni totali.Prodotto cartesiano
print(risultato) 

#oppure
risultato = [c+n for c in 'ABC' for n in '123']
print(risultato)  #['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

risultato = []
for c in 'ABC':
    for n in '123':
        risultato.append(c+n)
print(risultato) #['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

