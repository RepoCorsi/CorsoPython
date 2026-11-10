class Persona:

    def __init__(self, nome, cognome, eta):
        self._nome = nome
        self._cognome = cognome
        self._eta = eta

    def dorme(self):
        print("zzzzzzzzzzzzz")

    def __str__(self):
        return "la persona si chiama " + self._nome + " " + self._cognome + " ha " + str(self._eta) + " anni"


# is a -> è un
# la sottoclasse serve per specializzare una classe più generica
class Studente(Persona):

    def __init__(self, materia, nome, cognome, eta):
        # super() deve essere la prima cosa che si chiama, per convenzione
        super().__init__(nome, cognome, eta)  # -- sto passando i valori al costruttore di Persona
        self.materia = materia

    def get_materia(self):
        return self.materia

    def set_materia(self, materia):
        self.materia = materia

    def studia(self, materia):
        print("studio", materia)

    # NOTA: per fare l'override il metodo deve avere la stessa "firma"
    # basta ridefinire un metodo con lo stesso nome.
    def dorme(self):
        #super().dorme()  # possiamo chiamare dorme() di Persona
        print("Dormo poco perché devo studiare")

    def __str__(self):
        return super().__str__() + " studia " + self.materia


# ================== PROVA (equivalente del "main" di Java) ==================

s = Studente("Java", "mario", "rossi", 20)

print(s)

s.dorme()  # chiama il metodo dorme() ridefinito in Studente

p = Persona("giuseppe", "verdi", 40)
p.dorme()  # --> zzzzz

print(isinstance(s, Studente))  # True
print(isinstance(p, Studente))  # False
print(isinstance(s, Persona))  # True

ps = Studente("HTML", "luigi", "neri", 30)
# ps.studia()  # qui invece funzionerebbe: il metodo studia() esiste in Studente

elenco = [p, s]

# POLIMORFISMO
for x in elenco:
    x.dorme()  # --> metodo polimorfico
