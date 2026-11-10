#------------------------------------------------------------------------------------
'''
Creare un sistema che gestisca diverse tipologie di dipendenti, calcoli i loro stipendi in modo polimorfico e tenga traccia del numero totale di dipendenti assunti dall'azienda.

Vogliamo creare una classe base che funga da modello per tutti i dipendenti. 
Non deve essere possibile creare un Dipendente generico, ma solo tipi specifici. 
Inoltre, ogni dipendente deve avere un nome (pubblico) e un codice identificativo aziendale (privato/protetto).
La tua sfida:
1. Crea una classe astratta Dipendente.
2. Aggiungi un metodo costruttore __init__ che accetti nome e id_aziendale. Rendi id_aziendale protetto (usa _id_aziendale).
3. Definisci un metodo astratto chiamato calcola_stipendio(self).


Ora creiamo due tipi di dipendenti reali:
1. DipendenteFisso: Ha uno stipendio mensile fisso.
2. DipendenteOraio: Viene pagato in base alle ore lavorate. Ha una tariffa oraria e il numero di ore lavorate.
'''


from abc import ABC, abstractmethod  #importare ABC, abstractmethod
# La classe eredita da ABC per diventare astratta
class Dipendente(ABC):
    totale_dipendenti = 0 # Attributo di classe
    
    def __init__(self, nome, id_aziendale = None):
        self.nome=nome
        Dipendente.totale_dipendenti+=1 #si incrementa ognio volta che si crea un dipendente
        self._id_aziendale = Dipendente.totale_dipendenti if id_aziendale is None else id_aziendale #se non passiamo id_aziendale mette il progressivo


    @abstractmethod
    def calcola_stipendio(self):
        pass
    
    @property
    def id_aziendale(self):
        return self._id_aziendale
#-----

class DipendenteFisso(Dipendente):
        def __init__(self, nome, stipendio, id_aziendale=None):
            super().__init__(nome, id_aziendale)
            self.stipendio=stipendio

        def calcola_stipendio(self):
            return "Stipendio fisso di",self.stipendio

class DipendenteOrario(Dipendente):
    
        def __init__(self, nome, tariffaOraria, oreLavorate, id_aziendale=None):
            super().__init__(nome, id_aziendale)
            self.stipendio=tariffaOraria
            self.oreLavorate=oreLavorate
            
        def calcola_stipendio(self):
            return "ore lavorate:",self.oreLavorate, "stipendio calcolato:", (self.stipendio*self.oreLavorate)

# --- TEST DEL SOFTWARE ---

# 1. Creiamo i dipendenti
dip1 = DipendenteFisso("mario",1500)
dip2 = DipendenteOrario("laura",40,100)
dip3 = DipendenteFisso("ugo",2000)

# 2. Verifichiamo l'attributo di classe
print(f"Dipendenti totali in azienda: {Dipendente.totale_dipendenti}")

# 3. Verifichiamo il polimorfismo inserendoli in una lista comune
lista_personale = [dip1, dip2, dip3]

print("\n--- Registro Stipendi Mese Corrente ---")
for dip in lista_personale:
    # Python sa autonomamente quale metodo usare grazie al polimorfismo
    print("Dipendente:", dip.nome, "ID:", dip.id_aziendale, " -> Stipendio:", dip.calcola_stipendio(), "€")

# 4. Prova del blocco della Property (Genera errore se decommentato)
# dip1.id_aziendale = "123" # AttributeError: can't set attribute


# print(dipFisso.id_aziendale)
# dipFisso.calcola_stipendio()


# print(dipOrario.id_aziendale)
# dipOrario.calcola_stipendio()
