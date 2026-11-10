class Libro:

    def __init__(self, t, a, p):
        self.titolo = t
        self.autore = a
        self.prezzo = p

    def get_titolo(self):
        return self.titolo

    def get_autore(self):
        return self.autore

    def get_prezzo(self):
        return self.prezzo


class Libreria:

    def __init__(self, nome):
        self.nome = nome
        self.libri = []

    # NOTA: in Java questo è un overload: aggiungiLibri(Libro) e
    # aggiungiLibri(Libro[]) sono 2 metodi diversi. In Python li
    # unifichiamo in uno solo, controllando con isinstance() se ci è
    # stata passata una lista di libri o un libro singolo.
    def aggiungi_libri(self, l):
        if isinstance(l, list):
            self.libri.extend(l)  # equivalente di addAll(Arrays.asList(l))
        else:
            self.libri.append(l)

    def trova_libri(self, a):
        elenco = ""
        for libro in self.libri:
            if libro.get_autore() == a:
                elenco += libro.get_titolo() + " "
        return "Autore " + a + " libri: " + elenco

    def __str__(self):
        elenco = ""
        for libro in self.libri:
            elenco += libro.get_titolo() + " "
        return "Libreria{nome=" + self.nome + ", libri=" + elenco + "}"


# ================== PROVA (equivalente del "main" di Java) ==================

libreria = Libreria("mondadori")

l = Libro("aa", "bb", 10)
libreria.aggiungi_libri(l)
l2 = Libro("xx", "bb", 10)
libreria.aggiungi_libri(l2)

elenco = libreria.trova_libri("bb")
print(elenco)

arr_l = [Libro("aa", "bb", 10), Libro("xx", "bb", 10)]

libreria.aggiungi_libri(arr_l)

elenco2 = libreria.trova_libri("bb")
print(elenco2)

print(libreria)
