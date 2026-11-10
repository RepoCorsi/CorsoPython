# NOTA: qui ripetiamo ancora la versione compatta di Persona (coerente
# con la nuova Persona con attributi pubblici di
# 06_aggiornamenti_2/03_oop/01_persona_aggiornata.py, da cui questo file
# dipende davvero).
class Persona:

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta


class ContoCorrente:

    def __init__(self, p, saldo):
        self.p = p  # a chi è intestato
        self.saldo = saldo

    def deposito(self, amount):
        self.saldo += amount

    def prelievo(self, amount):
        self.saldo -= amount

    def get_saldo(self):
        return self.saldo

    def info(self):
        # format(x, ".2f") è l'equivalente Python di DecimalFormat("0.00")
        print(self.p.nome, "ha un saldo di", format(self.saldo, ".2f"))


# ================== PROVA (equivalente del "main" di Java) ==================

p = Persona("mario", "rossi", 33)
c = ContoCorrente(p, 10)
c.deposito(100)
print(format(c.get_saldo(), ".2f"))  # solo per visualizzazione
c.deposito(150.30)
print(format(c.get_saldo(), ".2f"))
c.prelievo(150)
print(format(c.get_saldo(), ".2f"))
c.info()
