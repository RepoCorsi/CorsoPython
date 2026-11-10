from abc import ABC, abstractmethod


class Abbigliamento(ABC):

    def __init__(self, taglia, prezzo, colore, quantita):
        self._taglia = taglia
        self.prezzo = prezzo  # "protected" in Java: qui è solo una convenzione, vedi nota nel file 05_negozio.py
        self._colore = colore
        self._quantita = quantita

    @abstractmethod
    def applica_sconto(self):
        pass

    def get_taglia(self):
        return self._taglia

    def set_taglia(self, taglia):
        self._taglia = taglia

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def get_colore(self):
        return self._colore

    def set_colore(self, colore):
        self._colore = colore

    def get_quantita(self):
        return self._quantita

    def set_quantita(self, quantita):
        self._quantita = quantita

    def __str__(self):
        return ("taglia=" + self._taglia + ", prezzo=" + str(self.prezzo)
                + ", colore=" + self._colore + ", quantita=" + str(self._quantita))


class Maglia(Abbigliamento):

    def __init__(self, taglia, prezzo, colore, quantita, tipo):
        super().__init__(taglia, prezzo, colore, quantita)
        self.tipo = tipo

    def applica_sconto(self):
        if self.get_quantita() > 2 and self.get_colore().lower() == "rosso" and self.tipo.lower() == "felpa":
            prezzo_scontato = self.prezzo - (self.prezzo * 0.1)
            print("Sconto Applicato, nuovo prezzo", prezzo_scontato)
            return prezzo_scontato
        else:
            print("Sconto NON applicato")
            return self.prezzo

    def __str__(self):
        return self.tipo + " " + super().__str__()


class Pantaloni(Abbigliamento):

    def __init__(self, taglia, prezzo, colore, quantita, modello):
        super().__init__(taglia, prezzo, colore, quantita)
        self.modello = modello

    def applica_sconto(self):
        if self.modello.lower() == "bermuda" and self.get_taglia().lower() == "xl":
            prezzo_scontato = self.prezzo - (self.prezzo * 0.1)
            print("Sconto applicato, nuovo prezzo", prezzo_scontato)
            return prezzo_scontato
        else:
            print("Sconto NON applicato")
            return self.prezzo

    def get_modello(self):
        return self.modello

    def set_modello(self, modello):
        self.modello = modello

    def __str__(self):
        return self.modello + " " + super().__str__()


# ================== PROVA (equivalente del "main" di Java) ==================

felpa = Maglia("m", 20, "rosso", 20, "felpa")
tshirt = Maglia("l", 10, "bianca", 10, "tshirt")
bermuda = Pantaloni("Xl", 20, "blu", 20, "bermuda")
jeans = Pantaloni("s", 30, "nero", 20, "jeans")

a = [felpa, tshirt, bermuda, jeans]

totale = 0
for abbigliamento in a:
    print(abbigliamento)
    prezzo_scontato = abbigliamento.applica_sconto()  # polimorfismo
    totale = abbigliamento.get_quantita() * prezzo_scontato

print("totale speso=", totale)
