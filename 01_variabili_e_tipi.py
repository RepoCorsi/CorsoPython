#1. Python è un linguaggio di programmazione:
# - Orientato agli oggetti
# - Procedurale
# - Case Sensitive
# - Debolmente tipizzato

print("ciao a tutti")
print("come state?")
print("Benvenuti al corso di python!!")

# Commento: non viene eseguito nel codice

# In Python, la funzione print() va a capo di default. 
# Per evitare il salto riga, usiamo il parametro end=""
print("aaaaaaa", end="")
print("bbbbbb") #dopo si ripristina da solo
print("cccc")

print("a","b","c", sep="-") #mette il sepraratore tra gli elementi

# Le variabili sono "contenitori" di un'informazione singola
# Il valore di una variabile, può cambiare nel corso dello script
# Le variabili devono avere dei nomi "parlanti"

# regole per i nomi delle variabili: valgono le stesse regole di Java
# (niente numero all'inizio, niente spazi, no parole riservate);
# camelCase o snake_case sono entrambe leggibili, ma la convenzione
# idiomatica di Python per le variabili è lo snake_case (nome_variabile)

# Regole per la denominazione
# camelCase (saldoConto)
# PascalCase (SaldoConto)
# snake_case (saldo_conto)
# kebab-case (saldo-conto) SCONSIGLIATO
# UPPER_CASE (SALDO_CONTO) Solitamente utilizzato con le costanti
# 

# Commento
# In Python non dichiariamo il tipo della variabile:
# il tipo è associato al valore che assegniamo.
# Tipi di dato: String, Number (Integer, Float), Boolean (True, False)

# nomeVariabile = valore (dichiaro e assegno un valore)
mioNome = "Mario" #Questa è una String
mioCognome = "Rossi"
numeroFortunato = 1000 #Questo è un Number (Integer)
presenza = True #Questo è un Boolean
piGreco = 3.14 #Questo è un Number(Float)

#Richiamo le variabili (leggere il suo valore)
#Con print() stampo nel terminale di VSCode
# 1° Modo
print("Ciao, mi chiamo", mioNome, mioCognome)

# 2° Modo
print("Ciao, mi chiamo " + mioNome + " " + mioCognome)

# 3° Modo - concatenazione con formattazione
print(f"Ciao, mi chiamo {mioNome} {mioCognome}. Il mio numero fortunato è il {numeroFortunato}. Il pi greco vale {piGreco}")

#ATTENZIONE!:
# In Python non possiamo sommare direttamente stringhe e numeri con il '+'
#print("Hai " + 51 + " anni") #NO! ERRORE STRINGA + NUMERO
#VERSIONE CORRETTA:
print("Hai " + str(51) + " anni") #CONVERSIONE NUMERO A STRINGA

# --------- Tipi numerici ----------------------
# NOTA: come già detto, Python ha un solo tipo intero int: niente byte/short/
x = "Ciao"
print(type(x))  #restituisce <class 'str'> (stringa)

y = 10
print(type(y))  #restituisce <class 'int'> (numero intero)

z = 3.14
print(type(z))  #restituisce <class 'float'> (numero decimale)

i = 1
print(i)

#Gli interi "lunghi" si possono scrivere con l'underscore per leggibilità.
#Gli int hanno lunghezza 'infinita'.
#Il limite è sostanzialmente quello dato dalla memoria disponibile del computer.
visualizzazioni = 123_456_789
print(visualizzazioni)

primo = 10
secondo = 5
print(primo + secondo)  # 15
print(primo - secondo)  # 5
print(primo * secondo)  # 50
print(primo / secondo)  # 2.0 (in Java "/" tra due int darebbe 2, non 2.0)
# Attenzione: in Python / produce sempre una divisione decimale.
# Per ottenere una divisione intera si usa //.
print(primo // secondo) # 2  (Divisione intera)
print(primo % secondo)  # 0

print(10 * 10 / 5 + 3 - 1 * 4 / 2)  # stesso ordine di esecuzione di Java

# ------- Variabili con la virgola ----------------------
# Numeri decimali
f = 1.5
d = 2.1
print("virgola:", f," ",d)
#16 cifre significative: 1.123456789012345

# *********************** TIPI CARATTERE ***********************************
a1 = 'a'
a2 = 'b'
a3 = 'c'

# carattere unicode: in Python basta scrivere direttamente il simbolo
euro = '€'

c1 = '1'
c2 = '2'
c3 = '3'

print(euro)
print(c1, c2, c3)

# Python non possiede il tipo char.
# Un singolo carattere è una stringa di lunghezza 1.

# Per ottenere il codice Unicode di un carattere possiamo usare ord().
print(ord("A"))#65

# Per ottenere il carattere associato a un codice Unicode usiamo chr().
a_maiuscola = chr(65)  # dalla tabella ascii: bisogna passare da chr(), niente cast diretto
print(a_maiuscola)

#i "caratteri" si possono incrementare così
# NOTA: niente "++": bisogna ricavare il codice, incrementarlo e riconvertirlo
a_maiuscola = chr(ord(a_maiuscola) + 1)  # B
print(a_maiuscola)

a_minuscola = 'a'
a_minuscola = chr(ord(a_minuscola) + 1)  # b  
print(a_minuscola)

# ******************** BOOLEANI *******************************
# I valori booleani in Python sono True e False (con la lettera iniziale MAIUSCOLA)
vero = True
falso = False
print("il valore di vero è", vero)
print("il valore di falso è", falso)

eta = 18
maggiorenne = eta >= 18  # True

# L'operatore logico di negazione NOT in Python si scrive a parole: 'not' (invece di '!')
b3 = not vero  
print("il valore di b3 è", b3)

# In Python possiamo convertire esplicitamente un intero in booleano:
# lo 0 equivale a False, qualsiasi altro numero equivale a True.
i2 = 0
b4 = bool(i2)  # b4 sarà False
print("Conversione intero 0 a booleano:", b4)


# *********ESPRESSIONI:****************
base = 4
altezza = 6
area = base * altezza
print("area =", area)

# --------------------------- Costanti --------------------------------------
#IN PYTHON NON ESISTONO LE COSTANTI!
# Si usa una CONVENZIONE di scrittura: i nomi delle costanti si scrivono interamente in MAIUSCOLO.
# Questo avvisa gli altri programmatori di non modificare quel valore.
PI = 3.14159  # per convenzione: MAIUSCOLO 
print(PI)

# ********************** CAST ******************************
a = 10
dbl = float(a)  # Converte l'intero in decimale (float) -> 10.0
print(dbl)  # 10.0

d3 = 3.9999999999
i3 = int(d3)  # Perde la parte decimale -> 3
print("Il risultato di i3 è", i3)

l5 = 56
f5 = float(l5)
print("Il risultato di f5 è", f5)

# Conversione da carattere a valore ASCII
prova = ord('1')  # conversione da carattere '1' al valore ascii
print("Il risultato di prova è", prova)

print("----------------------")
lettera = 'a'
ascii_codice = ord(lettera)
print(ascii_codice)  # 97
ascii_codice = ascii_codice + 1  # 98 b
ascii_codice += 1  # 99 c
ascii_codice += 1  # 100 d
print(ascii_codice)
print("----------------------------")

carattere = chr(100)  # d
print(carattere)

# Da Stringa a Numero:
uno = "1"
numero_convertito = int(uno)
print(numero_convertito)

# Da Numero a Stringa:
n = 10
dieci = str(n)
print(dieci)  # "10" come stringa


#Operatori brevi
# x++ o ++x: dobbiamo sempre scomporre in due istruzioni separate.
x = 10
print(x)
x += 1  # equivalente concettuale di x++ (ma il valore stampato PRIMA non è più "vecchio")
print(x)
x += 1
print(x)
x -= 1
print(x)

# NOTA: gli interi (non hanno limite).
# per i numeri con la virgola, il limite esiste e si trova nel modulo sys:
import sys
print("Range float è", sys.float_info.min, sys.float_info.max)

# Massimo tra due numeri: in Python si usa la funzione integrata max()
num1 = 3
num2 = 4
massimo = max(num1, num2)  # max() è già una funzione pronta
print("il maggiore tra", num1, "e", num2, "è", massimo)

# SCAMBIO DI 2 VARIABILI
var1 = 3
var2 = 8
print("Prima dello scambio: ", var1, ",", var2)

# Metodo classico (usando una variabile temporanea):
# temp = var1
# var1 = var2
# var2 = temp

# valori. In Python si può scambiare direttamente in una riga sola.
var1, var2 = var2, var1
print("Dopo lo scambio: ", var1, ",", var2)


# Esercizi:

#--------------------------------------------------
# Esercizio 1:
# calcolo perimetro rettangolo base 25 altezza 40
base_rett = 25
altezza_rett = 40
perimetro = (base_rett + altezza_rett) * 2
print(f"Perimetro rettangolo: {perimetro}")

# Esercizio 2:
# Programma che calcola l'area del cerchio (pi*r*r) e il perimetro (2*pi*r)
# con raggio a piacere. Definire una costante PI, dichiarare raggio e area,
# stampare i risultati.
PI_COSTANTE = 3.14159
raggio = 5.0
area_cerchio = PI_COSTANTE * (raggio ** 2)  # In Python l'elevamento a potenza si fa con **
circonferenza = 2 * PI_COSTANTE * raggio
print(f"Raggio: {raggio} -> Area: {area_cerchio:.2f}, Circonferenza: {circonferenza:.2f}")