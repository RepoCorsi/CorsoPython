# CODA (FIFO)
# il primo che entra è il primo che esce
# fifo -> first in first out
#
# In Python la libreria standard offre il modulo "collections" con la
# classe deque (si legge "deck", coda a doppia estremità), pensata proprio
# per aggiungere/togliere elementi in modo efficiente da entrambi i lati.

from collections import deque

q = deque()
q.append("cane")
q.append("gatto")
q.append("pesce")

print(len(q))  # dimensione
print(q)  # stampa la coda

# NOTA: Per vedere il primo elemento bisogna accedere all'indice 0, come per una lista.
print("primo da servire=", q[0])  # il primo della coda

for elemento in q:
    print(elemento)

# per togliere un elemento dalla coda si usa popleft(): toglie e restituisce
# l'elemento più a sinistra (quello entrato per primo).
q.popleft()  # elimina l'elemento in testa alla coda

print(q)

print("la coda è vuota?", len(q) == 0)
# NOTA: deque ha comunque anche i metodi appendleft() e pop() per lavorare
# sull'altro lato della coda, se servisse.
