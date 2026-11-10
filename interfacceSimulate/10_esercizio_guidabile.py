"""
Creare un'interfaccia chiamata Guidabile.
Scrivere una classe astratta Veicolo che preveda una targa, una marca, un
modello e un'età. Aggiungere i vari get/set e __str__.
Scrivere le classi Automobile e Motociclo che estendono Veicolo e
implementano Guidabile.
La classe Automobile prevede una stringa che ne descrive il tipo
("utilitaria", "StationWagon", "suv"...), mentre Motociclo prevede un
numero che ne descrive la cilindrata (50, 125...).
Creare una lista di oggetti guidabili e stampare l'elenco dei veicoli con
le loro caratteristiche.
"""

from abc import ABC, abstractmethod


class Guidabile(ABC):

    @abstractmethod
    def guida(self):
        pass


# NOTA (piccola differenza pratica): in Java, una classe può essere
# dichiarata "abstract" anche SENZA nessun metodo astratto, solo per
# impedire che se ne creino oggetti direttamente. In Python, ereditare
# da ABC blocca la creazione di un oggetto solo se la classe ha ALMENO
# un metodo @abstractmethod non ancora implementato: qui Veicolo eredita
# comunque da ABC per comunicare l'intento (è pensata per essere
# estesa), ma — a differenza di Java — nulla impedirebbe tecnicamente di
# creare un Veicolo() direttamente, perché non ha metodi astratti propri.
class Veicolo(ABC):

    def __init__(self, targa, marca, modello, eta):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.eta = eta

    def get_eta(self):
        return self.eta

    def set_eta(self, eta):
        self.eta = eta

    def get_targa(self):
        return self.targa

    def set_targa(self, targa):
        self.targa = targa

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modello(self):
        return self.modello

    def set_modello(self, modello):
        self.modello = modello

    def __str__(self):
        return ("targa: " + self.get_targa() + " Marca " + self.get_marca()
                + " modello " + self.get_modello() + " eta " + str(self.get_eta()) + "\n")

    __repr__ = __str__


# NOTA: qui vediamo bene il "vantaggio" dell'ereditarietà multipla di
# Python: Automobile eredita CONTEMPORANEAMENTE da una classe astratta
# concreta (Veicolo) e da quella che in Java sarebbe un'interfaccia
# (Guidabile), con la stessa identica sintassi, senza nessuna
# distinzione (vedi anche 05_oop/04_interfacce/02_pesabile.py).
class Automobile(Veicolo, Guidabile):

    def __init__(self, tipo, targa, marca, modello, eta):
        super().__init__(targa, marca, modello, eta)
        self.tipo = tipo

    def guida(self):
        print("si guida col volante")


class Motociclo(Veicolo, Guidabile):

    def __init__(self, cilindrata, targa, marca, modello, eta):
        super().__init__(targa, marca, modello, eta)
        self.cilindrata = cilindrata

    def guida(self):
        print("si guida col manubrio")


# ================== PROVA (equivalente del "main" di Java) ==================

g = [
    Automobile("utilitaria", "ssa", "fiat", "punto", 10),
    Automobile("utilitaria", "ssa", "fiat", "punto", 10),
    Motociclo(125, "sdf", "Honda", "cbr", 20),
]

print(g)

for guidabile in g:
    guidabile.guida()
