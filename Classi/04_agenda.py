class Impegno:

    def __init__(self, descrizione):
        self._descrizione = descrizione  # incapsulamento

    def get_descrizione(self):
        return self._descrizione

    def set_descrizione(self, descrizione):
        self._descrizione = descrizione

    def __str__(self):
        return self._descrizione

    # NOTA: come già visto nel modulo Generics, quando un oggetto finisce
    # dentro una lista che a sua volta viene stampata, Python usa
    # __repr__ (non __str__) per decidere cosa mostrare: qui li rendiamo
    # uguali per ottenere lo stesso comportamento di Java.
    __repr__ = __str__


class Pagina:

    def __init__(self, giorno, impegni):
        self.giorno = giorno
        self._impegni = impegni  # un elenco di impegni

    def __str__(self):
        return "Pagina del giorno " + self.giorno + ":\n impegni: " + str(self._impegni) + "\n"

    __repr__ = __str__


class Agenda:

    def __init__(self):
        # NOTA: in Java l'array ha una dimensione fissa dichiarata subito
        # (new Pagina[7], perché i giorni della settimana sono sempre 7).
        # In Python usiamo comunque una lista, come discusso nel modulo
        # sulle liste: qui la creiamo vuota e la riempiamo più avanti con
        # set_pagine().
        self._pagine = []

    def get_pagine(self):
        return self._pagine

    def set_pagine(self, pagine):
        self._pagine = pagine

    def __str__(self):
        return str(self._pagine)


# ================== PROVA (equivalente del "main" di Java) ==================

# definisco gli impegni creando oggetti della classe Impegno
i1 = Impegno("Studiare Python")
i2 = Impegno("Andare in posta")
i3 = Impegno("Fare la spesa")
i4 = Impegno("Fare l'aperitivo")
i5 = Impegno("Pulire casa")

# associo gli impegni al giorno della settimana
impegni_lunedi = [i1, i2, i3]
impegni_martedi = [i1, i4, i5]
impegni_mercoledi = [i1, i4]
impegni_giovedi = [i5, i3, i2]
# .
# .
# ...così fino a domenica

# creo la pagina e le passo giorno e impegni
p1 = Pagina("Lunedì", impegni_lunedi)
p2 = Pagina("Martedì", impegni_martedi)
p3 = Pagina("Mercoledì", impegni_mercoledi)
p4 = Pagina("Giovedì", impegni_giovedi)
# .
# .
# ...così fino a domenica

# creo l'agenda settimanale
a = Agenda()

# definisco la lista con tutte le pagine che abbiamo creato
sette_pagine = [p1, p2, p3, p4]  # ...così fino a p7

# assegno le pagine alla settimana
a.set_pagine(sette_pagine)

# stampo tutto
print(a)  # __str__ di Agenda

# for pagina in sette_pagine:
#     print(pagina)
#     print("---------------")
