from abc import ABC, abstractmethod

# 1. Strumento diventa una classe astratta ereditando da ABC
class Strumento(ABC):
    def __init__(self, nome):
        self.nome = nome

    # 2. Il metodo suona diventa un metodo astratto obbligatorio
    @abstractmethod
    def suona(self):
        pass

    def __str__(self):
        return f"Strumento{{nome={self.nome}}}"


class Chitarra(Strumento):
    def __init__(self, nome, numero_corde):
        super().__init__(nome)
        self.numero_corde = numero_corde

    def suona(self):
        print("la chitarra suona con le corde")


class Pianoforte(Strumento):
    def __init__(self, numero_tasti, nome):
        super().__init__(nome)
        self.numero_tasti = numero_tasti

    def suona(self):
        print("il pianoforte si suona con i tasti")


class Tromba(Strumento):
    def __init__(self, nome, numero_tasti):
        super().__init__(nome)
        self.numero_tasti = numero_tasti

    def suona(self):
        print("La tromba suona con l'aria")
