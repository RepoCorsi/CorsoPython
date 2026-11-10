"""
NOTA DELL'AUTORE ORIGINALE: il file Java segnala esplicitamente
"PROGRAMMA DIFFICILE!! NON PER CORSI DI BASE!!": usa una TreeMap (mappa
sempre ordinata per chiave) e un Comparator con method reference. Per
questo motivo qui ci concediamo, in via eccezionale, un paio di
strumenti più avanzati di Python (in particolare una funzione lambda
per il criterio di ordinamento), che nel resto del corso abbiamo sempre
evitato finché non necessari: qui lo sono, perché il materiale Java di
partenza è a sua volta segnalato come avanzato.
"""
from datetime import date


class Alimento:

    def __init__(self, codice_barre, nome, data_scadenza):
        self.codice_barre = codice_barre
        self.nome = nome
        self.data_scadenza = data_scadenza

    def get_codice_barre(self):
        return self.codice_barre

    def get_nome(self):
        return self.nome

    def get_data_scadenza(self):
        return self.data_scadenza

    def get_giorni_rimanenti(self):
        oggi = date.today()
        return (self.data_scadenza - oggi).days

    def __str__(self):
        return self.nome + " (Codice: " + self.codice_barre + ", Giorni rimanenti: " + str(self.get_giorni_rimanenti()) + ")"

    __repr__ = __str__


class FrigoriferoScadenza:

    def __init__(self):
        # NOTA: come già visto in 02_collections/04_map.py, Python non
        # ha un vero equivalente di TreeMap nella libreria standard: un
        # dict normale mantiene l'ordine di INSERIMENTO, non quello
        # alfabetico delle chiavi. Qui, dato che l'ordine con cui
        # inseriamo gli alimenti non ci interessa (li ordiniamo comunque
        # per data quando li visualizziamo), un dict normale va benissimo.
        self.frigorifero = {}

    def inserisci_alimento(self, codice_barre, nome, data_scadenza):
        alimento = Alimento(codice_barre, nome, data_scadenza)
        self.frigorifero[codice_barre] = alimento
        print("Alimento inserito correttamente.")

    def rimuovi_alimento(self, codice_barre):
        alimento = self.frigorifero.pop(codice_barre, None)
        if alimento is not None:
            print("Alimento rimosso correttamente.")
        else:
            print("L'alimento specificato non è presente nella cella frigorifera.")

    def visualizza_alimenti(self):
        if len(self.frigorifero) == 0:
            print("Nessun alimento presente nella cella frigorifera.")
        else:
            print("Alimenti presenti nella cella frigorifera (ordinati per scadenza):")
            # NOTA: Comparator.comparing(Alimento::getDataScadenza) di Java
            # diventa, in Python, il parametro "key" di sorted(): una
            # funzione che indica in base a cosa ordinare. Qui usiamo una
            # lambda solo perché il criterio è troppo piccolo per
            # meritare una funzione con un nome a parte.
            alimenti = sorted(self.frigorifero.values(), key=lambda a: a.get_data_scadenza())
            for alimento in alimenti:
                print(alimento)

    def visualizza_prossima_scadenza(self):
        if len(self.frigorifero) == 0:
            print("Nessun alimento presente nella cella frigorifera.")
        else:
            print("Alimento più vicino alla scadenza:")
            prossima_scadenza = None
            for alimento in self.frigorifero.values():
                if prossima_scadenza is None or alimento.get_giorni_rimanenti() < prossima_scadenza.get_giorni_rimanenti():
                    prossima_scadenza = alimento
            print(prossima_scadenza)


# ================== PROVA (equivalente del "main" di Java) ==================

frigo = FrigoriferoScadenza()
scelta = 0

while scelta != 5:
    print("\nMenu di gestione della cella frigorifera:")
    print("1) Inserimento di un alimento")
    print("2) Rimozione di un alimento")
    print("3) Visualizzazione di tutti gli alimenti")
    print("4) Visualizzazione dell'alimento più vicino alla scadenza")
    print("5) Uscita")

    scelta = int(input("Seleziona una funzione (1-5): "))

    if scelta == 1:
        codice_barre = input("Inserisci il codice a barre dell'alimento: ")
        nome = input("Inserisci il nome dell'alimento: ")
        # NOTA: LocalDate.parse() di Java diventa date.fromisoformat()
        # in Python, che si aspetta lo stesso identico formato AAAA-MM-GG.
        data_scadenza = date.fromisoformat(input("Inserisci la data di scadenza (formato AAAA-MM-GG): "))
        frigo.inserisci_alimento(codice_barre, nome, data_scadenza)
    elif scelta == 2:
        codice_barre = input("Inserisci il codice a barre dell'alimento da rimuovere: ")
        frigo.rimuovi_alimento(codice_barre)
    elif scelta == 3:
        frigo.visualizza_alimenti()
    elif scelta == 4:
        frigo.visualizza_prossima_scadenza()
    elif scelta == 5:
        print("Uscita dal programma.")
    else:
        print("Scelta non valida. Riprova.")
