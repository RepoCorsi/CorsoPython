# NOTA GENERALE SUI PACKAGE (concetto in parte diverso):
# in Java un "package" raggruppa più file/classi e influenza anche la
# VISIBILITÀ: un attributo senza modificatore (come "c" qui sotto) è
# visibile solo dentro lo stesso package, anche da altre classi.
#
# In Python il concetto più vicino è il MODULO: ogni file .py è già un
# modulo a sé, e più file nella stessa cartella (con un file speciale
# __init__.py, se serve) formano un PACKAGE, in modo concettualmente
# simile. La differenza importante è sulla visibilità: Python non ha un
# livello "visibile solo nel package": esiste solo la convenzione
# dell'underscore iniziale (vista fin dal modulo sulle basi delle
# classi), che non distingue "privato nel file" da "privato nel
# package": è sempre e solo una convenzione, ovunque si trovi il codice.

class Classe2:

    def __init__(self, a, b):
        self._a = a
        self._b = b
        self._c = None  # in Java sarebbe visibile solo nel package (nessun modificatore)
        self.d = None  # in Java è "public": visibile ovunque, anche da altri package

    def get_a(self):
        return self._a

    def set_a(self, a):
        self._a = a

    def get_b(self):
        return self._b

    def set_b(self, b):
        self._b = b

    def __str__(self):
        return "Classe2 [a=" + self._a + ", b=" + self._b + "]"
