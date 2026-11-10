# NOTA: come già visto in Altri_esempi, qui riuniamo in un unico file
# tutte le piccole classi che in Java stavano ciascuna nel proprio file
# (vincolo di Java, non di Python).

# ********************* Esercizio 1: Contatore *********************
class Contatore:

    def __init__(self, numero):
        self.numero = numero

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def aumenta_numero(self):
        self.numero += 1

    def diminuisci_numero(self):
        self.numero -= 1


# ------------- Esercizio 1: Contatore -------------
c = Contatore(10)
c.aumenta_numero()
print(c.get_numero())
c.diminuisci_numero()
c.set_numero(100)
print(c.get_numero())

# ********************* Esercizio 2: Rettangolo *********************
class Rettangolo:

    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def ridimensiona(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def perimetro(self):
        return (self.base + self.altezza) * 2

    def area(self):
        return self.base * self.altezza


# ------------- Test-------------
r = Rettangolo(5, 3)
print(r.area())
print(r.perimetro())
r.ridimensiona(6, 6)
print(r.area())
print(r.perimetro())


# ********************* Esercizio 3: Lampadina *********************
class Lampadina:

    def __init__(self, acceso):
        self.acceso = acceso
        self.n_accensioni = 0

    def is_rotta(self):  # dopo quanti click si rompe
        return self.n_accensioni >= 3

    def stato(self):
        if self.is_rotta():
            return "lampadina rotta!"
        return "Accesa" if self.acceso else "spenta"

    def click(self):
        self.acceso = not self.acceso
        self.n_accensioni += 1
        print(self.stato())


# ------------- Test -------------
l = Lampadina(True)
print(l.stato())
l.click()
l.click()
l.click()



# ********************* Esercizio 4: Appartamento *********************
class Appartamento:

    def __init__(self, nome_proprietario, numero_inquilini):
        self.nome_proprietario = nome_proprietario
        # NOTA: in Java superficie/piano sono "private final", inizializzati
        # direttamente sull'attributo (100 e 2 per ogni appartamento): qui
        # usiamo la convenzione "_underscore + MAIUSCOLO" per segnalare
        # sia che sono "privati" sia che, per convenzione, non andrebbero
        # più modificati (vedi anche la nota su "final" già fatta più volte)
        self._SUPERFICIE = 100
        self._PIANO = 2
        self.numero_inquilini = numero_inquilini

    def visualizza(self):
        print("Le caratteristiche dell'appartamento sono: superficie:", self._SUPERFICIE,
              "Nome proprietario:", self.nome_proprietario,
              "Piano:", self._PIANO,
              "Numero Inquilini", self.numero_inquilini)

    def cambia_proprietario(self, nome_proprietario):
        self.nome_proprietario = nome_proprietario

    def set_numero_inquilini(self, numero_inquilini):
        self.numero_inquilini = numero_inquilini

# ------------- Test -------------
a1 = Appartamento("Fabio", 3)
a1.visualizza()
a1.cambia_proprietario("ugo")
a1.set_numero_inquilini(2)
a1.visualizza()



# ********************* Esercizio 5: Automobile *********************
class Automobile:

    def __init__(self, marca, modello, livello_carburante):
        self.marca = marca
        self.modello = modello
        self.livello_carburante = livello_carburante

    def guida(self):
        self.livello_carburante -= 1

    def stato_carburante(self):
        return self.livello_carburante

    def fai_rifornimento(self, livello_carburante):
        self.livello_carburante += livello_carburante

    def visualizza(self):
        print(self.marca, self.modello, self.livello_carburante)


# -------------Test -------------
auto = Automobile("fiat", "panda", 10)
print(auto.stato_carburante())
auto.guida()
auto.guida()
auto.guida()
print(auto.stato_carburante())
auto.fai_rifornimento(20)
print(auto.stato_carburante())
auto.visualizza()



# ********************* Esercizio 6: ContoCorrente *********************

'''
Creare una classe conto corrente che, a fronte di un deposito iniziale, e del nome del cliente, assegnati automaticamente al momento dell'apertura del conto, permetta di:
prelevare,
versare dei soldi, 
vedere il saldo, 
visualizzare un riepilogo del nome e del saldo del conto 
Il numero di conto deve essere un numero progressivo diverso per ogni cliente, e assegnato in modo automatico dal sistema.
Fare i controlli nel caso il conto vada in rosso, e in quel caso impedire di prelevare.

'''

class ContoCorrente:

    n_conto = 0  # equivalente Python di "static int nConto": appartiene alla classe

    def __init__(self, nome, saldo):
        ContoCorrente.n_conto += 1  # incrementiamo il contatore di tutta la classe
        self.numero = ContoCorrente.n_conto  # assegniamo l'ultimo valore generato all'oggetto
        self.nome = nome
        self.saldo = saldo

    def deposito(self, quantita):
        self.saldo += quantita

    def prelievo(self, quantita):
        if self.rosso():
            raise Exception("Hai finito i soldi!")
        elif self.saldo < quantita:
            raise Exception("Prelievo oltre la disponibilità")
        self.saldo -= quantita

    def get_saldo(self):
        return self.saldo

    def rosso(self):
        return self.saldo <= 0

    def __str__(self):
        # NOTA: format(x, ".2f") è l'equivalente Python di DecimalFormat("0.00")
        return "cc numero: " + str(self.numero) + " di " + self.nome + " ha un saldo di " + format(self.saldo, ".2f")

# ------------- Test -------------
conto = ContoCorrente("Fabio", 10)
conto.deposito(100)
print(format(conto.get_saldo(), ".2f"))
conto.deposito(150.30)
print(format(conto.get_saldo(), ".2f"))
try:
    conto.prelievo(15000)
except Exception as e:
    print(e)
print(format(conto.get_saldo(), ".2f"))
print(conto)

# per vedere che il numero di conto (static) si incrementa di 1 ogni volta
conto1 = ContoCorrente("aa", 10)
print(conto1)

conto2 = ContoCorrente("bb", 20)
print(conto2)



# ********************* Esercizio 7: Prodotti *********************
class Prodotti:

    def __init__(self, codice, descrizione, prezzo):
        self.codice = codice
        self.descrizione = descrizione
        self.prezzo = prezzo

    def applica_sconto(self, sconto):
        self.prezzo -= (self.prezzo * sconto) / 100

    def get_codice(self):
        return self.codice

    def get_descrizione(self):
        return self.descrizione

    def get_prezzo(self):
        return self.prezzo

# ------------- Test -------------
p = Prodotti(1, "mouse", 20)
p.applica_sconto(10)
print("il prezzo del prodotto è:", format(p.get_prezzo(), ".2f"))




# ********************* Dipendente *********************

'''Progettare una classe di nome Dipendente. 
Tale classe prevede tre variabili di istanza, nome di tipo String, età di tipo int  e stipendio di tipo double. 

Scrivere un costruttore senza parametri, un costruttore con due parametri (nome e stipendio).

La classe deve inoltre implementare i metodi get e set per tutti gli attributi, e il toString .
Aggiungere poi un metodo aumenta, che incrementi lo stipendio del dipendente di una certa percentuale solo se l'età del dipendente è >50. 

Scrivere una classe col metodo main per testare il programma, dichiarare un array di Impiegati e calcolare il totale degli stipendi.
'''

class Dipendente:

    def __init__(self, nome=None, stipendio=0):
        self.nome = nome
        self.eta = 0
        self.stipendio = stipendio

    def aumenta(self, percentuale):
        if self.eta > 50:
            self.stipendio += (self.stipendio * percentuale) / 100
            print("aumentato lo stipendio a", self.nome, "del", percentuale, "%")
        else:
            print("aumento non concesso ad", self.nome)

# ------------- Test -------------
d = Dipendente("Ugo", 2000)
d.set_eta(48)
d.aumenta(10)
print(d.get_stipendio())

d1 = Dipendente("Gino", 3000)
d1.set_eta(55)
d1.aumenta(10)
print(d1.get_stipendio())

d2 = Dipendente("Pino", 4000)
d2.set_eta(60)
d2.aumenta(10)
print(d2.get_stipendio())

arr_dip = [d, d1, d2]

tot = 0
for dip in arr_dip:
    tot += dip.get_stipendio()

print("la somma degli stipendi è", tot)


