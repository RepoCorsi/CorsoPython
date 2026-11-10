# Python usa la lista [], che è dinamica per natura, può crescere e restringersi liberamente, e non
# richiede di indicare in anticipo quanti elementi conterrà.
# Le liste possono contenere elementi di tipo diverso.

#con le () invece è una tupla NON MODIFICABILE. Le insegno dopo. Non trattarle adesso.

'''
colori = ["rosso", "verde", "blu", "giallo"] (con le parentesi quadre) è una LISTA. Le liste sono mutabili: significa che dopo averle create puoi modificarle, cioè puoi aggiungere, rimuovere o cambiare gli elementi al loro interno.

colori = ("rosso", "verde", "blu", "giallo") (con le parentesi tonde) è una TUPLA. Le tuple sono immutabili: una volta create, non puoi più modificarle in alcun modo. Non puoi aggiungere nuovi colori, non puoi cancellarne e non puoi cambiare l'ordine.
'''

#           0        1        2        3
colori = ["rosso", "verde", "giallo", "blu"]
print(colori)

print(colori[2]) # giallo

lunghezza = len(colori)
print(lunghezza)

print(colori[lunghezza - 1]) #ultimo blu
print(colori[-2]) # penultimo - più da python

# for-each, senza indice
for colore in colori:  
    print(colore)

 #leggere gli elementi con indice. Range vuole solo numeri
for i in range(len(colori)):
    colore = colori[i]
    print(i,colore)

#modifico un colore
colori[2]="bianco"
print(colori)
#--------------------------------------------------------------
# un colore a caso:
import random

colore_scelto = random.choice(colori) # Estrae un elemento a caso
print(colore_scelto)  # Es. "verde"

#con indice e random.range() estremo superiore non incluso
# Genera un indice da 0 a 3 (il 4 è escluso)
indice_casuale = random.randrange(0, len(colori)) #0 - 3

colore_scelto = colori[indice_casuale]
print(colore_scelto, "si trova all'indice ",indice_casuale)

#-------------------------------------------------
#cercare un elemento nella lista:

if "rosso" in colori:
    print("rosso è presente nella lista")
else:
    print("rosso non è presente")
    
#--------------------------
#Trovare la posizione esatta con .index()
if "rosso" in colori:
    posizione = colori.index("rosso")
    print(f"Rosso si trova all'indice: {posizione}")  # Output: 0

#--------------------
#Contare le occorrenze con .count()
colori = ["rosso", "verde", "rosso", "blu"]

quanti_rossi = colori.count("rosso")
print(f"Il rosso appare {quanti_rossi} volte.")  # Output: 2
#----------------------
# Aggiungere un elemento al fondo della lista:
colori.append("nero")
print(colori)

# inserisce un valore ad una posizione specificata
colori.insert(3, "bianco")
print(colori)

# rimuove un elemento
colori.remove("bianco")  
print(colori)

# rimuove il valore dalla posizione indicata
colori.pop(3)  
print(colori)

# visualizza la lista in ordine alfabetico o numerico
colori.sort()  
print(colori)

# visualizza la lista al contrario
colori.reverse()  
print(colori)

#SLICING
print(colori[1:3]) # dalla pos 1 alla 2 -> "rosso", "nero"

# Aggiunge una lista ad un'altra lista
colori.extend(["nero","verde","blu"])
print(colori)

# rimuove tutti gli elementi della lista
colori.clear() 
print(colori)

#-----------------------------------------
#Lista di numeri
una_lista = [0] * 10  # creo una lista di 10 elementi, tutti inizializzati a 0
print(una_lista)
# primo elemento della lista
una_lista[0] = 1
# secondo elemento della lista
una_lista[1] = 2
# terzo elemento della lista
una_lista[2] = 3

# se non specificato, gli altri elementi valgono 0 perché li ho inizializzati così

print(una_lista[8])  # 0 perché non valorizzato
print(una_lista[1])  # 2

#-------------------------------------------------
note_musicali = [""] * 7

note_musicali[0] = "do"
note_musicali[1] = "re"
note_musicali[2] = "mi"
note_musicali[3] = "fa"
note_musicali[4] = "sol"
note_musicali[5] = "la"
note_musicali[6] = "si"

print(note_musicali)
# In Python la funzione len(), si può usare
# su liste, stringhe e altre sequenze.
lunghezza = len(note_musicali)
print(lunghezza)

#-----------------------------------------------
# creo una lista e la riempo con valori da 0 a 4
arr = [0] * 5
for i in range(len(arr)):
    arr[i] = i  # 0--4

# stampo con indice
for i in range(len(arr)):
    print(arr[i])

# stampo col for senza indice (for-each)
for numero in arr:
    print(numero)

# ////////////////////////////////////////////////////////////
giorni = ["lunedi", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]

#con indice
for i in range(len(giorni)):
    if giorni[i] == "venerdì" or giorni[i] == "sabato":
        print(giorni[i], "weekend")
    elif giorni[i] == "domenica":
        print(giorni[i], "relax")
    else:
        print(giorni[i], "lavoro")
print("*"*30)

#senza indice
for nome_giorno in giorni:
    if nome_giorno in ("venerdì", "sabato"):
        print(nome_giorno, "weekend")
    elif nome_giorno == "domenica":
        print(nome_giorno, "relax")
    else:
        print(nome_giorno, "lavoro")

# ---------------------------------------------
#più lunga
animali = ["cane", "gatto", "topo", "criceto", "pesce", "tricheco"]
piu_lunga = animali[0]  # lo decido io inizialmente, per avere un punto di partenza

for animale in animali:
    if len(animale) > len(piu_lunga):
        piu_lunga = animale
print("la più lunga è", piu_lunga)

# -----------------------------------------------------------------
# confronto tra 2 liste:  con ==
vegetali = ["lattuga","spinaci","zucchine"]
print(animali==vegetali) #False


#Abbiamo già la lista animali...
print("cicla al contrario con reversed")
for elementi in reversed(animali):
    print(elementi)

print("cicla in ordine alfabetico")
for elementi in sorted(animali):
    print(elementi)

print("stampa anche l'indice con enumerate:")
for i, v in enumerate(animali):
    print(i,v)

#per le liste è sempre possibile usare questi metodi:
numeri = [6,3,2,1,5,4]
lunghezza = len(numeri)
minimo = min(numeri)
massimo = max(numeri)
somma = sum(numeri)
ordina = sorted(numeri) #restituisce direttamente una nuova lista già pronta e formattata.
contrario = list(reversed(numeri)) #restituisce un oggetto, quindi ci va list.
#Altrimenti usare CONTRARIO = NUMERI[::-1] 

print(lunghezza,minimo,massimo,somma,ordina,contrario)


#-------------------------------
print("si può ciclare con 2 o più sequenze contemporaneamente:")#vale per tutti i tipi di liste
lista1 = ['nome', 'eta', 'colore preferito:']
lista2 = ['fabio', 43, 'blu']

#zip associa un elemento di una lista all'elemento corrispondente dell'altra lista
for s1,s2 in zip(lista1,lista2):
    print(f"tuo {s1}? è {s2}")

#----------------------------------
# in Python le stringhe non sono array modificabili, ma SI POSSONO
# comunque scorrere carattere per carattere con un for, perché sono comunque una sequenza.
parola2 = "ciao"
print(parola2[0])  
# Esempio: voglio cambiare la prima lettera di "ciao" in "M" per farlo diventare "miao".

# Se provi a fare: parola2[0] = "m" -> Python ti darà un ERRORE 
#parola2[0] = "m" #NO! ERRORE

#Allora trasformiamo la stringa in lista:
lista_caratteri = list(parola2)  # list trasforma la stringa in una lista di caratteri ['c', 'i', 'a', 'o']
print(lista_caratteri)

#Adesso possiamo modificare la prima lettera
lista_caratteri[0]="m"
print(lista_caratteri)

#cicliamo sulle lettere
for lettera in lista_caratteri:
    print(lettera)
    
#-----------------------------------------------

# Creare una lista a partire da un separatore di stringhe
frase = "ciao a tutti"
parole_della_frase = frase.split(" ")  # lista di 3 elementi: ciao, a, tutti
print(parole_della_frase)

# Per tornare a una stringa unisci i caratteri con .join  -> "collante".join(lista_da_unire)
nuova_stringa = " ".join(parole_della_frase)
print(nuova_stringa)  # Output: ciao a tutti

#posso scegliere il collante che voglio
nuova_stringa = "*".join(parole_della_frase)
print(nuova_stringa)  # Output: ciao*a*tutti

#andare a capo
nuova_stringa = "\n".join(parole_della_frase)
print(nuova_stringa)  # Output: ciao a tutti a capo

#-------------------
ingredienti = ["pomodoro", "mozzarella", "basilico"]

# Uniamo gli elementi usando una virgola e uno spazio ", "
lista_spesa = ", ".join(ingredienti)

print(lista_spesa)  # Output: pomodoro, mozzarella, basilico

# Il metodo .join() fa esattamente il lavoro opposto di list(): prende una lista (o qualsiasi sequenza) di stringhe e le unisce per formare un'unica stringa.

# .join() funziona solo se tutti gli elementi della lista sono stringhe. Se nella lista ci sono numeri (interi o decimali), Python restituirà un errore (TypeError).
# Se hai una lista mista o di soli numeri, devi prima convertirli in stringhe
#--
citta = ["Roma", "Milano", "Napoli"]
elenco_verticale = "\n".join(citta)
print(elenco_verticale)
#--------------------------------------
# Immagina di voler nascondere tutte le vocali di una parola sostituendole con un asterisco *.

parola = "segreto"
lettere = list(parola)  # ['s', 'e', 'g', 'r', 'e', 't', 'o']

# Cicliamo sulla lista usando l'indice per poter modificare la lettera sul posto
for i in range(len(lettere)):
    if lettere[i] in "aeiou":
        lettere[i] = "*"  # Modifica permessa perché è una lista!

# Ricostruiamo la stringa
parola_censurata = "".join(lettere)

print(parola_censurata)  # Output: s*gr*t*



#----------------------------------------
# In Python str.split() prende un separatore LETTERALE "*" 
str2 = "ciao*come*stai"
arr_of_str2 = str2.split("*")
for a in arr_of_str2:
    print(a)

#import re
# str3 = "parola1,parola2 parola3@parola4?parola5.parola6"
# arr_of_str3 = re.split("[, ?.@]", str3)
# for a in arr_of_str3:
    # print(a)
#------------------------------------------------------
#Con SLICING [inizio:fine]

altri_numeri = [3, 6, 9, 12, 1, 4, 21, 7]
print(altri_numeri)
altri_numeri[2:6] = [10] * 4 #riempie con 4 10 dalla posizione 2 alla 5 (estremo escluso)
print(altri_numeri) #[3, 6, 10, 10, 10, 10, 21, 7]
#--------
# copia di una parte della lista: lo slicing [inizio:fine]
parte_dei_numeri = altri_numeri[2:6] #dalla pos 2 alla posizione 5
print(parte_dei_numeri) # [10, 10, 10,10]

# ----------------------------------------------------------
# lista di numeri casuali
arr_casuali = [0] * 10 #10 elementi tutti a 0

for i in range(len(arr_casuali)):
    arr_casuali[i] = random.randint(0, 100)  # popolo la lista con valori casuali da 0 a 100

for valore in arr_casuali:
    print(valore)

print(arr_casuali)
# --------------------------------------------------------
#Chiede all'utente la dimensione della lista e inserisce i valori
quanti = int(input("quanti numeri vuoi avere? "))  # numero di elementi nella lista

valori = [0] * quanti  # creo la lista della dimensione scelta dall'utente
for i in range(len(valori)):
    print("inserisci l'elemento alla posizione", i)
    valori[i] = int(input())  # l'utente inserisce i valori in base all'indice
-----------------------------------------------------------
#qui abbiamo la lista con gli elementi

print("gli elementi della lista sono:")
for elemento in valori:
    print(elemento)
# ----------------------------------------------------------
# selection sort
# confrontare ogni valore col successivo: se è più piccolo lo sposta, lo mette prima
#
# for i in range(len(valori)):  # ogni valore
#     for j in range(len(valori)):  # lo confronto con tutti gli altri
#         if valori[i] < valori[j]:  # se è più piccolo
#             valori[i], valori[j] = valori[j], valori[i]  # li scambio
#             # NOTA: Python permette di scambiare 2 valori in una riga sola,
#             # senza bisogno di una variabile temporanea come in Java
# print("lista ordinata")
# print(valori)

# --------------------------------------------------------
# In Python una lista può contenere elementi di tipo diverso, senza bisogno di dichiarare nulla.
misto = [True, "Fragola", 123,3.14]
print(misto)

#-----------------------------------------------
# liste multidimensionali (lista di liste)
arr_multi = [
    [1, 2, 3],  # posizione 0
    [4, 5, 6],  # posizione 1
]

# stampo con print() direttamente
print(arr_multi)

print(arr_multi[0][1])  # stampa 2
print(arr_multi[1][2])  # stampa 6

# stampo la lista multiplo
for riga in arr_multi:
    for valore in riga:
        print(valore, end="")
    print()  # vado a capo dopo ogni riga


# stesso esempio con altra sintassi: creo prima la struttura vuota e poi la riempo
multiplo = [[0, 0, 0], [0, 0, 0]]
multiplo[0][0] = 1
multiplo[0][1] = 2
multiplo[0][2] = 3
multiplo[1][0] = 4
multiplo[1][1] = 5
multiplo[1][2] = 6

# stampo la lista multiplo
for riga in multiplo:
    for valore in riga:
        print(valore, end="")
    print()  # vado a capo dopo ogni riga

# stampo con print() direttamente
print(multiplo)
# ----------------------------------------------------

print("")

arr_multi2 = [
    ["mario", "rossi"], #0
    ["giuseppe", "verdi"], #1
    ["ugo", "bianchi"], #2
]

print(arr_multi2[1][1]) #verdi
print(arr_multi2[2][0]) #ugo

for persone in arr_multi2:
    for elementi in persone:
        print(elementi, end=" ")
    print("")

#---------------------------------
# array multiplo a partire da array esistenti
frutti = ["banane", "arance", "limoni", "lamponi"]
verdure = ["carote", "piselli", "pomodori", "insalata"]

#              0        1
vegetali = [frutti, verdure]  # lista da 2 liste da 4 elementi

print(vegetali)

print(vegetali[1][2]) #pomodori
print(vegetali[0][3]) #lamponi

for riga in vegetali:
    for elemento in riga:
        print(elemento)

#-----------------------------------------------
## ------- TUPLE ------------------------------
#-------------------------------------------------

# Una tupla è identificata dalla parentesi tonda, e ammette valori di diverso tipo, anche duplicati.
# NON é MODIFICABILE!! si può solo visualizzare e NON MODIFICARE O AGGIUNGERE ELEMENTI.
# Le tuple sono immutabili: una volta create, non puoi più modificarle in alcun modo. Non puoi aggiungere nuovi elementi, non puoi cancellarne e non puoi cambiare l'ordine.

# Più veloce, da usare solo quando non dobbiamo modificare la lista

# SOLO 2 METODI PERMESSI:
# 1. COUNT(valore) 
# 2. INDEX(valore) cerca il valore e ritorna la posizione
# Se non c'è errore!
numeri=(1,2,3,2,4,2)

#count
conteggio=numeri.count(2) #quanti 2?
print(conteggio) #3

#index
lettere=('a','b','c','d')
posizione=lettere.index('c') #posizione lettera c
print(posizione) #2

#--------------------------------------------------
#trasformare da lista in tupla e viceversa
# La nostra lista di partenza
lista_originale = ["FIFA", "Zelda", "GTA"]
print(type(lista_originale)) # Output: <class 'list'>

# 1. Da LISTA a TUPLA
mia_tupla = tuple(lista_originale)
print(mia_tupla)             # Output: ('FIFA', 'Zelda', 'GTA') - Notare le parentesi tonde
print(type(mia_tupla))       # Output: <class 'tuple'>

# 2. Da TUPLA a LISTA
nuova_lista = list(mia_tupla)
print(nuova_lista)           # Output: ['FIFA', 'Zelda', 'GTA'] - Notare le parentesi quadre
print(type(nuova_lista))     # Output: <class 'list'>

#-----------------------------------------------

# 1. Lista di Tuple: Registro dei Clienti (Database)

# Struttura: [(...), (...)]

#È una lista (modificabile) che contiene all'interno delle tuple (immutabili).
#Viene usata per gestire i database (ogni tupla è una riga/record della tabella). Puoi aggiungere o togliere righe alla lista, ma le singole righe sono protette e fisse

# Una lista (modificabile) di record-clienti (immutabili)
prenotazioni = [
    ("Marco Rossi", 4, "20:30"), #nome, tavolo, ora prenotazione
    ("Anna Bianchi", 2, "21:00"),
    ("Luca Verdi", 6, "19:45")
]

# Puoi modificare il contenitore esterno: aggiungi una nuova prenotazione
prenotazioni.append(("Sofia Neri", 3, "21:15"))

# Non puoi modificare il contenuto interno di una prenotazione:
# prenotazioni[0][1] = 5  <-- ERRORE: non puoi cambiare il tavolo direttamente sulla tupla

print("Lista delle prenotazioni della serata:")
print(prenotazioni)

#-------------------


# 2. Tupla di Liste: Coordinate GPS di un Percorso di Consegna

# Struttura: ([ ... ], [ ... ])

#La struttura esterna è congelata (non puoi aggiungere o rimuovere le liste all'interno), ma il contenuto interno delle singole liste può essere liberamente modificato

# Una tupla fissa di 2 elementi (Partenza e Arrivo), ma le coordinate dentro sono liste modificabili
percorso_consegna = (
    [45.0703, 7.6869],  # Lista 1: Coordinate attuali del punto di partenza (Torino)
    [45.4642, 9.1900]   # Lista 2: Coordinate attuali del punto di arrivo (Milano)
)
print(percorso_consegna)
# La struttura è bloccata: non puoi aggiungere una terza tappa intermedia alla tupla
# percorso_consegna.append([41.9028, 12.4964]) <-- ERRORE

# Il contenuto è modificabile: il GPS corregge leggermente la latitudine di partenza
percorso_consegna[0][0] = 45.0715 

print("\nTupla di liste (Coordinate GPS aggiornate):")
print(percorso_consegna)
# Output: ([45.0715, 7.6869], [45.4642, 9.1900])



# In sintesi:

# • Usi la lista di tuple quando hai un elenco di elementi che cresce o diminuisce nel tempo (es. passeggeri di un volo, prodotti nel carrello), ma ogni elemento ha dati che non devono essere pasticciati.
# • Usi la tupla di liste quando lo schema esterno è rigido e ha un significato fisso (es. coordinate X e Y, valori Minimi e Massimi, Primo tempo e Secondo tempo), ma i dati dentro quelle categorie si evolvono continuamente.

#--------------------------------------------------------------
# Esercizio da far fare
# programma che chiede all'utente di inserire dei numeri e li mette in una lista
# fino a quando l'utente non inserisce -1
# mostra tutti i valori e calcola la somma

numeri = []
somma = 0


while True:
    print("inserisci un numero, -1 per terminare")
    numero = int(input())
    if numero == -1:
        break
    else:
        numeri.append(numero)
        somma += numero

print(numeri)  # stampa la lista numeri
print("la somma è", somma)

