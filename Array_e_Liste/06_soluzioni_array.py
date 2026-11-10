import random

# ********************* Es. 1 - SOMMA MEDIA*********************************
# Creare un array di 10 numeri da tastiera e calcolare la somma e la media.
mio_array = [0] * 10
somma = 0
print("inserisci 10 numeri:")
for i in range(10):
    mio_array[i] = int(input())

for ris in mio_array:
    print(ris)
    somma += ris

print("la somma è:", somma, "la media è:", somma / 10)

# ********************** Es. 2 - SOMMA POSTO PARI-DISPARI***************************
# Dire se è maggiore la somma degli elementi di posto pari o dispari.
pari_dispari = [0] * 10
somma_pari = 0
somma_dispari = 0
print("inserisci 10 numeri:")
for i in range(10):
    pari_dispari[i] = int(input())

for i in range(10):
    if i % 2 == 0:
        somma_pari += pari_dispari[i]
    else:
        somma_dispari += pari_dispari[i]

if somma_pari > somma_dispari:
    print("La somma delle posizioni pari è maggiore e vale", somma_pari)
else:
    print("La somma delle posizioni dispari è maggiore e vale", somma_dispari)

# ************************ Es. 3 - CERCA ARRAY**********************************
# Numero casuale da 1 a 20: verificare se è tra 10 numeri casuali da 1 a 10.
n = random.randint(1, 20)
print("numero casuale:", n)
numeri = [0] * 10
posizione = 0
trovato = False
for i in range(10):
    numeri[i] = random.randint(1, 10)

for i in range(10):
    print(numeri[i], end=" ")
    if n == numeri[i]:
        posizione = i
        trovato = True

if trovato:
    print("\\nil numero", n, "è stato trovato in posizione", posizione)
else:
    print("\\nil numero", n, "NON è stato trovato")

# ******************* Es. 4 - ARRAY 6 NUMERI AL CONTRARIO ***********************
# Creare un array di 6 numeri da tastiera e uno con i numeri al contrario.
primo_array = [0] * 6
secondo_array = [0] * 6

for i in range(6):
    print("inserisci il valore", i + 1)
    primo_array[i] = int(input())

inverso = len(primo_array) - 1
for i in range(len(primo_array)):
    secondo_array[inverso] = primo_array[i]
    inverso -= 1

print("Array:", primo_array)
print("Array al contrario:", secondo_array)
#
# # NOTA: in Python c'è anche una scorciatoia molto più diretta per
# # ottenere una lista al contrario, con lo slicing "a passo -1":
# # secondo_array = primo_array[::-1]

# *************************** Es 5 - Maggiori di Zero ************************************
# Riempire un array con 8 numeri > 0, contando gli errori di inserimento.
numeri = [0] * 8
num_errori = 0
print("inserisci 8 numeri maggiori di zero")
contatore = 0
while True:
    if contatore == 8:
        break
    num_utente = int(input())
    if num_utente <= 0:
        print("ti ho detto maggiore di zero")
        num_errori += 1
    else:
        numeri[contatore] = num_utente
        contatore += 1
print(numeri, num_errori)

# ****************** Es. 6 - DUE LISTE ************************
# Somma di 2 array in posizioni corrispondenti.
cinque = [0] * 5
altri_cinque = [0] * 5
somma = [0] * 5

print("inserisci 5 numeri:")
for i in range(5):
    cinque[i] = int(input())
print("inserisci altri 5 numeri")
for i in range(5):
    altri_cinque[i] = int(input())

for i in range(5):
    somma[i] = cinque[i] + altri_cinque[i]

print("la somma dei numeri in posizioni corrispondenti sono:")
for ris in somma:
    print(ris)

# *************** Es. 7 - DUE LISTE 2 *********************
# Numeri in comune tra 2 array e loro somma.
cinque = [0] * 5
altri_cinque = [0] * 5
somma = 0
comune = 0
elenco = ""

print("inserisci 5 numeri:")
for i in range(5):
    cinque[i] = int(input())
print("inserisci altri 5 numeri")
for i in range(5):
    altri_cinque[i] = int(input())

for i in range(5):
    for j in range(5):
        if cinque[i] == altri_cinque[j]:
            comune += 1
            elenco += str(cinque[i]) + " "
            somma += cinque[i]

print("le 2 liste hanno", comune, "numeri in comune:", elenco)
print("la loro somma è", somma)

# ******************** Es. 8 - MIN-MAX ******************************
min_max = [0] * 10
print("inserisci 10 numeri positivi o negativi")
for i in range(10):
    min_max[i] = int(input())

minimo = min_max[0]
massimo = min_max[0]
pos_max = 0
pos_min = 0
for i in range(10):
    if min_max[i] < minimo:
        minimo = min_max[i]
        pos_min = i
    elif min_max[i] > massimo:
        massimo = min_max[i]
        pos_max = i

print("Il valore max è", massimo, "in posizione", pos_max)
print("Il valore min è", minimo, "in posizione", pos_min)

# ********************* Es. 9 - Uguali al precedente **********************************
numeri = [0] * 10
print("Inserisci 10 numeri:")
for i in range(len(numeri)):
    numeri[i] = int(input())

print("Numeri uguali al precedente:")
for i in range(1, len(numeri)):
    if numeri[i] == numeri[i - 1]:
        print(numeri[i])

# **************** Es. 10 - Array senza duplicati ***************************************
import random
numeri = [0] * 10
for i in range(10):
    numeri[i] = random.randint(1, 10)
    print(numeri[i], end=" ")

print("\\nArray senza duplicati: ", end="")
for i in range(10):
    duplicato = False
    for j in range(i):
        if numeri[i] == numeri[j]:
            duplicato = True
            break
    if not duplicato:
        print(numeri[i], end=" ")

# ***************** Es. 11 - SOLO i valori duplicati e quante volte ******************
numeri = [1, 2, 3, 4, 2, 7, 8, 8, 3, 2]
print(numeri)

ripetuti = [False] * len(numeri)
for i in range(len(numeri)):
    if ripetuti[i]:
        continue
    conteggio = 1
    for j in range(i + 1, len(numeri)):
        if numeri[j] == numeri[i]:
            conteggio += 1
            ripetuti[j] = True
    if conteggio > 1:
        print("Numero:", numeri[i], "- Ripetizioni:", conteggio)

# ...metodo alternativo, valido solo se i valori sono compresi tra 0 e len-1
# numeri = [8, 5, 8, 9, 8, 3, 1, 8, 3, 5]
# rip = [0] * 10
# print("Array=", numeri)
#
# for num in numeri:
#     rip[num] += 1
# print("Array=", rip)
# for i in range(len(rip)):
#     if rip[i] > 1:
#         print("il numero", i, "è ripetuto:", rip[i], "volte")

# ******************* Es. 13 - palindromo ***********************************
print("inserisci una stringa: ")
parola = input()

palindromo = True
lettere = parola.replace(" ", "")  # togliamo gli spazi (le stringhe restano scorribili come una lista)

for i in range(len(lettere)):
    if lettere[i] != lettere[len(lettere) - 1 - i]:
        palindromo = False
        break

if palindromo:
    print("la frase", parola, "è palindroma")
else:
    print("la frase", parola, "NON è palindroma")

# ************************* Es. 14 - somma num. precedente e successivo ************************
numeri = [0] * 10
print("Inserisci 10 numeri:")
for i in range(len(numeri)):
    numeri[i] = int(input())

trovato = False
for i in range(1, len(numeri) - 1):
    if numeri[i] == numeri[i - 1] + numeri[i + 1]:
        print("Trovato:", numeri[i - 1], "+", numeri[i + 1], "=", numeri[i])
        trovato = True

if not trovato:
    print("Nessun numero corrisponde alla somma del precedente e del successivo.")
