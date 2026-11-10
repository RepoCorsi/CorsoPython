# NOTA: qui ripetiamo la versione compatta di Persona con i metodi
# get_nome/get_cognome/get_eta, dato che il codice originale li chiama
# esplicitamente.
class Persona:

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_eta(self):
        return self.eta


class Student(Persona):

    def __init__(self, matricola, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        self.matricola = matricola

    def get_matricola(self):
        return self.matricola

    def set_matricola(self, matricola):
        self.matricola = matricola


# NOTA: in Java, "private static ArrayList<Student> studenti" e tutti i
# metodi "static" appartengono alla CLASSE, non a un oggetto: si possono
# chiamare senza creare nessuna istanza (StudenteArrayList.aggiungiStudente(...)).
# In Python, quando un intero gruppo di funzioni e dati condivisi non ha
# bisogno di appartenere a un oggetto specifico, l'equivalente più
# semplice e idiomatico è non usare affatto una classe: bastano funzioni
# di modulo e una variabile di modulo, esattamente come qui sotto.
studenti = []


def aggiungi_studente(studente):
    studenti.append(studente)


def rimuovi_studente(studente):
    studenti.remove(studente)


def visualizza_elenco_studenti():
    for studente in studenti:
        print("Nome:", studente.get_nome())
        print("Cognome:", studente.get_cognome())
        print("Età:", studente.get_eta())
        print("Matricola:", studente.get_matricola())
        print()


def trova_studente_per_matricola(matricola):
    for studente in studenti:
        if studente.get_matricola() == matricola:
            return studente
    return None  # se lo studente non viene trovato


def calcola_media_eta():
    somma_eta = 0
    for studente in studenti:
        somma_eta += studente.get_eta()
    return somma_eta / len(studenti)  # "/" in Python dà già un risultato decimale


# ================== PROVA (equivalente del "main" di Java) ==================

studente1 = Student("12345", "Mario", "Rossi", 20)
studente2 = Student("67890", "Luigi", "Verdi", 22)
studente3 = Student("54321", "Paola", "Bianchi", 21)

aggiungi_studente(studente1)
aggiungi_studente(studente2)
aggiungi_studente(studente3)

print("Elenco studenti:")
visualizza_elenco_studenti()

matricola_cercata = "67890"
studente_trovato = trova_studente_per_matricola(matricola_cercata)
if studente_trovato is not None:
    print("Studente trovato:")
    print("Nome:", studente_trovato.get_nome())
    print("Cognome:", studente_trovato.get_cognome())
    print("Età:", studente_trovato.get_eta())
    print("Matricola:", studente_trovato.get_matricola())
else:
    print("Studente non trovato.")

media_eta = calcola_media_eta()
print("Media età degli studenti:", media_eta)
