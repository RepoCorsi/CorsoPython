from abc import ABC, abstractmethod


class Interfaccia1(ABC):
    # implicitamente "public static final" in Java: qui è un attributo di classe
    stringa1 = "Ciao dall'interfaccia 1"


class Interfaccia2(ABC):
    stringa2 = "Ciao dall'interfaccia 2"


class Interfaccia3(ABC):
    # implicitamente "public abstract" in Java
    @abstractmethod
    def stampa(self):
        pass


# NOTA: in Java, un'interfaccia può estendere PIÙ interfacce insieme con
# "extends Interfaccia1, Interfaccia2, Interfaccia3" (un'altra eccezione
# rispetto alle classi, che estendono sempre e solo una classe sola).
# In Python questa distinzione, come già visto, non esiste: è la STESSA
# identica sintassi dell'ereditarietà multipla già usata per le classi.
class Interfaccia4(Interfaccia1, Interfaccia2, Interfaccia3):
    stringa3 = "Ciao dall'interfaccia 4"


class ImplementaInterfacce(Interfaccia4):

    def stampa(self):
        print("ho ereditato tutte le stringhe delle interfacce e implementato il metodo")


# ================== PROVA (equivalente del "main" di Java) ==================

i = ImplementaInterfacce()
print(i.stringa1)
print(i.stringa2)
print(i.stringa3)

i.stampa()
