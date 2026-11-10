from datetime import date

# NOTA: qui ripetiamo ancora la versione compatta di Persona (con
# attributo eta pubblico, coerente con la nuova Persona di
# 01_persona_aggiornata.py, da cui questo file dipende davvero).
class Persona:

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return "la persona si chiama " + self.nome + " ha " + str(self.eta) + " anni"


class Cliente(Persona):

    # equivalente Python di "static int numeroTessera": condiviso da
    # tutti i clienti (vedi anche 05_oop/02_ereditarieta/05_negozio.py)
    numero_tessera = 0

    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        Cliente.numero_tessera += 1
        self.tessera_cliente = Cliente.numero_tessera

    def __str__(self):
        return "Cliente{" + super().__str__() + " numeroTessera=" + str(self.tessera_cliente) + "}"


class Prodotti:

    codice = 0  # attributo di classe: equivalente di "static int codice"

    def __init__(self, descrizione, prezzo, c):
        Prodotti.codice += 1
        self.cod_prodotto = Prodotti.codice
        self.descrizione = descrizione
        # "protected" in Java: qui è solo una convenzione (vedi nota già
        # fatta in 05_oop/02_ereditarieta/05_negozio.py); ci serve nelle
        # sottoclassi
        self.prezzo = prezzo
        self.c = c  # riferimento al Cliente che acquista

    def applica_sconto(self):
        """5% di sconto ai clienti con più di 60 anni."""
        if self.c.eta > 60:
            self.prezzo -= (self.prezzo * 5) / 100

    def get_codice(self):
        return Prodotti.codice

    def get_descrizione(self):
        return self.descrizione

    def set_descrizione(self, descrizione):
        self.descrizione = descrizione

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def get_cliente(self):
        return self.c

    def set_cliente(self, c):
        self.c = c

    def __str__(self):
        # NOTA: qui non mettiamo il cliente nella stringa, altrimenti si
        # ripeterebbe per ogni prodotto nel ciclo (stesso commento
        # presente nel file Java originale)
        return "Prodotti{codice=" + str(self.cod_prodotto) + ", descrizione=" + self.descrizione + ", prezzo=" + str(self.prezzo) + "}"


class ProdottiAlimentari(Prodotti):

    def __init__(self, data_scadenza, descrizione, prezzo, c):
        super().__init__(descrizione, prezzo, c)
        self.data_scadenza = data_scadenza

    def applica_sconto(self):
        """Sconto se il prodotto è vicino alla scadenza (10 giorni)."""
        giorni_tra_2_date = (self.data_scadenza - date.today()).days
        if giorni_tra_2_date < 10:
            self.prezzo -= self.prezzo * 0.2  # 20%
        # NOTA: qui, a differenza della versione vista in
        # 05_oop/02_ereditarieta/05_negozio.py, lo sconto per età>60
        # della classe padre NON viene più sommato (la chiamata
        # super().applica_sconto() è commentata, come nel Java originale):
        # super().applica_sconto()

    def __str__(self):
        return super().__str__() + " data scadenza " + str(self.data_scadenza)


class ProdNonAlimentari(Prodotti):

    def __init__(self, materiale, descrizione, prezzo, c):
        super().__init__(descrizione, prezzo, c)
        self.materiale = materiale

    def applica_sconto(self):
        if self.materiale.lower() in ("carta", "vetro", "plastica"):
            self.prezzo -= self.prezzo * 0.1  # 10%
        # super().applica_sconto()  # anche qui non si somma più allo sconto della classe padre

    def get_materiale(self):
        return self.materiale

    def set_materiale(self, materiale):
        self.materiale = materiale

    def __str__(self):
        return super().__str__() + " Materiale: " + self.materiale


# ================== PROVA (equivalente del "main" di Java) ==================

c = Cliente("mario", "rossi", 65)
p = []

# Prodotti Non Alimentari
p.append(ProdNonAlimentari("vetro", "Specchio", 10, c))
p.append(ProdNonAlimentari("plastica", "penna", 10, c))

# Prodotti Alimentari (mettere una data successiva a oggi per NON avere lo sconto)
d_latte = date(2024, 3, 29)  # data di scadenza latte (nel passato: sconto applicato)
p.append(ProdottiAlimentari(d_latte, "latte", 10, c))

d_carne = date(2024, 3, 29)  # data di scadenza carne
p.append(ProdottiAlimentari(d_carne, "carne", 10, c))

print(c)  # stampo il Cliente

for prodotti in p:
    prodotti.applica_sconto()  # polimorfismo: applico gli sconti ai prodotti
    print(prodotti)  # stampo tutti i prodotti
