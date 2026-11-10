#http://www.html.it/pag/15613/liste/ per un riepilogo
# la lista è identificata dalla parentesi quadra, ed è una raccolta ordinata e modificabile di elementi di tipo diverso.
#  Consente membri duplicati. NON SI PUò ORDINARE (SORT) LA LISTA SE CI SONO NUMERI E LETTERE INSIEME
print("************************\n LISTE \n************************")
lista = ["apple", "banana", "cherry","banana"]
print(lista)
lista[2]="ciliegia"
print("Modificato cherry con ciliegia:")
print(lista)
lista.append("damson")  # Aggiungere un elemento al fondo.Uno solo. Per aggiungere un array alla lista usare extend
print("Aggiunto damson:")
print(lista)
lista.remove("apple")  # riumuove un elemento
print("tolto apple")
print(lista)
print("stampo numero elementi:",len(lista)) # len mi dice il mumero di elementi nella lista
lista.extend(['ford', 'bmw', 'volvo'])  # Aggiunge una lista ad un'altra lista
print("Aggiungo ford, bmv, volvo")
print(lista)
lista.insert(3, "orange")  # inserisce un valore ad una posizione specificata
print("Aggiungo orange in posizione 4")
print(lista)
lista.pop(3)  # rimuove il valore dalla posizione indicata
print("tolgo il quarto elemento")
print(lista)
lista.reverse()  # visualizza la lista al contrario
print("al contrario: ")
print(lista)
lista.sort()  # visualizza la lista in ordine alfabetico
print("sort:")
print(lista)
lista.remove("volvo")  # elimina uno specifico elemento
print("elimino volvo")
print(lista)
print("banana è all'indice: ",lista.index("banana"))#ritorna l'indice dell'elemento
print("verifica se orange è presente e se topo non è presente:")
print("orange" in lista, "topo" not in lista)#testare esistenza elemento in lista

>>> letters = ['a', 'b', 'c', 'd', 'e']
>>> letters[0] # le liste supportano indexing
'a'
>>> letters[-1]
'e'
>>> letters[1:4] # slicing
['b', 'c', 'd']
>>> 'a' in letters # gli operatori di contenimento "in" e "not in"
True
>>> letters + ['f', 'g', 'h'] # concatenazione (ritorna una nuova lista)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> [1, 2, 3] * 3 # ripetizione (ritorna una nuova lista)
[1, 2, 3, 1, 2, 3, 1, 2, 3]

>>> letters = ['a', 'b', 'c', 'b', 'a']
>>> len(letters) # numero di elementi
5
>>> min(letters) # elemento più piccolo (alfabeticamente nel caso di stringhe)
'a'
>>> max(letters) # elemento più grande
'c'
>>> letters.index('c') # indice dell'elemento 'c'
2
>>> letters.count('c') # numero di occorrenze di 'c'
1
>>> letters.count('b') # numero di occorrenze di 'b'
2

>>> letters = ['a', 'b', 'c']
>>> letters.append('d') # aggiunge 'd' alla fine
>>> letters
['a', 'b', 'c', 'd']
>>> letters.extend(['e', 'f']) # aggiunge 'e' e 'f' alla fine
>>> letters
['a', 'b', 'c', 'd', 'e', 'f']
>>> letters.append(['e', 'f']) # aggiunge la lista come elemento alla fine
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', ['e', 'f']]
>>> letters.pop() # rimuove e ritorna l'ultimo elemento (la lista)
['e', 'f']
>>> letters.pop() # rimuove e ritorna l'ultimo elemento ('f')
'f'
>>> letters.pop(0) # rimuove e ritorna l'elemento in posizione 0 ('a')
'a'
>>> letters.remove('d') # rimuove l'elemento 'd'
>>> letters
['b', 'c', 'e']
>>> letters.reverse() # inverte l'ordine "sul posto" e non ritorna niente
>>> letters # gli elementi sono ora in ordine inverso
['e', 'c', 'b']
>>> letters[1] = 'x' # sostituisce l'elemento in posizione 1 ('c') con 'x'
>>> letters
['e', 'x', 'b']
>>> del letters[1] # rimuove l'elemento in posizione 1 ('x')
>>> letters
['e', 'b']
>>> letters.clear() # rimuove tutti gli elementi rimasti
>>> letters
[]

x = lista.copy()  # copia una lista in una variable
print("copio la lista in un altra lista")
print(x)
print("ciclo sugli elementi della lista")
for elementi in x:
    print(elementi)

print("cicla al contrario con reversed")
for elementi in reversed(x):
    print(elementi)

print("cicla in ordine alfabetico")
for elementi in sorted(x):
    print(elementi)

print("stampa anche l'indice con enumerate:")
for i, v in enumerate(x):
    print(i,v)

x.clear() #elimina una lista
print(x)

print("si può ciclare con 2 o più sequenze contemporaneamente:")#vale per tutti i tipi di liste
seq1 = ('nome', 'eta', 'colore preferito:')
seq2 = ('fabio', 43, 'blu')
seq3= ('Bel nome!','Sei giovane','Bel colore!')

for s1,s2,s3 in zip(seq1,seq2,seq3):
    print("Qual'è il tuo "+s1+"? è",s2,".",s3)


print("************************************\n TUPLE \n************************************")
# Una tupla è identificata dalla parentesi tonda, e ammette valori di diverso tipo, anche duplicati.
# E' una collezione ordinata e immutabile, cioè si può solo visualizzare e non modificare o aggiungere elementi
tupla = ("mela", "pera", "banana",11,"pera")
print("banana è all'indice: ",tupla.index("banana"))#ritorna l'indice dell'elemento
print(tupla)
print("Cicla su tutti i valori:")
for val in tupla:
    print(val)

print("stampa anche l'indice con enumerate:")
for i, v in enumerate(tupla):
    print(i,v)


print("************************************\n SET\n************************************")
#Un set è una collezione non ordinata e non indicizzata,(cioè la visualizzazione è casuale) di elementi di tipo diverso.
#E' identificata dalle parentesi graffe. Si possono aggiungere e eliminare elementi ma NON SI POSSONO MODFICARE
# anche se si creano elementi duplicati, verranno considerati una volta sola
esempioSet = {'cane','cane','pesce', 'gatto',1}
print(esempioSet)
esempioSet.add('lupo')
print(esempioSet)
esempioSet.remove('gatto')
print(esempioSet)
print("Numero elementi: ",len(esempioSet))
print("ciclo su tutti gli elementi:")
for elementi in esempioSet:
    print(elementi)

# pop()   Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
# clear() Remove all elements from the set.

print("stampa anche l'indice con enumerate:")
for i, v in enumerate(esempioSet):
    print(i,v)
a = set('abracadabra') #altro modo di creare un set.
print ('a= ',a)#non visualizza i duplicati {'d', 'c', 'a', 'r', 'b'}
b={'a','b','c','z'}
print("b= ",b)
print("SET: operatori su insiemi")
print("a-b: solo i valori di a che non esistono in b")
print(a-b)
print("a|b: a or b tutto a e b senza duplicati")
print(a|b)
print("a&b: a and b i valori comuni ad entrambi")
print(a&b)
print("a^b a xor b i valori di a e di b non in comune")
print(a^b)

x = {"a", "b", "c", "d", "e"}
y = {"c", "d"}
print("x=",x,"\ny=",y)
print("y è un sottinsime di x?")
print(y.issubset(x))
print("x è un superset di y?")
print(x.issuperset(y))


print("*****************************************\nDIZIONARI\n*****************************************")
#Un dizionario è una collezione non ordinata, mutevole e indicizzata.
#I dizionari Python sono scritti con parentesi graffe e hanno chiavi e valori.
dizio =	{
  "mela": "verde",
  "banana": "gialla",
  "ciliegia": "rossa"
}
print(dizio)
print("cambio il valore della chiave mela in rosso:")
dizio["mela"] = "rossa"
print(dizio)
print("Aggiungo una nuova chiave:valore arancio: arancione")
dizio["arancio"]="arancione"
print(dizio)
print("elimino una chiave: valore mela:rossa")
del dizio["mela"]
print(dizio)
print("Il dizionario è lungo: ",len(dizio))
print("creo una lista con le chiavi del dizionario: ")
print(list(dizio))
print("ordino le chiavi di un dizionario")
print(sorted(dizio))
print("ciclo per tutte le chiavi:valori")
for k,val in dizio.items():
    print(k,":",val)
print("stampa anche l'indice con enumerate:")
for i, v in enumerate(dizio.items()):
    print(i,v)