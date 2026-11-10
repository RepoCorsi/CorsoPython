from abc import ABC, abstractmethod

# Classe Astratta Base
class Strumento(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def suona(self):
        pass

    def __str__(self):
        return f"Strumento{{nome={self.nome}}}"

# Sottoclassi Concrete
class Chitarra(Strumento):
    def __init__(self, nome, numero_corde):
        super().__init__(nome)
        self.numero_corde = numero_corde

    def suona(self):
        print(f"🎸 La chitarra '{self.nome}' suona con le sue {self.numero_corde} corde!")

class Pianoforte(Strumento):
    def __init__(self, numero_tasti, nome):
        super().__init__(nome)
        self.numero_tasti = numero_tasti

    def suona(self):
        print(f"🎹 Il pianoforte '{self.nome}' si suona premendo i suoi {self.numero_tasti} tasti!")

class Tromba(Strumento):
    def __init__(self, nome, numero_tasti):
        super().__init__(nome)
        self.numero_tasti = numero_tasti

    def suona(self):
        print(f"🎺 La tromba '{self.nome}' suona con l'aria e i suoi {self.numero_tasti} pistoni!")


# --- LA CLASSE ORCHESTRA ---
class Orchestra:
    def __init__(self, nome_orchestra):
        self.nome_orchestra = nome_orchestra
        self.strumenti = []  # Lista che conterrà gli strumenti

    def aggiungi_strumento(self, strumento): #DEPENDENCY INJECTION -> INIETTO LA DIPENDENZA CHE MI SERVE (L'OGGETTO STRUMENTO)
        """Aggiunge uno strumento all'orchestra (accetta solo derivati di Strumento)"""
        if isinstance(strumento, Strumento):
            self.strumenti.append(strumento)
            print(f"Aggiunto all'orchestra: {strumento.nome}")
        else:
            print("Errore: Questo non è uno strumento musicale valido!")

    def concerto(self):
        """Fa suonare contemporaneamente tutti gli strumenti dell'orchestra"""
        print(f"\n--- INIZIO CONCERTO della '{self.nome_orchestra}' ---")
        if not self.strumenti:
            print("L'orchestra è vuota... silenzio in sala.")
            return
            
        for strumento in self.strumenti:
            # Polimorfismo: chiama il metodo corretto in base alla classe dell'oggetto
            strumento.suona() #L'ORCHESTRA FA SUONARE LO STRUMENTO. USA IL METODO SUONA DELLA CLASSE STRUMENTO. DELEGHIAMO IL LAVORO ALLA CLASSE STRUMENTO
        print("--- FINE CONCERTO ---\n")


# --- ESECUZIONE DEL PROGRAMMA ---

# 1. Creiamo l'orchestra
mia_orchestra = Orchestra("Sinfonica di Torino")

# 2. Istanziamo i vari strumenti specifici
chitarra_rock = Chitarra("Fender Stratocaster", 6)
piano_gran_coda = Pianoforte(88, "Steinway & Sons")
tromba_jazz = Tromba("Yamaha Custom", 3)

print("--- Reclutamento Musicisti ---")
# 3. Aggiungiamo gli strumenti all'orchestra
mia_orchestra.aggiungi_strumento(chitarra_rock)
mia_orchestra.aggiungi_strumento(piano_gran_coda)
mia_orchestra.aggiungi_strumento(tromba_jazz)

# 4. Diamo il via al concerto!
mia_orchestra.concerto()
