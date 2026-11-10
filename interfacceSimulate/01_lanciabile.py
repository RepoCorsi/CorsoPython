# NOTA GENERALE SULLE INTERFACCE (concetto senza parola chiave dedicata):
# Java ha una parola chiave apposta, "interface": un contratto che elenca
# dei metodi (per default tutti pubblici e astratti) che le classi
# possono impegnarsi a rispettare con "implements". Una classe Java può
# estendere UNA SOLA altra classe, ma implementare PIÙ interfacce insieme:
# è proprio per aggirare il limite dell'ereditarietà singola che Java ha
# introdotto le interfacce.
#
# Python non ha una parola chiave "interface", perché non gli serve: le
# classi Python supportano già nativamente l'EREDITARIETÀ MULTIPLA (una
# classe può ereditare direttamente da più classi contemporaneamente).
# L'equivalente idiomatico più vicino a un'interfaccia Java è quindi una
# classe astratta (ABC, vista nel modulo precedente) senza attributi
# propri e con solo metodi @abstractmethod: le classi che la
# "implementano" la ereditano come farebbero con qualunque altra classe.
#
# Nei prossimi file vedremo anche: metodi che nell'interfaccia hanno già
# un corpo (i "default method" di Java, che in Python sono semplicemente
# metodi normali dentro la classe astratta) e interfacce "marcatrici"
# senza nessun metodo.

import random
from abc import ABC, abstractmethod


# NOTA: in Java questa interfaccia dichiara anche un campo
# "Random r = new Random();", condiviso da tutte le classi che la
# implementano, perché le funzioni casuali di Java richiedono un oggetto
# Random creato esplicitamente. Il modulo "random" di Python, invece,
# offre già le sue funzioni pronte all'uso (random.randint(...)) senza
# bisogno di creare nessun oggetto: quindi qui quel campo non serve.
class Lanciabile(ABC):

    @abstractmethod
    def lancia(self):
        pass


class Dado(Lanciabile):

    def lancia(self):
        return str(random.randint(1, 6))  # trasformo il numero in stringa


class Moneta(Lanciabile):

    def lancia(self):
        return "testa" if random.randint(0, 1) == 0 else "croce"  # 0 testa, 1 croce


# ================== PROVA (equivalente del "main" di Java) ==================

l = [Dado(), Dado(), Moneta(), Moneta()]

testa = 0
sei = 0

for lanciabile in l:
    ris = lanciabile.lancia()  # "testa"/"croce" oppure un numero da 1 a 6
    print(ris)

    if ris == "testa":
        testa += 1  # se esce testa, incremento il contatore
    elif ris == "6":
        sei += 1  # se esce 6, incremento il contatore

if testa == 2 or sei == 2:
    print("Hai vinto")
