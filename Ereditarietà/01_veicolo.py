class Veicolo:

    def __init__(self, nome, ruote):
        self._nome = nome
        self._ruote = ruote

    def parti(self):
        print("il veicolo parte")

    def ferma(self):
        print("il veicolo si ferma")

    # def get_nome(self):
        # return self._nome

    # def set_nome(self, nome):
        # self._nome = nome

    # def get_ruote(self):
        # return self._ruote

    # def set_ruote(self, ruote):
        # self._ruote = ruote

    def __str__(self):
        return "Veicolo: nome=" + self._nome + ", ruote=" + str(self._ruote)


# una classe può estendere solo un'altra classe (Python è un po' più
# flessibile e in casi avanzati permette l'eredità multipla, ma non è
# questo l'argomento di questa lezione)
class Macchina(Veicolo):

    def __init__(self, nome, ruote, porte):
        super().__init__(nome, ruote)  # deve essere la prima istruzione, per convenzione
        self.porte = porte

    # NOTA: Java usa l'annotazione @Override per segnalare che questo
    # metodo esisteva già nella superclasse e lo stiamo ridefinendo.
    # Python non ha un'annotazione equivalente: basta ridefinire il
    # metodo con lo stesso nome, e Python capisce da solo che stiamo
    # sovrascrivendo quello della classe padre.
    def parti(self):
        print("parto con la benzina")

    def ferma(self):
        print("mi fermo col freno a mano")

    def __str__(self):
        # super() permette di richiamare il metodo della classe padre,
        # esattamente come "super." in Java
        return super().__str__() + " porte " + str(self.porte)


class Bicicletta(Veicolo):

    def __init__(self, nome, ruote, pedali):
        super().__init__(nome, ruote)
        self.pedali = pedali

    def parti(self):
        print("parto con i pedali")

    def ferma(self):
        print("mi fermo con le manopole")

    def __str__(self):
        return super().__str__() + " pedali=" + str(self.pedali)


class Treno(Veicolo):

    def __init__(self, nome, ruote, numero_vagoni):
        super().__init__(nome, ruote)
        self._numero_vagoni = numero_vagoni

    def parti(self):
        print("Il treno parte dalla stazione con", self._numero_vagoni, "vagoni")

    def ferma(self):
        print("il treno si ferma alla stazione")

    def __str__(self):
        return super().__str__() + " numero Vagoni " + str(self._numero_vagoni)


# ================== PROVA (equivalente del "main" di Java) ==================

m = Macchina("punto", 4, 5)
print(m)
m.parti()
m.ferma()

b = Bicicletta("Bianchi", 2, 2)
print(b)
b.parti()
b.ferma()

t = Treno("FrecciaRossa", 8, 15)
print(t)
t.parti()
t.ferma()

print("---------------POLIMORFISMO------------------------")

# polimorfismo -> chiamare lo stesso metodo su oggetti diversi
# il polimorfismo si fa solo sui metodi ridefiniti (override)
mezzi_di_trasporto = [m, b, t]
for veicolo in mezzi_di_trasporto:
    print(veicolo)
    veicolo.parti()  # <-- metodo ridefinito
    veicolo.ferma()  # <-- metodo ridefinito


def stampa_info(v):
    v.parti()  # <-- metodo ridefinito nella sottoclasse
    v.ferma()  # <-- metodo ridefinito nella sottoclasse
    
stampa_info(t)
stampa_info(m)
stampa_info(b)
