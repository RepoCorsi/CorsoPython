from abc import ABC, abstractmethod

# NOTA: una classe è astratta se ha almeno un metodo astratto. È una
# classe non completamente definita e non può essere istanziata
# direttamente. Si usa quando non è possibile definire un'implementazione
# comune per un metodo (esempio: il decollo è diverso per ogni tipo di
# veivolo).


class Veivolo(ABC):

    def __init__(self, modello, velocita_massima):
        self.modello = modello
        self.velocita_massima = velocita_massima

    def descrizione(self):
        print("La velocità massima di un", self.modello, "è:", self.velocita_massima)

    # devono essere implementati dalle classi che ereditano da Veivolo
    @abstractmethod
    def decollo(self):
        pass

    @abstractmethod
    def atterraggio(self):
        pass


class Boeing747(Veivolo):

    def decollo(self):
        print("Il 747 ha bisogno di una pista molto lunga per il decollo ...")

    def atterraggio(self):
        print("Il 747 ha bisogno di una pista molto lunga per l'atterraggio...")


class Elicottero(Veivolo):

    def decollo(self):
        print("L'elicottero decolla da fermo ...")

    def atterraggio(self):
        print("L'elicottero atterra in verticale ...")


class Idrovolante(Veivolo):

    def decollo(self):
        print("L'idrovolante può decollare dall'acqua o da una pista ...")

    def atterraggio(self):
        print("L'idrovolante può atterrare nell'acqua o su una pista...")


# ================== PROVA (equivalente del "main" di Java) ==================

b = Boeing747("747", 590)
b.descrizione()
b.decollo()
b.atterraggio()

print()

eli = Elicottero("Pegaso3", 1190)
eli.descrizione()
eli.decollo()
eli.atterraggio()

print()

idro = Idrovolante("Cessna Anfibio", 213)
idro.descrizione()
idro.decollo()
idro.atterraggio()

print("***************************")
v = [b, eli, idro]
for veivolo in v:
    veivolo.descrizione()
    veivolo.decollo()
    veivolo.atterraggio()
