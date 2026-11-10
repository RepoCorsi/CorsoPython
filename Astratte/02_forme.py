import math
from abc import ABC, abstractmethod


class FormaAstratta(ABC):

    def __init__(self, lato, tipo):
        self._lato = lato
        self._tipo = tipo

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def get_lato(self):
        return self._lato

    def set_lato(self, lato):
        self._lato = lato

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return "FormaAstratta [lato=" + str(self._lato) + ", tipo=" + self._tipo + "]"


class Rettangolo(FormaAstratta):

    def __init__(self, lato, tipo, altezza):
        super().__init__(lato, tipo)
        self.altezza = altezza

    def area(self):
        return self.get_lato() * self.altezza

    def perimetro(self):
        return (self.get_lato() + self.altezza) * 2


class Quadrato(Rettangolo):

    def __init__(self, lato, tipo):
        super().__init__(lato, tipo, lato)

    def area(self):
        return self.get_lato() * self.get_lato()

    def perimetro(self):
        return (self.get_lato() * self.get_lato()) * 2


class Triangolo(FormaAstratta):

    def __init__(self, lato, tipo):
        super().__init__(lato, tipo)

    def area(self):
        return (self.get_lato() * self.get_lato()) / 2

    def perimetro(self):  # triangolo equilatero
        return self.get_lato() * 3


class Cerchio(FormaAstratta):

    def __init__(self, lato, tipo):
        super().__init__(lato, tipo)
        self.pi_greco = math.pi

    def area(self):
        return self.get_lato() * self.get_lato() * self.pi_greco

    def perimetro(self):
        return 2 * self.pi_greco * self.get_lato()  # il lato per noi è il raggio


# ================== PROVA (equivalente del "main" di Java) ==================

f = []

print("inserisci le dimensioni di base e altezza")
base = float(input())
altezza = float(input())
print("inserisci il raggio")
raggio = float(input())

f.append(Rettangolo(base, "Rettangolo", altezza))
f.append(Triangolo(base, "Triangolo"))
f.append(Cerchio(raggio, "Cerchio"))
f.append(Quadrato(base, "Quadrato"))

# NOTA: Java qui usa f.forEach(forme -> {...}), con una lambda expression.
# Le liste di Python non hanno un metodo forEach: l'idioma normale è
# sempre il for-each, che qui fa esattamente lo stesso lavoro.
for forme in f:
    print(forme)
    print("Area:", forme.area())
    print("Perimetro:", forme.perimetro())
