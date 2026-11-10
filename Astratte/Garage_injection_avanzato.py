from abc import ABC, abstractmethod

# ==========================================
# 1. PARTE: VEICOLI (Logica di Core)
# ==========================================
class Veicolo(ABC):
    def __init__(self, nome, ruote):
        self.nome = nome
        self.ruote = ruote

    @abstractmethod
    def parti(self):
        pass
        
    @abstractmethod
    def ferma(self):
        pass

    #@property #permtte di usare il metodo tipo come se fosse un parametro. veicolo.tipo 
    @abstractmethod
    def tipo(self):
        pass

    def __str__(self):
        return f"veicolo: {self.nome}, ruote= {self.ruote}"


class Macchina(Veicolo): 
    @property
    def tipo(self): 
        return "Macchina"
    
    def parti(self): print(f"🚗 '{self.nome}' parte.")
    def ferma(self): print(f"🚗 '{self.nome}' si ferma.")    


class Bicicletta(Veicolo):
    @property
    def tipo(self): 
        return "Bicicletta"
    
    def parti(self): print(f"🚲 '{self.nome}' parte.")
    def ferma(self): print(f"🚲 '{self.nome}' si ferma.")    


# ==========================================
# 2. PARTE: INFRASTRUTTURA DI PAGAMENTO
# ==========================================
class CassaAutomatica:
    def __init__(self):
        self._listino_prezzi = {"Macchina": 2.50, "Bicicletta": 0.00}
        self._incasso_totale = 0.0

    def calcola_e_incassa(self, tipo_veicolo, ore):
        """Calcola la tariffa, la accumula nell'incasso e restituisce l'importo"""
        tariffa_oraria = self._listino_prezzi.get(tipo_veicolo, 1.50)
        costo = ore * tariffa_oraria
        self._incasso_totale += costo
        return costo

    def mostra_resoconto(self):
        print(f"💰 [CASSA] Incasso totale accumulato: {self._incasso_totale:.2f} €")


# ==========================================
# 3. PARTE: IL GARAGE (Sfrutta la Dependency Injection)
# ==========================================
class Garage:
    # La cassa viene INIETTATA dal costruttore
    def __init__(self, nome_garage, posti_massimi, cassa_servizio):
        self.nome_garage = nome_garage
        self.posti_massimi = posti_massimi
        self._veicoli_parcheggiati = []
        self._cassa = cassa_servizio  # Salviamo la dipendenza iniettata

    def parcheggia(self, veicolo: Veicolo):
        if len(self._veicoli_parcheggiati) >= self.posti_massimi:
            print(f"🛑 Garage Pieno! Impossibile parcheggiare '{veicolo.nome}'.")
            return
        print(f"\n[Ingresso] '{veicolo.nome}' entra nel {self.nome_garage}.")
        veicolo.ferma()
        self._veicoli_parcheggiati.append(veicolo)

    def fai_uscire(self, nome_veicolo, ore_sosta: int):
        for veicolo in self._veicoli_parcheggiati:
            if veicolo.nome == nome_veicolo:
                print(f"\n[Uscita] '{veicolo.nome}' ({veicolo.tipo}) esce dopo {ore_sosta} ore:")
                
                # Delega il calcolo e l'incasso alla cassa iniettata
                importo = self._cassa.calcola_e_incassa(veicolo.tipo, ore_sosta)
                print(f"💳 Importo pagato alla cassa: {importo:.2f} €")
                
                veicolo.parti()
                self._veicoli_parcheggiati.remove(veicolo)
                return
        print(f"🔍 Veicolo '{nome_veicolo}' non trovato.")


# ==========================================
# TEST DEL SISTEMA DISACCOPPIATO
# ==========================================

# Creiamo prima l'infrastruttura di pagamento autonoma
cassa_principale = CassaAutomatica()

# Creiamo il garage INIETTANDO la cassa appena nata
mio_garage = Garage("Central Parking", 2, cassa_principale)

# Istanziamo i veicoli
auto = Macchina("Fiat Panda", 4)
bici = Bicicletta("Rockrider", 2)

# Movimenti nel garage
mio_garage.parcheggia(auto)
mio_garage.parcheggia(bici)

mio_garage.fai_uscire("Fiat Panda", ore_sosta=3) # 3 ore * 2.50€ = 7.50€
mio_garage.fai_uscire("Rockrider", ore_sosta=2)  # Gratis

# Possiamo interrogare direttamente la cassa indipendentemente dal garage!
print("\n--- Fine Giornata ---")
cassa_principale.mostra_resoconto()
