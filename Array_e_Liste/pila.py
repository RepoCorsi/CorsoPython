# PILA (LIFO)
# Last in first out
# l'ultimo che entra è il primo che esce
#
# In Python non serve una classe apposita: una normale lista si comporta
# già perfettamente come una pila, perché append() e pop() lavorano
# entrambi sull'ULTIMO elemento della lista.

p = [] #lista vuota
#append aggiunge alla fine
p.append("piatto1") #aggiunge alla fine
p.append("piatto2")
p.append("piatto3")
p.append("piatto4")

p.insert(1,"ciao") #inserisce nella posizione indicata dall'indice

print(p)

print("il primo elemento inserito al fondo della lista è:",p[0]) # restituisce il primo elemento, al fondo della pila
print("L'ultimo elemento inserito in cima alla lista è:",p[-1])  # restituisce l'ultimo elemento, in cima alla pila

print(f"elimino l'ultimo elemento inserito in cima alla lista {p[-1]}")
p.pop()  # rimuove l'elemento in cima alla pila (l'ultimo)

print(p)

print(f"elimino l'elemento indicato dall'indice o dal nome:")
p.remove(p[1]) #secondo elemento perchè parte da zero
#p.remove("ciao") #funziona sia con la posizione che col nome
print(p)