'''
# # #mmagina di voler rappresentare delle automobili in un programma.
# # La classe è il progetto che descrive come sarà un'automobile.
# # L'oggetto è una singola automobile costruita seguendo quel progetto.
# # Gli attributi sono le caratteristiche dell'automobile, come marca e colore.
# # I metodi sono le azioni che può compiere, come accelerare.

La Programmazione Orientata agli Oggetti (OOP) in Python è un modello di programmazione che permette di strutturare il codice combinando dati (attributi) e comportamenti (metodi) in entità chiamate oggetti.

La classe è il progetto o lo stampo (es. il disegno di un'auto). L'oggetto è l'istanza reale creata da quel progetto (es. la tua auto parcheggiata sotto casa). Il metodo __init__ è il costruttore: viene eseguito automaticamente quando crei un nuovo oggetto e serve a inizializzarne i dati.
'''

class Auto:
    # Il costruttore inizializza gli attributi di istanza
    def __init__(self, marca, modello): #Creo gli attributi dentro __init__
        self.marca = marca        # Attributo di istanza
        self.modello = modello    # Attributo di istanza

    # Un metodo è una funzione interna alla classe che agisce sull'oggetto
    def descrivi(self): #obbligatotrio il self come primo parametro. Senza self è una funzione interna alla classe, non un metodo. Non si può choamare.
        return f"Questa è una {self.marca} {self.modello}."

# self rappresenta l'oggetto specifico che sta chiamando il metodo.
# Indica a Python di modificare o leggere i dati di quella precisa istanza.

    def parti(self):
        print("sto partendo")

    def fermati(self):
        print("mi sto fermando")

# Creazione degli oggetti (istanze)
auto1 = Auto("Fiat", "500")
auto2 = Auto("Tesla", "Model 3")

print(auto1.descrivi())  # Output: Questa è una Fiat 500.
print(auto2.descrivi())  # Output: Questa è una Fiat 500.

auto1.parti()
auto1.fermati()

#posso aggiungere delle proprietà anche dopo:
auto1.colore="rosso"

print(auto1.colore)

# #stampo la descrizione della classe
print(auto1.__dict__) #per vedere come un dizionario come è fatta la classe
print(auto2.__dict__) #per vedere come un dizionario come è fatta la classe

print(dir(auto1)) #attributi e metodi dell'oggetto

#----------------------------------------------------------------------------------------
#--ATTRIBUTI DI ISTANZA VS ATTRIBUTI DI CLASSE

# • Attributi di istanza: Variabili specifiche di ogni singolo oggetto (ogni auto ha il suo colore o modello). Si definiscono con self.
# • Attributi di classe: Variabili CONDIVISE da TUTTE le istanze della classe. 
# Si definiscono direttamente nel corpo della classe, fuori dai metodi. Se cambia nella classe, cambia per tutti.

class Chitarra:
    # Attributo di classe: comune a tutte le chitarre create
    numero_corde = 6

    def __init__(self, marca):
        self.marca = marca  # Attributo di istanza

# Creiamo due auto
chitarra_a = Chitarra("Fender")
chitarra_b = Chitarra("Gibson")

print(chitarra_a.numero_corde)  # Output: 6
print(chitarra_b.numero_corde)  # Output: 6

# Se modifichiamo l'attributo di classe, cambia per tutte le istanze
Chitarra.numero_corde = 12 # SI CHIAMA COL NOME DELLA CLASSE, NON DEGLI OGGETTI!!!
print(chitarra_a.numero_corde)  # Output: 12
print(chitarra_b.numero_corde)  # Output: 12

#--------------------------------------------------------------------------------

class ContoBancario:
    def __init__(self, intestatario, saldo):
        self.intestatario = intestatario
        self.saldo = saldo

    def deposita(self, importo): #modifica il saldo
        if importo <= 0:
            print("Importo non valido")
            return
        self.saldo += importo
        print(f"Deposito di {importo}€ effettuato")

    def mostra_saldo(self): #visualizza il saldo
        print(f"{self.intestatario} ha un saldo di: {self.saldo} euro")


conto = ContoBancario("Marco", 100)

conto.mostra_saldo() 

conto.deposita(50)

conto.mostra_saldo()

#  --- DA FARE DOPO!!! -----


#----------------------------------------------------------------
# PER ASSEGNARE UNA FUNZIONE AD UN OGGETTO SOLO(NON A TUTTA LA CLASSE)

class Auto:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

auto1 = Auto("Fiat", "500")
auto2 = Auto("Tesla", "Model 3")

# 1. Definiamo una funzione esterna che accetta un oggetto 
def clacson_singolo_oggetto(oggetto):
    return f"La {oggetto.marca} {oggetto.modello} fa Beep Beep!"

# 2. La assegniamo SOLO a auto1
auto1.suona = clacson_singolo_oggetto

# 3. La usiamo (passando l'oggetto stesso come argomento)
print(auto1.suona(auto1))  # Output: La Fiat 500 fa Beep Beep!

#------
# PER ASSEGNARE UNA FUNZIONE A TUTTA LA CLASSE, non ad un oggetto solo

# 1. Definiamo la funzione esterna (con il parametro 'self')
def clacson_globale(self):
    return f"La {self.marca} {self.modello} fa BOOM BOOM!"

# 2. La iniettiamo nella CLASSE Auto (non nell'oggetto)
Auto.suona_globale = clacson_globale

# 3. Ora TUTTI gli oggetti, vecchi e nuovi, hanno questo metodo!
print(auto1.suona_globale())  # Output: La Fiat 500 fa BOOM BOOM!
print(auto2.suona_globale())  # Output: La Tesla Model 3 fa BOOM BOOM!

print(dir(auto1)) ##attributi e metodi dell'oggetto 
#--------------

# --- SETATTR ---
# Permette di aggiungere o modificare attributi e metodi di un oggetto o di una classe in modo dinamico, utilizzando le stringhe.
# Scrivere setattr(auto1, "colore", "rosso") produce lo stesso identico risultato di auto1.colore = "rosso".

auto1.targa="ab123cd"
setattr(auto1, "targa", "ab123cd") # è la stessa cosa di sopra auto1.marca="ab123cd"

print("la targa è:",auto1.targa)

print(auto1.__dict__) #solo attributi
#print(dir(auto1)) #attributi e metodi

# ESEMPIO: Aggiungere attributi in blocco con un ciclo
# Immaginiamo di avere dati extra che arrivano, ad esempio, da un database o da un file JSON
caratteristiche_extra = {
    "colore": "rosso",
    "alimentazione": "elettrica",
    "anno": 2024
}

# Aggiungiamo tutto dinamicamente usando setattr
for chiave, valore in caratteristiche_extra.items():
    setattr(auto1, chiave, valore)

# Ora l'oggetto ha tutti i nuovi attributi!
print(auto1.colore)         # Output: rosso
print(auto1.alimentazione)  # Output: elettrica
print(auto1.anno)           # Output: 2024

#----------------------------------------------------------

# ---- AGGIUNGERE METODI CON SETATTR:

# 1. Definiamo la funzione esterna DA AGGIUNGERE ALLA CLASSE
def clacson_dinamico(self):
    return f"Beep da {self.marca}!"

# 2. Definiamo il nome del metodo tramite una stringa
# nome_metodo = "suona_clacson"

# 3. Iniettiamo la funzione nella CLASSE usando setattr
setattr(Auto, "suona_clacson", clacson_dinamico)

# 4. Ora il metodo è richiamabile normalmente da tutte le istanze!
print(auto1.suona_clacson())  # Output: Beep da Fiat!
print(auto2.suona_clacson())  # Output: Beep da Fiat!

#-----------------------------------------------------------------------------------

# ------ ESEMPIO COMPLESSIVO: ---------------

# Il Personaggio di un Gioco

# Creiamo un personaggio che inizialmente sa solo camminare. 
# Nel corso del gioco, controlleremo se sa volare (un metodo) e se possiede uno scudo (un attributo). 
# Se non li ha, glieli assegneremo dinamicamente.

class Personaggio:
    def __init__(self, nome):
        self.nome = nome

    def cammina(self):
        return f"{self.nome} sta camminando."

# 1. Creiamo il nostro eroe
eroe = Personaggio("Arthur")

# --- PARTE 1: Gestire un ATTRIBUTO (lo Scudo) ---
print("--- Controllo Attributo ---")

# Cerchiamo l'attributo 'scudo'. Se non esiste, getattr restituisce None (il terzo parametro)
valore_scudo = getattr(eroe, "scudo", None) #possiamo restituire il valore che vogliamo. In questo caso None

if valore_scudo is None:
    print("Arthur non ha uno scudo. Glielo assegno ora!")
    # Aggiungiamo l'attributo dinamicamente
    setattr(eroe, "scudo", "Scudo di Legno")
else:
    print(f"Arthur ha già lo scudo: {valore_scudo}")

# Ora che è stato aggiunto, lo leggiamo con sicurezza
print(f"Equipaggiamento attuale: {eroe.scudo}")


# --- PARTE 2: Gestire un METODO (Volare) ---
print("\n--- Controllo Metodo ---")

# Definiamo la funzione esterna che diventerà il nostro metodo
def vola_funzione(self):
    return f"{self.nome} sta volando"


# Cerchiamo il metodo 'vola' sull'oggetto eroe
metodo_vola = getattr(eroe, "vola", None)

if metodo_vola is None:
    print("Arthur non sa volare. Gli insegno l'abilità!")
    
    # IMPORTANTE: Se aggiungiamo una funzione a un singolo OGGETTO (e non alla classe),
    # dobbiamo passargli manualmente 'self' tramite una funzione lambda, 
    # oppure iniettare la funzione direttamente nella CLASSE per fare in modo che Python gestisca 'self' da solo.
    # Optiamo per iniettarla nella CLASSE Personaggio in modo che l'uso sia pulito.
    setattr(Personaggio, "vola", vola_funzione)
    
    # Ora che è nella classe, lo recuperiamo aggiornato per l'eroe
    metodo_vola = getattr(eroe, "vola")

# Eseguiamo il metodo (essendo una funzione, dobbiamo aggiungere le parentesi tonde `()`)
print(metodo_vola())

# -------------------------------

# -- RIDEFINIRE SETATTR ---
# -- Se devo applecare la stessa logica su puù attributi: Per esempio tutti devono essere >0
#Posso anche ridefinire il metodo setattr in questo modo:

class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def __setattr__(self, nome, valore): # intercetta l'assegnazione e applica la logica
        if nome in ("base", "altezza") and valore <= 0:
            raise ValueError(f"{nome} deve essere maggiore di zero")

        object.__setattr__(self, nome, valore)

rettangolo = Rettangolo(3, 4)

rettangolo.base = 5    # OK
rettangolo.altezza = 6   # OK

# rettangolo.base = -2   # ValueError
# rettangolo.altezza = 0   # ValueError

print(rettangolo.base)
print(rettangolo.altezza)

#------------------------------------------------------------

#  __SLOTS__
# BLOCCARE DEL TUTTO L'AGGIUNTA DI NUOVI ATTRIBUTI USANDO __SLOTS__

class Rectangle:
    # Definiamo rigorosamente QUALI attributi sono ammessi
    __slots__ = ("width", "height") #solo questi sono gli attributi della classe e basta

    def __init__(self, width, height):
        self.width = width
        self.height = height

# 1. Creazione dell'oggetto
rettangolo = Rectangle(10, 20)

# 2. Modificare gli attributi consentiti funziona normalmente
rettangolo.width = 15 
print(rettangolo.width)  # Output: 15

# 3. TENTATIVO DI AGGIUNGERE UN NUOVO ATTRIBUTO
try:
    rettangolo.colore = "rosso"  # Questo solleverà un errore!
except AttributeError as e:
    print(f"Errore intercettato: {e}")
    # Output: Errore intercettato: 'Rectangle' object has no attribute 'colore'
