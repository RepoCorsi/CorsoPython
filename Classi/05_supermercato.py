from datetime import date


class Prodotto:

    def __init__(self, codice, descrizione, prezzo):
        self._codice = codice
        self._descrizione = descrizione
        self._prezzo = prezzo

    def get_codice(self):
        return self._codice

    def set_codice(self, codice):
        self._codice = codice

    def get_descrizione(self):
        return self._descrizione

    def set_descrizione(self, descrizione):
        self._descrizione = descrizione

    def get_prezzo(self):
        return self._prezzo

    def set_prezzo(self, prezzo):
        self._prezzo = prezzo

    def __str__(self):
        return self._descrizione + ":" + str(self._prezzo) + "€"

    __repr__ = __str__


class Cassa:

    def __init__(self):
        self._prodotti = []
        self._data = date.today()

    # NOTA: come già visto più volte, i 2 metodi leggiProdotto() in
    # overload di Java (uno che riceve i 3 dati separati, uno che riceve
    # già un Prodotto) diventano un solo metodo Python: controlliamo con
    # isinstance() che cosa ci è stato passato in "codice_o_prodotto".
    def leggi_prodotto(self, codice_o_prodotto, descrizione=None, prezzo=None):
        if isinstance(codice_o_prodotto, Prodotto):
            self._prodotti.append(codice_o_prodotto)
        else:
            p = Prodotto(codice_o_prodotto, descrizione, prezzo)
            self._prodotti.append(p)

    def stampa_scontrino(self):
        somma = 0

        # equivalente del DateTimeFormatter di Java con pattern personalizzato
        print(self._data.strftime("Scontrino del %d/%m/%Y"))

        for p in self._prodotti:
            print(p)  # __str__ della classe Prodotto
            somma += p.get_prezzo()  # sommo il prezzo di tutti i prodotti

        # formato con 2 decimali, come il DecimalFormat di Java
        print("il totale della spesa è:", format(somma, ".2f") + "€")

    def piu_costoso(self):  # metodo che restituisce l'oggetto col prezzo più alto
        prezzo_max = 0
        piu_costoso = None

        for prodotto in self._prodotti:
            if prodotto.get_prezzo() > prezzo_max:
                prezzo_max = prodotto.get_prezzo()
                piu_costoso = prodotto
        return piu_costoso  # qui restituisco l'oggetto col prezzo più alto


# ================== PROVA (equivalente del "main" di Java) ==================

print("quanti prodotti hai acquistato?")
n_prodotti = int(input())

cassa1 = Cassa()

print("passa i prodotti sul lettore")

for i in range(n_prodotti):
    print("codice:")
    codice = input()
    print("Descrizione:")
    descrizione = input()
    print("Prezzo:")
    prezzo = float(input())

    p = Prodotto(codice, descrizione, prezzo)
    cassa1.leggi_prodotto(p)

    # cassa1.leggi_prodotto(codice, descrizione, prezzo)

cassa1.stampa_scontrino()
piu_costoso = cassa1.piu_costoso()
print("il prodotto più costoso è", piu_costoso)
