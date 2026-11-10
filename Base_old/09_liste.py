import random

# NOTA (concetto senza equivalente diretto):
# in Java l'array ha dimensione FISSA: va dichiarata subito (new int[10])
# e non può più crescere né restringersi. Python non ha un tipo "array"
# di uso comune per i principianti: si usa la lista (list), che è invece
# dinamica per natura, può crescere e restringersi liberamente, e non
# richiede di indicare in anticipo quanti elementi conterrà.
# Le liste inoltre possono contenere elementi di tipo diverso (in Java
# invece tutti gli elementi dell'array devono essere dello stesso tipo).

un_array = [0] * 10  # creo una lista di 10 elementi, tutti inizializzati a 0

# primo elemento della lista
un_array[0] = 1
# secondo elemento della lista
un_array[1] = 2
# terzo elemento della lista
un_array[2] = 3

# se non specificato, gli altri elementi valgono 0 perché li ho inizializzati così

print(un_array[8])  # 0 perché non valorizzato
print(un_array[1])  # 2

note_musicali = [""] * 7

note_musicali[0] = "do"
note_musicali[1] = "re"
note_musicali[2] = "mi"
note_musicali[3] = "fa"
note_musicali[4] = "sol"
note_musicali[5] = "la"
note_musicali[6] = "si"

# NOTA: in Java la lunghezza di un array è una PROPRIETA' (array.length,
# senza parentesi). In Python è invece la FUNZIONE len(), che si può usare
# su liste, stringhe e altre sequenze.
lunghezza = len(note_musicali)
print(lunghezza)

parola = len("ciao")  # len() funziona anche sulle stringhe

# --sintassi alternativa: creare la lista già con i valori
#                     0         1        2        3
colori = ["bianco", "nero", "giallo", "blu"]

print(colori[2])  # giallo
# come visualizzo il penultimo elemento?

lungh = len(colori)

print(colori[lungh - 2])
# in Python c'è anche una scorciatoia con gli indici negativi:
print(colori[-2])  # stesso risultato, più idiomatico

# -------------------------------------------------

print(colori)
for i in range(len(colori)):
    print(i, colori[i])

# sintassi alternativa dove non uso l'indice (for-each)
for elemento in colori:
    print(elemento)

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

for i in range(len(giorni)):
    if giorni[i] == "venerdì" or giorni[i] == "sabato":
        print(giorni[i], "weekend")
    elif giorni[i] == "domenica":
        print(giorni[i], "relax")
    else:
        print(giorni[i], "lavoro")

for nome_giorno in giorni:
    if nome_giorno == "venerdì" or nome_giorno == "sabato":
        print(nome_giorno, "weekend")
    elif nome_giorno == "domenica":
        print(nome_giorno, "relax")
    else:
        print(nome_giorno, "lavoro")

# ---------------------------------------------
animali = ["cane", "gatto", "topo", "criceto", "pesce", "tricheco"]
piu_lunga = animali[0]  # lo decido io inizialmente, per avere un punto di partenza

for animale in animali:
    if len(animale) > len(piu_lunga):
        piu_lunga = animale
print("la più lunga è", piu_lunga)

# -----------------------------------------------------------------
# in Python le stringhe non sono array modificabili, ma SI POSSONO
# comunque scorrere carattere per carattere con un for, perché sono
# comunque una sequenza.
parola2 = "ciao"
lista_caratteri = list(parola2)  # trasforma la stringa in una lista di caratteri

for lettera in lista_caratteri:
    print(lettera)

# in Python, a differenza di Java, l'accesso diretto con l'indice
# funziona già sulla stringa stessa, senza doverla prima convertire:
print(parola2[0])  # 'c' -- qui invece funziona, a differenza di Java

# ho creato una lista a partire da una stringa
frase = "ciao a tutti"
parole_della_frase = frase.split(" ")  # lista di 3 elementi: ciao, a, tutti
for pezzo in parole_della_frase:
    print(pezzo)

# ---------------------------------------------------------
numeri = [4, 2, 1, 3]
# in Python basta usare direttamente print() per vedere il contenuto di una
# lista: non serve una classe di utilità come Arrays in Java.
print(numeri)

# ----------------------------------------------------------
# lista di numeri casuali
arr_casuali = [0] * 10

for i in range(len(arr_casuali)):
    arr_casuali[i] = random.randint(0, 100)  # popolo la lista con valori casuali da 0 a 100

for valore in arr_casuali:
    print(valore)

print(arr_casuali)
# --------------------------------------------------------

# quanti = int(input("quanti numeri vuoi avere? "))  # numero di elementi nella lista
#
# valori = [0] * quanti  # creo la lista della dimensione scelta dall'utente
# for i in range(len(valori)):
#     print("inserisci l'elemento alla posizione", i)
#     valori[i] = int(input())  # l'utente inserisce i valori in base all'indice
# -----------------------------------------------------------
# qui abbiamo la lista con gli elementi
#
# print("gli elementi della lista sono:")
# for elemento in valori:
#     print(elemento)
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
# liste multidimensionali (lista di liste)
arr_multi = [
    [1, 2, 3],  # posizione 0
    [4, 5, 6],  # posizione 1
]

print(arr_multi[0][1])  # stampa 2
print(arr_multi[1][2])  # stampa 6

# stesso esempio con altra sintassi: creo prima la struttura vuota e poi la riempio
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
print(arr_multi)
# ----------------------------------------------------

xy = [0] * 3
xy[0] = 99
xy[1] = 55
xy[2] = 33

for i in range(len(xy)):
    print(xy[i])

for valore in xy:
    print(valore)

frutti = ["banane", "arance", "limoni", "lamponi"]
verdure = ["carote", "piselli", "pomodori", "insalata"]

#                     0        1
vegetali = [frutti, verdure]  # lista di 2 liste da 4 elementi

for riga in vegetali:
    for elemento in riga:
        print(elemento)

# --------------------------------------------------------------

numerix = [0] * 8
print("inserisci 8 numeri >0")
num_utente = 0
num_errori = 0

contatore = 0
while True:
    if contatore == 8:
        break
    num_utente = int(input())
    if num_utente <= 0:
        print("ti ho detto >0")
        num_errori += 1
    else:
        numerix[contatore] = num_utente
        contatore += 1

print(numerix, "Errori:", num_errori)
