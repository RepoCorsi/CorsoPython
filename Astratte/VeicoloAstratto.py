from abc import ABC, abstractmethod

# 1. Veicolo eredita da ABC per diventare una classe astratta
class Veicolo(ABC):

    def __init__(self, nome, ruote):
        self._nome = nome
        self._ruote = ruote

    # 2. Definiamo i metodi astratti senza un'implementazione reale
    @abstractmethod
    def parti(self):
        pass

    @abstractmethod
    def ferma(self):
        pass

    def __str__(self):
        return "Veicolo: nome=" + self._nome + ", ruote=" + str(self._ruote)

# Le classi Macchina, Bicicletta e Treno rimangono identiche a prima
class Macchina(Veicolo):

    def __init__(self, nome, ruote, porte):
        super().__init__(nome, ruote)
        self.porte = porte

    def parti(self):
        print("parto con la benzina")

    def ferma(self):
        print("mi fermo col freno a mano")

    def __str__(self):
        return super().__str__() + " porte " + str(self.porte)


class Bicicletta(Veicolo):

    def __init__(self, nome, ruote, pedali):
        super().__init__(nome, ruote)
        self.pedali = pedali

    def parti(self):
        print("parto con i pedali")

    def ferma(self):
        print("mi fermo con le manopole")

    def __str__(self):
        return super().__str__() + " pedali=" + str(self.pedali)


class Treno(Veicolo):

    def __init__(self, nome, ruote, numero_vagoni):
        super().__init__(nome, ruote)
        self._numero_vagoni = numero_vagoni

    def parti(self):
        print("Il treno parte dalla stazione con", self._numero_vagoni, "vagoni")

    def ferma(self):
        print("il treno si ferma alla stazione")

    def __str__(self):
        return super().__str__() + " numero Vagoni " + str(self._numero_vagoni)
