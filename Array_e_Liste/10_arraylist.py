# NOTA GENERALE (concetto senza equivalente diretto):
# in Java esiste una distinzione netta tra array (dimensione fissa) e
# ArrayList (dimensione dinamica, con metodi come add(), get(), remove()).
# In Python questa distinzione non esiste: esiste UN SOLO tipo, la lista
# (list), che è già dinamica e copre entrambi i ruoli. Questa lezione, in
# Python, userà quindi lo stesso tipo "list" già visto nella lezione
# precedente, mostrando i suoi metodi (append, insert, ecc.) come
# equivalente dei metodi di ArrayList.

lista = []
# aggiungo elementi alla lista (in Java si usa add(), in Python append())
lista.append(1)
lista.append(2)
lista.append(3)

# NOTA: in Python len() sostituisce sia array.length sia arrayList.size()
for i in range(len(lista)):
    print(lista[i])  # gli indici funzionano come in un array

lista.append(4)

for elemento in lista:
    print(elemento)

lista.append("ciao")
lista.append(True)

for elemento in lista:
    print(elemento)

# /////////////////////////////////////////////////////
# NOTA (concetto senza equivalente diretto):
# in Java, per mettere tipi primitivi (int, char, boolean, double) dentro
# collezioni come ArrayList, serve una "wrapper class" (Integer, Character,
# Boolean, Double) perché le collezioni Java accettano solo oggetti.
# In Python questo problema non esiste: in Python TUTTO è già un oggetto,
# quindi qualunque valore (numeri, caratteri, booleani...) può stare
# direttamente in una lista, senza bisogno di nessuna classe involucro.

# in Python un "carattere" è semplicemente una stringa di un solo carattere
lettere = []
lettere.append('a')
lettere.append('b')
lettere.append('c')
lettere.append('d')

for i in range(len(lettere)):
    print(lettere[i])

lettere.insert(0, 'e')  # inserisco l'elemento nella posizione 0

# stampa direttamente la lista, come se fosse Arrays.toString()
print(lettere)

for lettera in lettere:
    print(lettera)

# NOTA: in Java, il metodo forEach() delle collezioni si usa spesso insieme
# a una lambda expression o a un method reference (System.out::println).
# Le liste di Python non hanno un metodo forEach: l'idioma normale e
# idiomatico per scorrere una lista è sempre il for-each visto sopra.
# Le lambda esistono anche in Python, ma non servono qui: le vedremo in
# una lezione successiva, quando saranno davvero utili.
for lettera in lettere:
    print(lettera)

# ----------------------------------------------------
prodotti = []
prodotti.append("scarpe")
prodotti.append("maglie")
prodotti.append("camicie")

lunghezza = len(prodotti)
elemento0 = prodotti[0]

# NOTA (concetto senza equivalente diretto, attenzione a un'insidia comune):
# in Java, ArrayList ha 2 metodi remove() diversi in base al tipo
# dell'argomento: remove(int indice) rimuove per POSIZIONE, mentre
# remove(Object valore) rimuove per VALORE. In Python il metodo .remove()
# delle liste rimuove SEMPRE per VALORE. Per rimuovere per posizione si usa
# invece .pop(indice) oppure l'istruzione "del lista[indice]".
prodotti.pop(0)  # rimuove l'elemento in posizione 0 (equivalente a remove(int))
# prodotti.remove("scarpe")  # questo invece rimuoverebbe per VALORE
prodotti.insert(0, "giacca")

for prodotto in prodotti:
    print(prodotto)

# ------------------------------------------------------------------

classe = []
classe.append("mario")
classe.append("luigi")
classe.append("luca")

voti = []
voti.append(25)
voti.append(30)
voti.append(27)

for i in range(len(voti)):
    print("studente", classe[i], "voto:", voti[i])

# -------------------------------------------------------------------------
c = ['x', 'y', 'z']

# in Java, Arrays.asList(c) trasforma l'array in una lista che si può poi
# passare al costruttore di ArrayList. In Python questo passaggio non
# serve: una lista letterale è già una lista, quindi qui basta list(c)
# per farne una copia indipendente.
lettere2 = list(c)

lettere2.append('w')
for carattere in lettere2:
    print(carattere)

for carattere in lettere2:
    print(carattere)

# NOTA: in Java bisogna convertire l'ArrayList in un array vero e proprio
# con toArray() per usare certe API. In Python non serve nessuna
# conversione: la lista è già la struttura dati che si usa ovunque.
print(lettere2)

# --------------------------------------------------------------

# ordina una lista di dati (equivalente di Collections.sort)
lettere2.sort()

# cerca un elemento: in Java, Collections.binarySearch richiede che la
# lista sia ordinata e restituisce la posizione dell'elemento cercato.
# In Python la ricerca binaria non fa parte dei metodi base delle liste
# (esiste nel modulo più avanzato "bisect", da usare più avanti nel corso).
# Per un principiante, il modo idiomatico per trovare la posizione di un
# elemento è il metodo .index():
print(lettere2.index('y'))

# lista al contrario: mette i valori al contrario (equivalente di
# Collections.reverse, modifica la lista sul posto)
lettere2.reverse()
print(lettere2)

# copia di una lista
copia = list(lettere2)

print(copia)

print(lettere2[2])
