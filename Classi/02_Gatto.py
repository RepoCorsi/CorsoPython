class Gatto:
    def __init__(self, nome, razza, eta):
        # Gli attributi vengono creati direttamente assegnandoli a 'self'.
        self.nome = nome
        self.razza = razza
        self.eta = eta

    # Metodi di comportamento della classe
    def miagola(self):
        print("miao miao")

    def mangia(self, cibo):
        print(f"sto mangiando {cibo}")

    def fai_le_fusa(self):
        print("prrr prrr")

    def is_anziano(self):
         # Un gatto è considerato anziano se ha più di 10 anni
        return self.eta >= 11

    # L'equivalente del metodo toString() di Java è il metodo speciale __str__()
    # Viene invocato automaticamente quando usiamo print() sull'oggetto o lo convertiamo in stringa
    def __str__(self):
        return f"{self.nome} {self.razza} {self.eta}"

    # L'equivalente del metodo equals() di Java è il metodo speciale __eq__()
    # Definisce cosa succede quando usiamo l'operatore di uguaglianza '==' tra due oggetti
    def __eq__(self, other):
        # Verifichiamo se l'altro oggetto è un'istanza della classe Gatto
        if isinstance(other, Gatto):
            # Confrontiamo i valori dei singoli attributi (uguaglianza strutturale)
            return (self.eta == other.eta and
                    self.razza == other.razza and
                    self.nome == other.nome)
        return False


# Il blocco seguente permette di eseguire questo file direttamente per testare la classe

print("--- CREAZIONE DEGLI OGGETTI ---")
# Creiamo tre istanze della classe Gatto
gatto1 = Gatto("Fuffi", "Persiano", 12)
gatto2 = Gatto("Silvestro", "Europeo", 5)
gatto3 = Gatto("Fuffi", "Persiano", 12) # Stessi identici dati di gatto1

print("\n--- TEST METODI DI COMPORTAMENTO ---")
gatto1.miagola()
gatto1.mangia("i croccantini")
gatto1.fai_le_fusa()

print("\n--- TEST LOGICA DI BUSINESS (is_anziano) ---")
print(f"{gatto1.nome} è anziano? {gatto1.is_anziano()}") # True (ha 12 anni)
print(f"{gatto2.nome} è anziano? {gatto2.is_anziano()}") # False (ha 5 anni)

print("\n--- TEST RAPPRESENTAZIONE TESTUALE (toString / __str__) ---")
# Stampando l'oggetto, Python chiama automaticamente il metodo __str__
print("Stampa gatto1:", gatto1)
print("Stampa gatto2:", gatto2)

print("\n--- TEST UGUAGLIANZA (equals / ==) ---")
# In Python, l'operatore '==' mappa direttamente sul metodo __eq__ se questo è definito.
# Non abbiamo bisogno di chiamare .equals() come in Java!
print(f"gatto1 è uguale a gatto2? {gatto1 == gatto2}") # False (dati diversi)
print(f"gatto1 è uguale a gatto3? {gatto1 == gatto3}") # True (stessi dati)

