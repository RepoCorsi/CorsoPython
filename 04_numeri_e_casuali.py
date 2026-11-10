# ************** MATH ******************
# In Python, funzioni di base come max() e min() sono incluse nativamente,
# non occorre importare o chiamare un modulo Math.
massimo = max(5, 10)
print("Massimo:", massimo)

minimo = min(5, 10)
print("Minimo:", minimo)

# Per funzioni matematiche più specifiche usiamo il modulo 'math' importato.
import math

radice = math.sqrt(8)
potenza = math.pow(2, 3) # Ritorna un float 
potenza = 2 ** 3  # equivalente di Math.pow(2,3), ma con l'operatore **

# round() arrotonda all'intero più vicino. Ritorna un intero.
# Se finisce esattamente con .5, arrotonda al numero PARI più vicino (arrotondamento bancario, es: 5.5 -> 6, ma 4.5 -> 4  e  7.5 ->8) i PARI
print(round(5.5))  # 6

# oppure, per ottenere esattamente il numero di decimali:
print(round(5.5,1))  # si mette il secondo parametro

numero = 3.56432

# per arrotondare a n cifre si usa format()
numero_formattato = format(numero, ".2f")
print(numero_formattato)  # ritorna una stringa, solo per visualizzazione

#oppure identico ma più comodo si usano le f-string (stringhe formattate)
print(f"{numero:.2f}")

print(math.ceil(5.4)) # Valore più alto (prossimo intero) -> 6
print(math.floor(5.8)) # Valore più basso (intero precedente) -> 5

# ============================================================
# NUMERI CASUALI
# ============================================================
# Random ************************************************
# Bisogna importare random
import random

#Estremi
#casuale = random.randint(-2**31, 2**31 - 1) 

# NOTA: random.randint() richiede sempre ENTRAMBI gli estremi;
limite = random.randint(0, 5)  # da 0 a 5 inclusi
print(limite)

estremi = random.randint(2, 10)  # da 2 a 10, entrambi inclusi
print(estremi)

# lo stesso con i numeri decimali
# random.random() genera un float tra 0.0 e 1.0 (escluso)
print(random.random()) #tra 0.0 e 1.0 (escluso)
#Con estremi
print(random.uniform(2.5, 11.0)) #lo stesso che random.random() ma con estremi

# con i booleani
print(random.choice([True, False]))

#Si pouò usare random.choice() su una stringa:
lettera = random.choice("abcdefghijklmnopqrstuvwxyz")
print(lettera)

#stesso esempio di sopra ma con import string
import string

lettera = random.choice(string.ascii_lowercase)
print(lettera)

letteraMaiuscola = random.choice(string.ascii_uppercase)
print(letteraMaiuscola)


# random.randrange(n) genera un numero da 0 a n-1 (estremo superiore escluso).
limite = random.randrange(6) # Da 0 a 5
print(limite)

# random.randrange(start, stop) esclude l'estremo superiore.
estremi = random.randrange(2, 11) # Da 2 a 10
print(estremi)

#Differenza randint VS randrange:
#randint(2, 11) include l'11
#random.randrange(2, 11) esclude l'11.
#randrange permette anche di specificare un terzo argomento step, che indica il "passo" o salto tra i numeri.

#Esempio:
# Genera solo numeri PARI compresi tra 2 e 10 (l'11 è escluso, passo di 2)
numero_pari = random.randrange(2, 11, 2) #2, 4, 6, 8, 10

# Genera solo numeri DISPARI compresi tra 1 e 9 (il 10 è escluso, passo di 2)
numero_dispari = random.randrange(1, 10, 2) # Possibili risultati: 1, 3, 5, 7, 9


############################################################
# ************************** Generatore di Password **************
# Generiamo 4 numeri casuali nell'intervallo dei caratteri ASCII stampabili (32 - 125)
num1 = random.randint(32, 125)
num2 = random.randint(32, 125)
num3 = random.randint(32, 125)
num4 = random.randint(32, 125)

print("Esempio Password")
# Usiamo la funzione integrata chr() per convertire un codice numerico ASCII nel carattere corrispondente
char1 = chr(num1)
char2 = chr(num2)
char3 = chr(num3)
char4 = chr(num4)

print(char1)
print(char2)
print(char3)
print(char4)

password = char1 + char2 + char3 + char4
print("password:", password)

# In realtà per password reali Python dispone del modulo secrets,
# progettato per la generazione di valori casuali adatti a scopi di sicurezza.
import secrets

password = secrets.token_urlsafe(6) #8 caratteri. 6 è il numero da mettere per ottenere 8 caratteri. 
#numero di lettere che voglio X 0.75 mi da il numero caratteri da mettere nella funzione
#Indica il numero di byte casuali generati, non la lunghezza finale. #Questi byte vengono poi codificati, quindi la stringa risultante è più lunga.
#Formula per calcolare i parametri: numero di lettere desiderate X 0.75. Es: 8 X 0.76 = 6 è il numero da mettere nella funzione.
print(password)

#oppure più facile:
password = secrets.token_urlsafe(8)[:8] #mettiamo il valore e poi lo prendiamo con lo slicing[:8]
print(password)


############# ESERCIZIO: due dadi #############
# Programma che simula il lancio di due dadi (a sei facce)
# Mostra il valore del primo dado, del secondo e la somma.
# Con le variabili booleane stampare se i due dadi sono uguali
dado1 = random.randint(1, 6)
print(dado1)
dado2 = random.randint(1, 6)
print(dado2)
print("somma=", dado1 + dado2)
uguali = dado1 == dado2
print("sono uguali?", uguali)


############# ESERCIZIO: estremi generati dall'utente #############
# Chiedere all'utente 2 numeri da usare come estremi per generare un numero casule.
# Stampa i 2 numeri e il numero casuale generato a partire dai 2 numeri
print("primo numero")
numero1 = int(input())
print("Secondo numero")
numero2 = int(input())

# Assicuriamoci che il primo sia minore del secondo per evitare errori in randint
min_val = min(numero1, numero2)
max_val = max(numero1, numero2)

numero_casuale = random.randint(min_val, max_val)

print(min_val, max_val, numero_casuale)

