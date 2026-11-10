# NOTA GENERALE: come già visto in 01_fondamenta/10_arraylist.py, Python
# usa un solo tipo (list) sia per gli array che per gli ArrayList di
# Java. Le note già fatte in dettaglio in quel file qui non si ripetono.

lettere = []
lettere.append('a')
lettere.append('b')
lettere.insert(0, 'c')  # equivalente di add(0, 'c'): inserisce all'inizio
lettere.append('d')

print(lettere)

# NOTA: niente lettere[2] in Java (ArrayList non si legge con l'indice
# diretto, serve get()); in Python invece l'indice diretto FUNZIONA
# anche sulle liste "dinamiche", perché è l'unico tipo che esiste.
print("Elemento alla posizione 2:", lettere[2])

print("dimensione=", len(lettere))

for i in range(len(lettere)):
    print(lettere[i])

print("----------------------------")

for carattere in lettere:
    print(carattere)

# NOTA: come già visto, le liste Python non hanno un metodo forEach: il
# for-each qui sopra è già l'equivalente idiomatico, sia della lambda
# expression sia del "method reference" (System.out::println) di Java.
for carattere in lettere:
    print(carattere)

print("----------------------------")

print('a' in lettere)  # equivalente di .contains('a')

# NOTA: containsAll() di Java diventa, in Python, un controllo con
# l'operatore "in" ripetuto su ogni elemento, oppure — più elegante —
# la verifica che l'insieme di un gruppo sia "sottoinsieme" dell'altro
# (set(...) <= set(...)); qui restiamo sul controllo elemento per
# elemento, più semplice da leggere per chi comincia.
arl = ['a', 'b', 'c', 'd']
contiene_tutti = True
for elemento in arl:
    if elemento not in lettere:
        contiene_tutti = False
        break
print("contiene tutti questi?", contiene_tutti)

# NOTA: .indexOf() di Java restituisce -1 se non trova l'elemento. In
# Python il metodo .index() delle liste, se non trova nulla, solleva
# addirittura un errore (ValueError): per replicare il comportamento di
# Java serve un piccolo controllo con "in" prima di cercarlo.
print(lettere.index('t') if 't' in lettere else -1)

print("è vuoto?", len(lettere) == 0)

# Altro esempio
prodotti = []
prodotti.append("scarpe")
prodotti.append("t-shirt")
prodotti.append("camicie")

lunghezza = len(prodotti)
elemento0 = prodotti[0]

prodotti.pop(2)  # .remove(indice) in Java diventa .pop(indice) in Python (vedi nota già vista)

prodotti.append("giacche")

for elemento in prodotti:
    print(elemento)

classe = []
classe.append("Marco")
classe.append("Gennaro")
classe.append("Anna")
classe.append("Laura")

for studente in classe:
    print(studente)

voti = []
voti.append(25)
voti.append(30)
voti.append(30)
voti.append(27)

for i in range(len(voti)):
    print("Nome Studente:", classe[i], "- voto:", voti[i])

# ...................... LISTA DA UNA LISTA GIÀ ESISTENTE .......................
c = ['x', 'y', 'z']
lettere2 = list(c)  # copia indipendente (vedi già la nota fatta in 10_arraylist.py)

for car in lettere2:
    print(car)

print("----------------------------")

lettere2[0] = 'w'  # equivalente di .set(0, 'w'): sostituisce il valore a quell'indice

for n in lettere2:
    print(n)

# NOTA: come già visto, Python non ha bisogno di "convertire" una lista
# in un array: la lista è già l'unica struttura usata ovunque, quindi
# .toArray() non ha corrispettivo perché non serve.
print(lettere2)

print("----------------------------")

# NOTA: in Java si può ciclare su un ArrayList anche con un Iterator
# esplicito (hasNext()/next()). In Python questo meccanismo esiste
# "sotto il cofano" (è quello che il for usa automaticamente), ma non si
# usa quasi mai a mano: il for-each è già l'equivalente diretto e più
# leggibile.
it = iter(lettere2)
for elemento in it:
    print(elemento)

# /*
# RIEPILOGO METODI LISTA:
# .append(a)   aggiunge un elemento a alla fine della lista.
# .insert(i,c) aggiunge nella posizione i l'elemento c.
# .pop(i)      elimina l'elemento nella posizione i.
# len(lista)   restituisce la dimensione della lista.
# lista[i]     restituisce/assegna l'elemento nella posizione i.
# non serve isEmpty(): si usa semplicemente "len(lista) == 0"
# */

# *********************** LISTA di tipo generico ***********************************
misto = []
misto.append(1)
misto.append("ciao")
misto.append(True)
misto.append(3.14)

print(misto)
for o in misto:
    print(o)

# .....................................................................
nani = []
nani.append("pisolo")
nani.append("eolo")
nani.append("mammolo")
nani.append("gongolo")
nani.append("brontolo")
nani.append("cucciolo")
nani.append("dotto")

print(nani)

# NOTA: .addAll() di Java diventa .extend() in Python (aggiunge tutti
# gli elementi di un'altra lista, uno per uno, alla fine).
nani.extend(lettere)


def stampa(parole):  # funzione che accetta in input una lista e la stampa
    for val in parole:
        print(val)


stampa(nani)

# NOTA: .remove("gatto") di Java non solleva errore se l'elemento non
# c'è (restituisce solo False). In Python, .remove() SOLLEVA un errore
# se il valore non è presente: va quindi controllato prima con "in".
if "gatto" in nani:
    nani.remove("gatto")

# .subList(4,6).clear() di Java elimina un intervallo di elementi. In
# Python lo stesso risultato si ottiene con "del" e lo slicing.
del nani[4:6]

stampa(nani)

# NOTA: .removeAll() di Java rimuove dalla lista tutti gli elementi che
# fanno parte di un'altra lista. In Python si scorre l'altra lista e si
# rimuove ogni elemento presente.
for elemento in lettere:
    if elemento in nani:
        nani.remove(elemento)

stampa(nani)

print(nani[1])

print("--------------")

print("eolo" in nani)

nani.sort()  # equivalente di Collections.sort()
for o in nani:
    print(o)

# vedi già la nota su Collections.binarySearch in 01_fondamenta/10_arraylist.py
print(nani.index("eolo") if "eolo" in nani else -1)

print("************")
nani.reverse()  # ATTENZIONE: come in Java, modifica la lista sul posto
print(nani)

copia = list(nani)
print(copia)
