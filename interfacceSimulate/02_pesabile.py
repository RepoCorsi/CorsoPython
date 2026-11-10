from abc import ABC, abstractmethod


# nell'interfaccia tutti i metodi sono astratti
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


# NOTA: vedi la spiegazione già fatta in 02_studente.py (modulo
# Ereditarietà) sul perché qui ripetiamo una versione compatta di Persona.
class Persona:

    def __init__(self, nome, cognome, eta):
        self._nome = nome
        self._cognome = cognome
        self._eta = eta

    def get_nome(self):
        return self._nome


# NOTA: qui vediamo il vero punto di forza dell'ereditarietà multipla di
# Python. In Java, Studente "extends Persona implements Pesabile": estende
# UNA classe concreta e implementa un'interfaccia. In Python questa
# distinzione (classe concreta vs interfaccia) sparisce: Studente eredita
# semplicemente da 2 classi contemporaneamente, con la stessa identica
# sintassi.
class Studente(Persona, Pesabile):

    def __init__(self, peso, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        self.peso = peso

    def pesa(self):
        print("lo studente", self.get_nome(), "pesa", self.peso)


# ================== PROVA (equivalente del "main" di Java) ==================

p = [Macchina("fiat", 1000), Studente(70, "Mario", "Rossi", 50)]

for pesabile in p:
    pesabile.pesa()
