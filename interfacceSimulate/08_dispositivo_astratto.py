from abc import ABC, abstractmethod


# la classe superiore diventa a tal punto generica che è meglio pensarla
# come una base per le altre classi piuttosto che come una classe di cui
# creare direttamente un oggetto: è proprio questo il caso d'uso di una
# classe astratta
class Dispositivo(ABC):

    @abstractmethod
    def accendi(self):
        pass


class Televisore(Dispositivo):

    def accendi(self):
        print("Televisore acceso")


class Lampada(Dispositivo):

    def accendi(self):
        print("Lampada accesa")


class Macchina(Dispositivo):

    def accendi(self):
        print("Bruummm")


class Computer(Dispositivo):

    def accendi(self):
        print("Parte windows/Mac/Linux")


# ================== PROVA (equivalente del "main" di Java) ==================

d = [Computer(), Lampada(), Macchina(), Televisore()]

for dispositivo in d:
    dispositivo.accendi()  # polimorfismo
