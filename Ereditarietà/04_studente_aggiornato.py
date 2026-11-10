# NOTA: qui ripetiamo ancora la versione compatta di Persona (coerente
# con la nuova versione con attributi pubblici di 01_persona_aggiornata.py).
class Persona:

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def dorme(self):
        print("zzzzzzzzzz")

    def __str__(self):
        return "la persona si chiama " + self.nome + " ha " + str(self.eta) + " anni"


# is a -> è un
# la classe serve per specializzare una classe più generica
class Studente(Persona):

    def __init__(self, materia, nome, cognome, eta):
        # deve essere la prima istruzione
        super().__init__(nome, cognome, eta)  # passo i valori al costruttore di Persona,
        # perché il costruttore non si eredita
        self.materia = materia

    def studia(self, materia):
        print("studio", materia)

    # NOTA: per fare l'override il metodo deve avere la stessa "firma"
    # (stesso nome). In Python questo vale ancora di più alla lettera:
    # basta ridefinire un metodo con lo stesso nome, senza nemmeno dover
    # far coincidere il numero di parametri come in Java.
    def dorme(self):
        super().dorme()  # dorme() di Persona
        print("Dormo poco perché devo studiare")

    def __str__(self):
        return super().__str__() + " Studio " + self.materia


# ================== PROVA (equivalente del "main" di Java) ==================

# per creare una persona, basta usare la classe
p = Persona("aldo", "baglio", 30)
print(p)
p.dorme()  # chiama quello di Persona

s = Studente("informatica", "gino", "latino", 20)

s.studia("Python")

s.dorme()  # chiama quello di Studente, sovrascritto

print(s)

# NOTA: nel file Java originale questa seconda persona viene dichiarata
# di nuovo come "p", il che in realtà non compilerebbe (nome di
# variabile duplicato nello stesso metodo): qui usiamo "p2", come già
# fatto in altri file del corso (vedi 05_oop/02_ereditarieta/02_studente.py).
p2 = Persona("giuseppe", "verdi", 40)
p2.dorme()  # --> zzzzz

print(isinstance(s, Studente))  # True
print(isinstance(p2, Studente))  # False
print(isinstance(s, Persona))  # True

# si può fare, ma "ps" vede solo le cose di Persona, non quelle di Studente
ps = Studente("Python", "mario", "rossi", 20)

# ps.studia("Python")  # NO: se "ps" fosse dichiarata di tipo Persona in un
# linguaggio a tipizzazione statica come Java, non vedrebbe studia().
# NOTA: in Python questo limite non esiste: qui "ps" È uno Studente a
# tutti gli effetti (non esiste una "dichiarazione di tipo" separata
# dall'oggetto stesso), quindi ps.studia("Python") funzionerebbe
# comunque. Il limite di Java qui è un vincolo del COMPILATORE, non
# dell'oggetto in memoria.

studenti = []
studenti.append(s)
studenti.append(Studente("html", "giuseppe", "verdi", 90))
studenti.append(Studente("sql", "pinco", "pallo", 40))

for studente in studenti:
    print(studente)

elenco = [p, s]

# POLIMORFISMO
for x in elenco:
    x.dorme()  # --> metodo polimorfico
