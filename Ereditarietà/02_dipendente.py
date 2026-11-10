"""
Progettare una classe Dipendente, sottoclasse di Persona.
Tale classe prevede le variabili di istanza nome, cognome, età (da Persona)
e stipendio.

Scrivere i vari costruttori e i metodi get()/set() per tutti gli attributi,
e il metodo __str__.
Aggiungere poi un metodo aumenta(percentuale), che incrementi lo stipendio
del dipendente di una certa percentuale solo se l'età del dipendente è >50.

Dichiarare una lista di dipendenti e calcolare il totale degli stipendi.
"""
class Persona:

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def get_nome(self):
        return self.nome

    def get_eta(self):
        return self.eta

    def __str__(self):
        return "la persona si chiama " + self.nome + " ha " + str(self.eta) + " anni"


class Dipendente(Persona):

    def __init__(self, stipendio, nome, cognome, eta):
        super().__init__(nome, cognome, eta)  # costruttore di Persona
        self.stipendio = stipendio

    # metodo che aumenta lo stipendio solo se l'età è > 50
    def aumenta(self, percentuale):
        if self.get_eta() > 50:  # get_eta() arriva da Persona
            self.stipendio += (self.stipendio * percentuale) / 100
            print("aumentato lo stipendio a", self.get_nome(), ". Nuovo stipendio:", self.stipendio)
        else:
            print("aumento non concesso a", self.get_nome())

    def get_stipendio(self):
        return self.stipendio

    def set_stipendio(self, stipendio):
        self.stipendio = stipendio

    def __str__(self):
        return super().__str__() + " stipendio= " + str(self.stipendio)


# ================== PROVA (equivalente del "main" di Java) ==================

"""
Progettare una classe Dipendente, sottoclasse di Persona.
Tale classe prevede le variabili di istanza nome, cognome, età (da Persona)
e stipendio. Scrivere i vari costruttori e i metodi get()/set() per tutti
gli attributi, e il metodo __str__. Aggiungere poi un metodo aumenta
(percentuale), che incrementi lo stipendio del dipendente di una certa
percentuale solo se l'età del dipendente è >50.
Dichiarare una lista di dipendenti e calcolare il totale degli stipendi.
"""


def dip_max_stipendio(dipendenti):  # dipendente con lo stipendio massimo
    massimo = 0
    d2 = None
    for dipendente in dipendenti:
        if dipendente.get_stipendio() > massimo:
            massimo = dipendente.get_stipendio()
            d2 = dipendente
    return d2


d = []
somma = 0

d.append(Dipendente(1000, "mario", "rossi", 20))
d.append(Dipendente(5000, "giuseppe", "verdi", 55))
d.append(Dipendente(3000, "aldo", "bianchi", 60))

for dipendente in d:
    print(dipendente)  # __str__
    dipendente.aumenta(10)
    somma += dipendente.get_stipendio()

print("somma stipendi", somma)

dip_massimo = dip_max_stipendio(d)
print("Il dipendente con lo Stipendio massimo è:", dip_massimo)
