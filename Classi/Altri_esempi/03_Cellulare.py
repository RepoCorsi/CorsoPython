class Cellulare:

    PREZZO_AL_MINUTO = 0.20  #costante per convenzione (MAIUSCOLO)

    def __init__(self, marca, modello, credito):
        self.marca = marca
        self.modello = modello
        self.credito = credito
        self.numero_chiamate = 0

    def ricarica(self, soldi):
        self.credito += soldi

    def chiamata(self, minuti_durata):
        self.credito -= self.PREZZO_AL_MINUTO * minuti_durata
        self.numero_chiamate += 1

    def get_credito(self):
        return self.credito

    def set_credito(self, credito):
        self.credito = credito

    def get_numero_chiamate(self):
        return self.numero_chiamate

    def credito_esaurito(self):
        return self.credito <= 0

    def __str__(self):
        return ("Cellulare{marca=" + self.marca + ", modello=" + self.modello
                + ", credito=" + str(self.credito) + ", numeroChiamate=" + str(self.numero_chiamate)
                + ", PREZZO_AL_MINUTO=" + str(self.PREZZO_AL_MINUTO) + "}")

# creo un oggetto Cellulare con 20€ di credito e 0 chiamate effettuate
nokia = Cellulare("nokia", "3310", 20.0)

nokia.ricarica(50.0)  # ricarico il cellulare di 50€
nokia.chiamata(13.0)  # chiamata di 13 minuti

print(nokia.get_credito())  # 67.4
print(nokia.get_numero_chiamate())  # 1

nokia.chiamata(20.0)

print(nokia.get_credito())  # 63.4
print(nokia.get_numero_chiamate())  # 2

print("Ho finito i soldi?", nokia.credito_esaurito())