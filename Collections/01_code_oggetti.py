from collections import deque

# NOTA: come già visto in 02_collections/01_coda.py, la coda Python si fa
# con collections.deque. Qui vediamo che funziona anche con oggetti
# "personalizzati" (istanze di una nostra classe), non solo con numeri o
# stringhe: non serve nessuna sintassi diversa.


class Persona:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def get_nome(self):
        return self.nome

    def get_eta(self):
        return self.eta

    def __str__(self):
        return "nome:" + self.get_nome() + " eta: " + str(self.get_eta())

    __repr__ = __str__  # vedi la nota su __str__/__repr__ nel modulo Generics


# ================== PROVA (equivalente del "main" di Java) ==================

q = deque()  # coda di persone

p = Persona("gino", 30)
p2 = Persona("rino", 5)
p3 = Persona("mino", 60)
p4 = Persona("tino", 10)
p5 = Persona("lino", 90)

q.append(p)  # equivalente di offer()
q.append(p2)
q.append(p3)
q.append(p4)
q.append(p5)

print("Primo della coda:", q[0])  # equivalente di peek(): il primo elemento senza toglierlo

# l'ordine di visualizzazione, il primo elemento e quello rimosso seguono
# sempre l'ordine di inserimento: FIFO
print(q)

while len(q) != 0:
    print("Eliminato:", q.popleft())  # equivalente di poll()
