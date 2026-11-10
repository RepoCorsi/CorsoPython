"""
Il gestore di un negozio associa a tutti i suoi Prodotti un codice a barre
univoco, una descrizione del prodotto e il suo prezzo, oltre al cliente
che lo acquista (da cui si ricavano età e numero tessera).

La classe Prodotto ha un metodo applica_sconto che riduce il prezzo del
5% solo se il cliente ha più di 60 anni.

Ai prodotti Alimentari è associata una data di scadenza; ai prodotti
NonAlimentari il materiale principale (carta, vetro, plastica...).

Le due sottoclassi ridefiniscono applica_sconto: sconto ulteriore del 20%
per gli Alimentari vicini alla scadenza (10 giorni), del 10% per i
NonAlimentari fatti di materiale riciclabile.
"""

from datetime import date


# NOTA: vedi la spiegazione già fatta in 02_studente.py sul perché qui
# ripetiamo una versione compatta di Persona invece di importarla.
class Persona:

    def __init__(self, nome, cognome, eta):
        self._nome = nome
        self._cognome = cognome
        self._eta = eta

    def get_nome(self):
        return self._nome

    def get_eta(self):
        return self._eta

    def __str__(self):
        return "la persona si chiama " + self._nome + " ha " + str(self._eta) + " anni"


class Cliente(Persona):

    # NOTA: un attributo scritto direttamente dentro il corpo della
    # classe (fuori da __init__) è condiviso da TUTTI gli oggetti Cliente:
    # è l'equivalente Python di un campo "static" in Java. Appartiene
    # alla classe, non al singolo oggetto.
    numero_tessera = 0

    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        Cliente.numero_tessera += 1  # incremento l'attributo di classe
        self.tessera_cliente = Cliente.numero_tessera  # lo assegno all'attributo dell'oggetto

    def __str__(self):
        return "Cliente: " + super().__str__() + " numero tessera:" + str(self.tessera_cliente)


class Prodotto:

    # equivalente Python del campo static di Java: appartiene alla
    # classe Prodotto, non ai singoli oggetti creati da essa
    codice = 0

    def __init__(self, descrizione, prezzo, c):
        Prodotto.codice += 1  # incremento l'attributo di classe
        self.cod_prodotto = Prodotto.codice  # lo assegno all'attributo dell'oggetto
        self._descrizione = descrizione
        # NOTA: Java distingue "protected" (visibile alle sottoclassi,
        # ma non a tutto il resto del programma) da "private" (visibile
        # solo qui). Python non fa questa distinzione: l'underscore
        # iniziale è la stessa identica convenzione sia per "privato" sia
        # per "protetto", e le sottoclassi vi accedono comunque.
        self.prezzo = prezzo
        self.c = c  # riferimento alla classe Cliente

    def applica_sconto(self):
        """Applica lo sconto del 5% ai clienti con più di 60 anni."""
        if self.c.get_eta() > 60:
            self.prezzo -= (self.prezzo * 5) / 100

    def get_cod_prodotto(self):
        return self.cod_prodotto

    def get_descrizione(self):
        return self._descrizione

    def set_descrizione(self, descrizione):
        self._descrizione = descrizione

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def get_cliente(self):
        return self.c

    def set_cliente(self, c):
        self.c = c

    def __str__(self):
        return "Prodotto " + str(self.cod_prodotto) + ", descrizione=" + self._descrizione + ", prezzo=" + str(self.prezzo)


class ProdottiAlimentari(Prodotto):

    def __init__(self, data_scadenza, descrizione, prezzo, c):
        super().__init__(descrizione, prezzo, c)
        self._data_scadenza = data_scadenza

    def applica_sconto(self):
        """Applica lo sconto se il prodotto è vicino alla scadenza (10 gg)."""
        # calcolo la differenza tra 2 date
        giorni_tra_2_date = (self._data_scadenza - date.today()).days

        if giorni_tra_2_date < 10:  # sconto se vicino alla scadenza
            self.prezzo -= self.prezzo * 0.2  # 20%
        super().applica_sconto()  # sconto per età>60 (dalla classe Prodotto)

    def __str__(self):
        return super().__str__() + " data Scadenza: " + str(self._data_scadenza)


class ProdNonAlimentari(Prodotto):

    def __init__(self, materiale, descrizione, prezzo, c):
        super().__init__(descrizione, prezzo, c)
        self.materiale = materiale

    def applica_sconto(self):
        if self.materiale.lower() in ("carta", "vetro", "plastica"):
            self.prezzo -= self.prezzo * 0.1
        super().applica_sconto()  # ulteriore sconto da Prodotto se età>60

    def get_materiale(self):
        return self.materiale

    def set_materiale(self, materiale):
        self.materiale = materiale

    def __str__(self):
        return super().__str__() + " materiale=" + self.materiale


# ================== PROVA (equivalente del "main" di Java) ==================

c = Cliente("mario", "rossi", 65)
p = []

# aggiungiamo 2 prodotti non alimentari
p.append(ProdNonAlimentari("vetro", "Specchio", 10, c))
p.append(ProdNonAlimentari("plastica", "penna", 10, c))

# aggiungiamo 2 prodotti alimentari
d_latte = date(2024, 11, 13)
p.append(ProdottiAlimentari(d_latte, "Latte", 10, c))

d_carne = date(2024, 11, 13)
p.append(ProdottiAlimentari(d_carne, "Manzo", 10, c))

print(c)  # --> stampo il cliente

for prodotto in p:
    prodotto.applica_sconto()  # --> polimorfismo
    print(prodotto)  # stampo le informazioni di tutti i prodotti
