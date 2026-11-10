from abc import ABC, abstractmethod


# NOTA: come già visto in 05_oop/04_interfacce/02_pesabile.py, tutti i
# metodi di un'interfaccia sono astratti a meno che non abbiano un corpo
# (i "metodi default"); gli eventuali attributi sono costanti condivise.
class Pesabile(ABC):

    @abstractmethod
    def pesa(self):
        pass


class Macchina(Pesabile):

    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def pesa(self):
        print("la macchina", self.nome, "pesa", self.peso)


class Studente(Pesabile):

    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def pesa(self):
        print("lo studente", self.nome, "pesa", self.peso)


class Cane(Pesabile):

    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def pesa(self):
        print("il cane", self.nome, "pesa", self.peso)


# ================== PROVA (equivalente del "main" di Java) ==================

p = [Macchina("clio", 3), Studente("ugo", 75), Cane("bobby", 20)]

# polimorfismo
for cose in p:
    cose.pesa()
