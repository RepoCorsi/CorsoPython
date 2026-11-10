# I SET NON SONO ORDINATI E NON AMMETTE DUPLICATI
# NON ordinata (CIOÈ LA VISUALIZZAZIONE È CASUALE. ogni volta che eseguo posso ottenere un diverso ordine) 
# gli elementi sono rimescolati all'interno.
# l'ordine interno dipende da una funzione di HASH
# non esiste un metodo get per accedere a un elemento tramite posizione
# Elementi possono essere di tipo diverso.
# E' identificata dalle parentesi graffe. 
# Si possono aggiungere e eliminare elementi ma NON SI POSSONO MODFICARE!
# anche se si creano elementi duplicati, verranno considerati una volta sola
esempioSet = {'cane','cane','pesce', 'gatto'}
print(esempioSet)
esempioSet.add('lupo')
print(esempioSet)
esempioSet.add('lupo') #se c'è già non inserisce di nuovo
print(esempioSet)
esempioSet.remove('gatto')
print(esempioSet)

#Rimuove e restituisce un elemento CASUALE dal set.
elemento_eliminato=esempio_set.pop() #elimina e ritorna un elemento a caso dal set
print(elemento_eliminato)

#se non esiste l'elemento remove() da errore!
#esempio_set.remove("topo")
#Discard no, se non esiste non fa niente
esempio_set.discard("topo")
print(esempio_set)


print("Numero elementi: ",len(esempioSet))

print("ciclo su tutti gli elementi:")
for elementi in esempioSet:
    print(elementi)

# clear() Remove all elements from the set.

print("stampa anche l'indice con enumerate:")
for i, v in enumerate(esempioSet):
    print(i,v)

#--------------------
# altro modo: #con set() creiamo un set
mio_set = set()
mio_set.add("c")
mio_set.add("a")
mio_set.add("b")
mio_set.add("b")
mio_set.add("a")

print(mio_set)

elemento_gia_presente = "d" in mio_set
print(elemento_gia_presente)  # False se non c'è l'elemento

for valore in mio_set:
    print(valore)
    
# sorted() restituisce una lista ordinata solo in visualizzazione    
print(sorted(mio_set))  #solo visualizzazione perchè i set non posono cambiare

# mio_set rimane un set
print(type(mio_set))  # Output: <class 'set'> #rimane un set
print(mio_set)         # {'a', 'c', 'b'}

# per trasformarlo in lista bisogna assegnarlo ad una variabile:
lista=sorted(mio_set)
print(type(lista))  # Output: <class 'list'> #diventa una lista
print(lista)  #['a', 'b', 'c']

# Usiamo reverse=True per invertire l'ordine
lista_decrescente = sorted(mio_set, reverse=True)

print(lista_decrescente) # Output: ['c', 'b', 'a']

#-----------------------------------
a = set('abracadabra') #altro modo di creare un set.
print(a) #NON è ORDINATO!

b={'a','b','c','d'}
print(b)
print("SET: operatori su insiemi")
print("a-b: solo i valori di a che non esistono in b")
print(a-b) #LEFT outer JOIN con clausola WHERE b.chiave IS NULL
print("a|b: a or b tutto a e b senza duplicati")
print(a|b) #una union
print("a&b: a and b i valori comuni ad entrambi")
print(a&b) #equi join /inner join
print("a^b a xor b i valori non in comune")
print(a^b) #FULL OUTER JOIN WHERE a.id IS NULL OR b.id IS NULL

x = {"a", "b", "c", "d", "e"}
y = {"c", "d"}
print("x=",x,"\ny=",y)
print("y è un sottinsime di x?")
print(y.issubset(x))
print("x è un superset di y?")
print(x.issuperset(y))

#-------------------------------------------
# Rimozione duplicati da una lista:
# lista ➔ set ➔ lista

# Lista di partenza con diversi elementi duplicati
lista_duplicati = ["mela", "banana", "mela", "kiwi", "banana", "pitecantropo", "mela"]

# 1. Trasformazione in set: i duplicati vengono eliminati automaticamente
senza_duplicati = set(lista_duplicati)

# 2. Riconversione in lista
lista_pulita = list(senza_duplicati)

#L'ORDINE NON SARÀ LO STESSO PERCHÈ SET NON è ORDINATO!
print("Lista originale:", lista_duplicati)
print("Lista senza duplicati:", lista_pulita)


#--- ESERCIZIO: -------------------
#--
# 🏋️ Esercizio Pratico: "Il Gestore del Magazzino"
'''
Gestire il magazzino di un piccolo negozio di vestiti. Hai questa lista di vestiti rimasti in stock:
magazzino = ["maglietta", "Jeans", "felpa", "felpa", "Jeans", "camicia","gonna"]
Scrivere un codice che:
1. Controlla se un vestito è presente in magazzino. Se c'è, stampa un messaggio di conferma, altrimenti stampa "vestito non disponibile".
2. Conta quante copie di un determinato vestito ci sono in magazzino e stampa il risultato.
3. Trova l'indice (la posizione) della prima copia di un vestito nella lista.
4. simulare la vendita di un vestito (rimuovendolo dalla lista) e stampare la lista aggiornata
5. BONUS: Usa il trucco del Set per ripulire la lista magazzino dai duplicati e stampa una nuova lista che contenga solo i titoli unici dei vestiti disponibili.
'''
magazzino = ["maglietta", "Jeans", "felpa", "felpa", "Jeans", "camicia","gonna"]

# 1. Controllare se "felpa" è presente
if "felpa" in magazzino:
    print("la felpa è disponibile in magazzino.")
else:
    print("la felpa non disponibile")

# 2. Contare quante copie ci sono
quantita = magazzino.count("felpa")
print("Copie disponibili:", quantita)

# 3. Trovare l'indice della prima copia
indice = magazzino.index("felpa")
print("La prima copia si trova all'indice:", indice)

# 4. Simulare la vendita di una copia
if "felpa" in magazzino:
    magazzino.remove("felpa")
    print("Vendita effettuata!")
else:
    print("Impossibile vendere: vestito non disponibile.")

# 5. Stampare il magazzino aggiornato
print("Magazzino aggiornato:", magazzino)

# 6. BONUS: eliminare i duplicati usando un Set
vestiti_unici = list(set(magazzino))
print("Vestiti disponibili senza duplicati:", vestiti_unici)

#------------------------------------------------------------