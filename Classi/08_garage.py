# --- 1. CLASSE COMPRESA NELLA COMPOSIZIONE ---
class Motore:
    def __init__(self, cavalli, tipo_carburante):
        self.cavalli = cavalli
        self.tipo_carburante = tipo_carburante

    def avvia(self):
        return f"Vrumm! Motore {self.tipo_carburante} da {self.cavalli} CV avviato."


# --- 2. CLASSE PRINCIPALE (Usa Composizione) ---
class Macchina:
    def __init__(self, marca, modello, cavalli, carburante): #Quando creo una macchina creo anche l'oggetto motore. Sono legati
        self.marca = marca
        self.modello = modello
        
        # COMPOSIZIONE PURA: L'oggetto Motore nasce QUI dentro.
        # Se un oggetto Macchina viene rimosso, anche questo specifico motore cessa di esistere.
        self.motore = Motore(cavalli, carburante)

    def accendi_auto(self):
        # Deleghiamo il comportamento all'oggetto interno
        return f"La {self.marca} {self.modello} si accende: {self.motore.avvia()}"


# --- 3. CLASSE CONTENITORE (Usa Aggregazione e __len__) ---
class Garage:
    def __init__(self, nome):
        self.nome = nome
        self.veicoli = []  # Aggregazione: conterrà le macchine create fuori

    #principio Open/Closed (aperto alle estensioni(posso passare un camio, estensione di macchina), ma chiuso alle modifiche).
    def parcheggia(self, macchina):  #dependency injection (Iniettiamo la macchina dentro la classe Garage) 
        self.veicoli.append(macchina)

    # DUNDER METHOD: Permette di usare len(oggetto_garage)
    def __len__(self):
        # Restituiamo la lunghezza della lista interna
        return len(self.veicoli)

    def elenco(self):
        if not self.veicoli:
            print("Il garage è vuoto.")
        for v in self.veicoli:
            print(f"- {v.marca} {v.modello} ({v.motore.cavalli} CV)")


# --- ESECUZIONE DEL CODICE ---

# Creiamo le macchine (Nota: non passiamo oggetti Motore, passiamo solo i dati per crearlo)
auto1 = Macchina("Fiat", "500", 70, "Ibrida")
auto2 = Macchina("Porsche", "Sportiva", 450, "Benzina")

# Test della composizione: l'auto accede al suo motore interno
print(auto1.accendi_auto()) # Output: La Fiat 500 si accende: Vrumm! Motore Ibrida da 70 CV avviato.
print(auto2.accendi_auto()) #La Porsche Sportiva si accende: Vrumm! Motore Benzina da 450 CV avviato.


# Creiamo il Garage (Aggregazione)
mio_garage = Garage("Garage Centrale")

# Parcheggiamo le auto
mio_garage.parcheggia(auto1)
mio_garage.parcheggia(auto2)

print("\n--- Stato del Garage ---")
# Usiamo il metodo __len__ nativamente con la funzione len() di Python
print(f"Nel garage ci sono attualmente {len(mio_garage)} veicoli.")
# Output: Nel garage ci sono attualmente 2 veicoli.

mio_garage.elenco()
