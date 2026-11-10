import random
from datetime import datetime

# print("inserisci la tua età")
# eta = int(input())
#
# # > < >= <= == != diverso
#
# # condizione da controllare, di tipo booleano (True/False)
# if eta >= 18:  # parte vera
#     # se il controllo è vero
#     print("sei maggiorenne puoi entrare")
# else:  # parte falsa
#     # entra qui solo se il controllo è falso
#     print("non sei maggiorenne non puoi entrare")
# ---------------------------------------------------
num = 2
# condizione
if num > 5:
    # se è vero che è >5
    print("il numero è maggiore di 5")
elif num == 5:
    print("il numero è uguale a 5")
else:
    print("il numero è < di 5")

# ------------------------------------------------------
# print("inserisci la temperatura")
# temperatura = int(input())
#
# if temperatura > 30:
#     print("accendi condizionatore")
# elif temperatura < 17:
#     print("accendi il riscaldamento")
# else:  # l'ultima cosa che si mette
#     print("si sta bene")

# ----------------------------------------------
# print("inserisci il primo numero")
# num1 = int(input())
# print("inserisci il secondo numero")
# num2 = int(input())
#
# if num2 != 0:
#     # faccio la divisione solo se il numero è diverso da 0
#     print("la divisione è", num1 // num2)
#     print("il resto è", num1 % num2)  # % operatore modulo
# else:
#     print("Errore: Non puoi dividere per zero")

num3 = 10
if num3 % 2 == 0:  # % restituisce il resto della divisione
    print("il numero è pari")
else:
    print("il numero è dispari")

# ------------------------------------------------------------
orario = datetime.now().hour  # qui ricavo l'ora

# il primo ramo vero che trova esce
if orario < 12:
    saluto = "Buon giorno"
elif orario < 18:
    saluto = "buon pomeriggio"
elif orario < 22:
    saluto = "Buona sera"
else:
    saluto = "Buona notte"
print(saluto)
# -----------------------------------------------------------------

# print("Inserisci una parola")
# parola = input()
#
# lunghezza = len(parola)  # quante lettere ha la parola
# if lunghezza % 2 == 0:
#     print("la parola ha un numero pari di lettere")
# else:
#     print("la parola ha un numero dispari di lettere")

sole = False
temperatura = 25
# esco solo se c'è una temperatura >20 e c'è il sole
# operatori logici: "and" al posto di &&, "or" al posto di ||
if sole and temperatura > 20:  # "and" richiede che siano vere entrambe le condizioni
    print("esco")
else:  # non esco
    print("Sto a casa")

# "or" basta che ce ne sia solo 1 vera perché tutto diventi vero
if sole or temperatura > 20:
    print("esco")
else:
    print("sto a casa")
# -----------------------------------------------------------------------
voto1 = 6
voto2 = 5
voto3 = 6

# "and" ha la priorità su "or", esattamente come in Java
# se voglio cambiare la priorità metto le parentesi ()

if voto1 >= 6 and (voto2 >= 6 or voto3 >= 6):
    print("promosso")
else:
    print("bocciato")

voto4 = 8
if voto4 >= 6:
    print("promosso")
else:
    print("bocciato")

# operatore ternario: Java lo scrive come condizione ? valoreSeVero : valoreSeFalso
# in Python la stessa cosa si scrive come: valoreSeVero if condizione else valoreSeFalso
print("promosso" if voto4 >= 6 else "bocciato")

altezza = 120
tipologia = "alto" if altezza > 180 else "normale"
print(tipologia)

if altezza > 180:
    print("alto")
else:
    print("normale")

# ------------------------------------------------------
a = 10
b = 10

massimo = a if a > b else b
print("il maggiore è", massimo)

if a > b:
    massimo = a
else:
    massimo = b

print("il maggiore è", massimo)

# in Python il ternario si può concatenare come in Java, ma diventa poco
# leggibile: qui, come nel materiale originale, va usato con moderazione
max_o_uguale = ("il più grande è " + str(a) if a > b
                 else "i numeri sono uguali" if a == b
                 else "il più grande è " + str(b))

print(max_o_uguale)

if a > b:
    print("il più grande è", a)
elif a == b:
    print("i numeri sono uguali")
else:
    print("il più grande è", b)

# --------------------------------------------------------------------
# NOTA (concetto senza equivalente diretto):
# in Java lo switch classico funziona solo con numeri interi, char e
# String (non con boolean, double, float). Python non ha uno switch
# "storico": per un principiante, la scelta idiomatica è sempre if/elif/
# else, che funziona con qualunque tipo di condizione, comprese quelle
# che in Java sarebbero vietate nello switch.
i = 0
if i == 0:  # if
    print("i è uguale a 0")
elif i == 1:  # else if
    print("i vale 1")
elif i == 2:  # else if
    print("i vale 2")
else:  # else
    print("i è diverso da 0,1,2")

# il numero del giorno della settimana: 1 = lunedì ... 7 = domenica
giorno = datetime.now().isoweekday()
print(giorno)

if giorno == 1:
    print("oggi è lunedì")
elif giorno == 2:
    print("oggi è martedì")
elif giorno == 3:
    print("oggi è mercoledì")
elif giorno == 4:
    print("oggi è giovedì")
elif giorno == 5:
    print("oggi è venerdì")
elif giorno == 6:
    print("oggi è sabato")
elif giorno == 7:
    print("oggi è domenica")
else:
    print("errore nella scelta del giorno")

# ---------------------------------------------------
# "switch sequenziali": in Java si scrivono più case di seguito senza
# codice in mezzo, per farli condividere la stessa istruzione finale.
# In Python l'equivalente idiomatico è controllare l'appartenenza a un
# gruppo di valori con l'operatore "in".
lettera = "x"
if lettera in ("a", "e", "i", "o", "u"):
    print(lettera, "è una vocale")
else:
    print(lettera, "è una consonante")

# --------------------------------------------------
# NOTA: Java (dalla versione 14) ha anche una forma più moderna di switch,
# con la freccia "->" al posto di "case: ... break;", che può anche
# restituire direttamente un valore da assegnare a una variabile.
# In Python questo secondo comportamento (uno switch che produce un
# valore) si ottiene di nuovo con l'espressione ternaria if/else, non con
# uno switch, perché Python non ha una parola chiave "switch".
messaggio = (lettera + " è una vocale" if lettera in ("a", "e", "i", "o", "u")
             else lettera + " è una consonante")

print(messaggio)

# ---------------------------------------------------
# chiedere all'utente 2 numeri a, b
# stampare 1 se a è maggiore di b
# stampare 2 se a è uguale a b
# altrimenti stampare 3

print("inserisci il primo numero")
a1 = int(input())
print("inserisci il secondo numero")
b1 = int(input())

if a1 > b1:
    c = 1
elif a1 == b1:
    c = 2
else:
    c = 3

print(c)
# ------------------------------------

# ***************************** ESERCIZI: *****************************

# ********************* 1) BMI (BODY MASS INDEX) ************************
# Si scriva un programma che chiede all'utente peso e altezza e calcola
# il BMI e indichi se la persona è nella norma, sovrappeso o sottopeso.
# BMI = peso / (Altezza * Altezza)  (altezza in metri)
# Un BMI da 20 a 25 è considerato "nella norma".

# -------------------------------------------------------------------------
# ********************* 2) Morra cinese (Carta forbice sasso) ***************
# Realizzare un programma che permetta di giocare alla morra cinese contro
# il computer.

numero_pc = random.randint(0, 2)  # da 0 a 2

if numero_pc == 0:
    computer = "f"
elif numero_pc == 1:
    computer = "s"
else:
    computer = "c"

print("inserisci f,s,c")

giocatore = input().lower()

print("tu:", giocatore, "pc:", computer)

vittoria = (
    (giocatore == "s" and computer == "f")
    or (giocatore == "f" and computer == "c")
    or (giocatore == "c" and computer == "s")
)

if computer == giocatore:
    print("parità")
elif vittoria:
    print("hai vinto")
else:
    print("hai perso")

# -----------------------------------------------------------------------------

# ********************* 3) Calcolatrice ***************************
# Realizzare con lo SWITCH (in Python: con if/elif) un programma che
# chiede all'utente 2 numeri e l'operazione da eseguire sui 2 numeri (+ - * /)
# Gestire nel caso della divisione che il divisore sia DIVERSO da 0
# Esempio: inserisci il primo numero: 3
#          inserisci il secondo numero: 4
#          inserisci l'operazione: +
# output programma: 3 + 4 = 7

print("primo numero")
primo = int(input())
print("secondo numero")
secondo = int(input())

print("che operazione vuoi fare?")
operazione = input().lower()

if operazione == "+":
    print(primo, "+", secondo, "=", primo + secondo)
elif operazione == "-":
    print(primo, "-", secondo, "=", primo - secondo)
elif operazione == "*":
    print(primo, "*", secondo, "=", primo * secondo)
elif operazione == "/":
    if secondo == 0:
        print("non puoi dividere per 0")
    else:
        print(primo, "/", secondo, "=", primo / secondo)
else:
    print("operazione non valida")

# ********************* 4) Giorni mese ***************************
# Realizzare con lo SWITCH (in Python: con if/elif) un programma che chiede
# il nome del mese e restituisce il numero dei giorni.
#       Esempio: inserisci il mese: Marzo
#       output:  Marzo ha 31 giorni.
#   non considerare gli anni bisestili
