#CLASSI ASTRATTE ->ABC ->ABSTRACT DATA CLASSES

# Una classe astratta è una classe che non può essere istanziata direttamente (non puoi creare un oggetto di quella classe) perchè incompleta.
# VA SEMPRE EREDITATA! Serve esclusivamente come "MODELLO DI BASE" per le classi figlie. 
# Se una classe figlia eredita da una classe astratta, DEVE OBBLIGATORIAMENTE IMPLEMENTARE tutti i metodi definiti come astratti (@abstractmethod).
# Si usa il modulo nativo abc (Abstract Base Classes)

## IMPORTANTE!! IMPORTARE LE CLASSI ASTRATTE PER POTER CREARE ALTRE CLASSI ASTRATTE!!

# Se un metodo è astratto (dichiarato ma senza corpo), tutta la classe
# diventa astratta.
#
# l'errore non si presenta quando si prova davvero a creare un
# oggetto della sottoclasse incompleta.
from abc import ABC, abstractmethod # ABSTRACT BASE CLASS


class Animale(ABC):  # ereditare da ABC rende la classe astratta

    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta

    # un metodo decorato con @abstractmethod non ha un corpo "utile":
    # obbliga le sottoclassi a ridefinirlo
    @abstractmethod
    def parla(self):
        pass

    @abstractmethod
    def mangia(self):
        pass

    def __str__(self):
        return "Animale [nome=" + self._nome + ", eta=" + str(self._eta) + "]"


# se estendo una classe astratta, sono obbligato a ridefinire (override)
# tutti i suoi metodi astratti
class Cane(Animale):

    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def parla(self):
        print("bau bau")

    def mangia(self):
        print("mangio le ossa")


class Gatto(Animale):

    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def parla(self):
        print("miao miao")

    def mangia(self):
        print("il topo")


class Topo(Animale):

    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def parla(self):
        print("squit squit")

    def mangia(self):
        print("mangio il formaggio")


# ================== PROVA (equivalente del "main" di Java) ==================

# a = Animale("prova", 1)  # TypeError: non si può istanziare una classe astratta

a = [Cane("boby", 10), Gatto("milu", 5), Topo("miky", 7)]

for animale in a:
    print(animale)
    # polimorfismo
    animale.parla()
    animale.mangia()
