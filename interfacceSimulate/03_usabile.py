from abc import ABC, abstractmethod


# Gestisce i comportamenti, non è gerarchica (non descrive un "è un", ma
# un "sa fare questo").
# NOTA: in Java "implements" è la parola chiave usata apposta per le
# interfacce (al posto di "extends" usato per le classi). In Python la
# sintassi è identica in entrambi i casi: si scrive semplicemente il nome
# della classe/interfaccia tra parentesi.
class Usabile(ABC):

    @abstractmethod
    def usa(self):
        pass


class Computer(Usabile):

    def usa(self):
        print("il pc si usa con la tastiera")


class Macchina(Usabile):

    def usa(self):
        print("Sto guidando")


class Martello(Usabile):

    def usa(self):
        print("pianto i chiodi")


# ================== PROVA (equivalente del "main" di Java) ==================

def utilizza(u):  # funzione che accetta in input elementi che "sono Usabile"
    u.usa()


arr_usabili = [Computer(), Macchina(), Martello()]

for usabile in arr_usabili:
    usabile.usa()  # polimorfismo

c = Computer()
m = Martello()
utilizza(c)
utilizza(m)
