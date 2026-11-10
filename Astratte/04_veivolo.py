from abc import ABC, abstractmethod


class Veivolo(ABC): #ABSTRACT BASE CLASS

    def __init__(self, modello, velocita_massima):
        self._modello = modello
        self._velocita_massima = velocita_massima

    @abstractmethod
    def decollo(self):
        """Metodo astratto: deve essere implementato dalle sottoclassi."""

    @abstractmethod
    def atterraggio(self):
        """Metodo astratto: deve essere implementato dalle sottoclassi."""

    def __str__(self):
        return "Veivolo [modello=" + self._modello + ", velocitaMassima=" + str(self._velocita_massima) + "]"


class Aereo(Veivolo):

    def __init__(self, modello, velocita_massima):
        super().__init__(modello, velocita_massima)

    def decollo(self):
        print("l'aereo decolla dalla pista")

    def atterraggio(self):
        print("l'aereo atterra sulla pista")

    def __str__(self):
        return super().__str__()


class Elicottero(Veivolo):

    def __init__(self, modello, velocita_massima):
        super().__init__(modello, velocita_massima)

    def decollo(self):
        print("l'elicottero decolla in verticale")

    def atterraggio(self):
        print("l'elicottero atterra in verticale")

    def __str__(self):
        return super().__str__()


class Idrovolante(Veivolo):

    def __init__(self, modello, velocita_massima):
        super().__init__(modello, velocita_massima)

    def decollo(self):
        print("L'idrovolante decolla dall'acqua")

    def atterraggio(self):
        print("L'idrovolante atterra sull'acqua")

    def __str__(self):
        return super().__str__()


# ================== PROVA (equivalente del "main" di Java) ==================

a = Aereo("Boeing 747", 600)
e = Elicottero("Apache", 500)
i = Idrovolante("idro", 300)

v = [a, e, i]

for veivolo in v:
    # polimorfismo
    print(veivolo)
    veivolo.decollo()
    veivolo.atterraggio()
