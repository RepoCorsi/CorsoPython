from abc import ABC, abstractmethod

# 1. DEFINIAMO LA CLASSE ASTRATTA (Il contratto comune)
class ProfessionistaCucina(ABC):
    @abstractmethod
    def cucina(self, piatto):
        """Ogni cuoco specializzato DEVE implementare questo metodo"""
        pass


# 2. CREIAMO LE CLASSI FIGLIE (Le specializzazioni con logiche diverse)
class Pizzaiolo(ProfessionistaCucina):
    def cucina(self, piatto):
        print(f"🔥 [Forni a Legna] Il pizzaiolo stende l'impasto e inforna: {piatto}!")

class Pasticcere(ProfessionistaCucina):
    def cucina(self, piatto):
        print(f"🎂 [Laboratorio Dolce] Il pasticcere monta la panna e decora: {piatto}!")


# 3. LA CLASSE CAMERIERE (Sfrutta il polimorfismo tramite Aggregazione)
class Cameriere:
    # Il cameriere accetta un qualunque "ProfessionistaCucina" (Dependency Injection)
    def __init__(self, nome, cuoco: ProfessionistaCucina):
        self.nome = nome
        self.cuoco = cuoco

    def prendi_ordini(self, piatto):
        print(f"🛒 Il cameriere {self.nome} prende nota dell'ordine: '{piatto}'")
        # POLIMORFISMO IN AZIONE: 
        # Il cameriere chiama sempre lo stesso metodo (.cucina), 
        # ma l'effetto cambierà totalmente in base al cuoco assegnato!
        self.cuoco.cucina(piatto)


# --- ESECUZIONE DEL SOFTWARE ---

# Creiamo i nostri specialisti della cucina
mario = Pizzaiolo()
luigi = Pasticcere()

print("--- Turno di Pranzo (In cucina c'è Mario) ---")
# Diamo il pizzaiolo Mario al cameriere Ambrogio
ambrogio = Cameriere("Ambrogio", mario)
ambrogio.prendi_ordini("Pizza Margherita")

print("\n--- Turno di Cena (In cucina c'è Luigi) ---")
# Cambiamo il cuoco al volo (Aggregazione dinamica) passando il pasticcere Luigi
ambrogio.cuoco = luigi
ambrogio.prendi_ordini("Torta di Compleanno")
