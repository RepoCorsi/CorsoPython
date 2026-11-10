from abc import ABC, abstractmethod


class Multimedia(ABC):

    def __init__(self, titolo, durata):
        self.titolo = titolo  # "protected" in Java: qui è solo una convenzione
        self.durata = durata

    @abstractmethod
    def riproduci(self):
        pass

    def get_titolo(self):
        return self.titolo

    def set_titolo(self, titolo):
        self.titolo = titolo

    def get_durata(self):
        return self.durata

    def set_durata(self, durata):
        self.durata = durata

    def __str__(self):
        return "titolo=" + self.titolo + ", durata=" + str(self.durata)


class Canzone(Multimedia):

    def __init__(self, titolo, durata, autore):
        super().__init__(titolo, durata)
        self.autore = autore

    def riproduci(self):
        print("Sto riproducendo la canzone", self.get_titolo())

    def get_autore(self):
        return self.autore

    def set_autore(self, autore):
        self.autore = autore

    def __str__(self):
        return super().__str__() + " autore=" + self.autore


class Film(Multimedia):

    def __init__(self, titolo, durata, numero_visualizzazioni):
        super().__init__(titolo, durata)
        self.numero_visualizzazioni = numero_visualizzazioni

    def riproduci(self):
        print("Sto riproducendo il film", self.get_titolo())

    def get_numero_visualizzazioni(self):
        return self.numero_visualizzazioni

    def set_numero_visualizzazioni(self, numero_visualizzazioni):
        self.numero_visualizzazioni = numero_visualizzazioni

    def __str__(self):
        return super().__str__() + " numero visualizzazioni=" + str(self.numero_visualizzazioni)


class Riproducibile(ABC):

    @abstractmethod
    def play(self, multimedia):
        pass


class Audio(Riproducibile):

    def play(self, multimedia):
        for m in multimedia:
            if isinstance(m, Canzone):  # equivalente di "instanceof"
                m.riproduci()
                print(m)
                print("---------------")


class Video(Riproducibile):

    def play(self, multimedia):
        for m in multimedia:
            if isinstance(m, Film):
                m.riproduci()
                print(m)
                print("------------------")


# ================== PROVA (equivalente del "main" di Java) ==================

playlist = [
    Canzone("Canzone1", 5, "Autore1"),
    Canzone("Canzone2", 3, "Autore2"),
    Film("Film1", 60, 1000),
    Film("Film2", 120, 5000),
]

# audio e video hanno in comune il fatto di poter essere riprodotti,
# quindi condividono la stessa "interfaccia" Riproducibile
r = [Audio(), Video()]

for riproducibile in r:
    # il metodo play riproduce un elemento multimediale (canzone o film)
    riproducibile.play(playlist)
