"""
MODIFICATORI DI ACCESSO in Java:
    PUBLIC: visibile dappertutto, anche in altri progetti
    DEFAULT (senza modificatore): visibile solo dentro il package
    PRIVATE: visibile solo dentro il suo file
    PROTECTED (solo per l'ereditarietà): pubblico per le sottoclassi, privato per gli altri
    .jar -> Java ARchive, il formato con cui si "impacchetta" un programma Java

In Python non esiste questa scala di 4 livelli: come già ripetuto più
volte nel corso, esiste solo la convenzione dell'underscore iniziale,
identica ovunque si trovi il codice.

Questo file dimostra invece il vero equivalente Python dei "package"
Java: l'IMPORT di un modulo da un altro file .py nella stessa cartella.
Per eseguirlo, lancialo da dentro questa cartella (02_package) così
Python trova gli altri due file.
"""

from classe1 import Classe1
from classe2 import Classe2


# NOTA: nel file Java originale, "Persona" viene importata da un altro
# package (testPersona.Persona) e per la variabile p2 viene creata una
# CLASSE ANONIMA al volo, che ridefinisce dorme() sul posto:
#
#   Persona p2 = new Persona("giuseppe", "verdi", 40) {
#       @Override
#       public void dorme() { ... }
#   };
#
# Come vedremo meglio nel prossimo file (03_classi_anonime.py), Python
# non ha una sintassi per creare una classe "senza nome" al volo in
# questo modo: l'equivalente idiomatico è definire una piccola
# sottoclasse con un nome esplicito, come facciamo qui sotto.
class Persona:

    def __init__(self, nome, cognome, eta):
        self._nome = nome
        self._cognome = cognome
        self._eta = eta

    def dorme(self):
        print("zzzzzzzzzzzzz")

    def __str__(self):
        return "la persona si chiama " + self._nome + " " + self._cognome + " ha " + str(self._eta) + " anni"


class PersonaCheDormeMolto(Persona):
    def dorme(self):
        print("dormo 10 ore al giorno")


# ================== PROVA (equivalente del "main" di Java) ==================

p = Persona("mario", "Rossi", 20)
print(p)

p2 = PersonaCheDormeMolto("giuseppe", "verdi", 40)

p.dorme()
p2.dorme()

c = Classe1(10, 20)
print(c)

c2 = Classe2("a", "b")
print(c2)
c2.d = "ciao"

# print(c2._c)  # --> in Java non sarebbe visibile perché ha visibilità di package;
#                    in Python è comunque accessibile, essendo solo una convenzione
