# NOTA GENERALE: il "for" di Java è composto da 3 parti esplicite
# (inizializzazione; condizione; incremento). Il "for" di Python è invece
# un "for-each": scorre sempre gli elementi di una sequenza (una lista,
# una stringa, oppure una sequenza di numeri generata da range()).
# Per riprodurre il comportamento del for numerico di Java si usa quasi
# sempre range().

# inizializzazione: range(10) parte da 0; la fa 1 sola volta
# condizione di permanenza nel ciclo: range(10) si ferma prima di arrivare a 10
# incremento: range() di default aumenta di 1 ad ogni passo
# for i in range(10):
#     print(i, "ciao")
# --------------------------------------
# al contrario (range con passo -1)
# for i in range(10, 0, -1):
#     print(i, "ciao")
# ----------------------------------------------

# 0-->10 solo i pari (range con passo 2)
# for i in range(0, 11, 2):
#     print(i)
# --------------------------------------------------
# caratteri stampabili della tabella ascii
# for i in range(32, 127):
#     print(i, ":", chr(i))

# ---------------------------------------------
# NOTA (concetto senza equivalente diretto):
# in Java il "for destrutturato" permette di scrivere un for senza una o più
# delle sue 3 parti (ad esempio senza incremento nelle parentesi). In Python
# questo non è possibile: il for non ha una sintassi "a parti separate".
# Quando serve un controllo più libero sul ciclo, in Python si usa un
# semplice while.
# contatore = 0  # inizializzazione
# while contatore < 10:  # condizione
#     print(contatore)
#     contatore += 1  # incremento

# ------------------------------------------------------
# NOTA (concetto senza equivalente diretto):
# in Java si possono gestire più variabili di ciclo insieme nello stesso for
# (i che sale, j che scende). Python non lo permette nel for: si può ottenere
# lo stesso risultato con un while.
# i = 0
# j = 10
# while i < 10:
#     print("i=", i, "j=", j)
#     i += 1
#     j -= 1
# --------------------------------------------------
#
# a = "ciao a tutti"
# for i in range(len(a)):
#     print(a[i])  # in Python l'accesso a un singolo carattere si fa con
#                  # le parentesi quadre, non con un metodo come charAt()
# -----------------------------------
#
# numero_spazi = 0
# for i in range(len(a)):
#     if a[i] == ' ':
#         numero_spazi += 1
# print("spazi=", numero_spazi)

import random

# boolean trovato = False  # stato iniziale
#
# casuale = random.randint(1, 20)  # 1 a 20
# print("il numero casuale è", casuale)
#
# trovato = False
# i = 1
# while i <= 10 and not trovato:
#     if casuale == i:
#         trovato = True
#         print("l'ho trovato in posizione", i)
#         # break
#     i += 1
#
# if not trovato:
#     print("non ho trovato il numero")

# ---------------------------------------------------------------------

# tabellina (ciclo annidato): per ogni valore di i....
# for i in range(1, 11):
#     for j in range(1, 11):  # lo moltiplico per il valore di j
#         print(i * j, end="\t")
#     print()

for i in range(5):
    print("ciclo esterno")
    for j in range(3):
        print("\t ciclo interno")

# --------------------------------------------------------------------

# for destrutturato (vedi nota sopra)
# contatore = 0  # inizializzazione
# while contatore < 10:  # condizione
#     print(contatore)
#     contatore += 1  # incremento

# contatore = 10  # inizializzazione
# while contatore < 10:  # condizione
#     print(contatore)
#     contatore += 1  # incremento
#
# NOTA (concetto senza equivalente diretto):
# Java ha anche il ciclo do-while, che esegue il corpo ALMENO una volta
# e controlla la condizione solo alla fine. Python non ha un do-while.
# L'idioma più comune per riprodurlo è un "while True" con un controllo
# e un "break" alla fine del corpo:
# while True:
#     print(contatore)
#     contatore += 1
#     if contatore >= 10:
#         break

# print("inserisci un valore, metti 0 per uscire")
# valore = int(input())
# while valore != 0:
#     print("inserisci un valore, metti 0 per uscire")
#     valore = int(input())
#
# (versione "do-while" con l'idioma while True + break)
# while True:
#     print("inserisci un valore, metti 0 per uscire")
#     valore = int(input())
#     if valore == 0:
#         break

# -------------------------------------------------
# lettera = 'a'
# while lettera <= 'z':
#     print(lettera)
#     lettera = chr(ord(lettera) + 1)  # in Python il carattere non si
#                                       # incrementa direttamente: bisogna
#                                       # passare dal codice numerico

# ---------------------------------------------------
# vocali = 0
# consonanti = 0
#
# for codice in range(ord('a'), ord('z') + 1):
#     lettera = chr(codice)
#     # NOTA: Java può usare uno switch con più valori nello stesso case
#     # (case 'a','e','i','o','u':). In Python la scelta idiomatica per
#     # verificare l'appartenenza a un gruppo di valori è l'operatore "in".
#     if lettera in ('a', 'e', 'i', 'o', 'u'):
#         print(lettera, "è una vocale")
#         vocali += 1
#     else:
#         print(lettera, "è una consonante")
#         consonanti += 1
#
# print("vocali", vocali, "consonanti", consonanti)
# -----------------------------------------------------------------

# for i in range(10):
#     if i == 5:
#         continue  # salta un giro
#     if i == 7:
#         break
#     print(i)

# ----------------------------------------
# ciclo infinito col while
# while True:
#     print("inserisci un numero, 7 per uscire")
#     numero = int(input())
#     print("hai inserito", numero)
#     if numero == 7:
#         print("ciao")
#         break
#
# NOTA (concetto senza equivalente diretto):
# Java ha anche il for infinito scritto come for(;;). Python non ha una
# sintassi equivalente per il for: un ciclo infinito si scrive sempre con
# "while True".
# val = 0
# while True:
#     print(val)
#     if val == 10:
#         break
#     val += 1

# for i in range(10):
#     print(i)
#
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i >= 10:
#         break
