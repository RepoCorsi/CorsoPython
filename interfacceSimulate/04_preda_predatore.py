from abc import ABC, abstractmethod


class Preda(ABC):

    @abstractmethod
    def scappa(self):
        pass


class Predatore(ABC):

    @abstractmethod
    def caccia(self):
        pass


# NOTA: questa è una cosiddetta "interfaccia marcatrice" (marker
# interface): non dichiara nessun metodo, serve solo a "etichettare" un
# gruppo di classi come appartenenti a una stessa categoria, così da
# poterle mettere tutte in una lista dello stesso tipo o riconoscerle con
# un controllo isinstance(). In Python la stessa idea si ottiene con una
# classe vuota, senza nemmeno bisogno di ABC (non c'è nessun metodo da
# rendere obbligatorio).
class I:
    pass


# una classe (o in Java un'interfaccia) può "implementare"/ereditare da
# più tipi contemporaneamente, separandoli con la virgola
class Avvoltoio(Predatore, I):

    def caccia(self):
        print("L'avvoltoio va a caccia di prede")


class Coniglio(Preda, I):

    def scappa(self):
        print("Il coniglio scappa")


class Pesce(Preda, Predatore, I):

    def caccia(self):
        print("Il pesce caccia i pesci più piccoli")

    def scappa(self):
        print("Il pesce scappa dai pesci più grandi")


# ================== PROVA (equivalente del "main" di Java) ==================

prede = [Coniglio(), Pesce()]
predatori = [Avvoltoio(), Pesce()]

for predatore in predatori:
    predatore.caccia()

for preda in prede:
    preda.scappa()

tutto = [Coniglio(), Pesce(), Avvoltoio()]
