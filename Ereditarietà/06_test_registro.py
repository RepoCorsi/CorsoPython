class Voto:

    def __init__(self, materia, voto):
        self.materia = materia
        self.voto = voto

    def get_materia(self):
        return self.materia

    def set_materia(self, materia):
        self.materia = materia

    def get_voto(self):
        return self.voto

    def set_voto(self, materia, voto):
        self.materia = materia
        self.voto = voto

    def __str__(self):
        return self.get_materia() + ": " + str(self.get_voto())

    # necessario perché i voti finiscono anche dentro una lista, che li
    # stampa con __repr__ (vedi nota già fatta più volte, es. nel modulo Generics)
    __repr__ = __str__


# NOTA: qui ripetiamo la versione compatta di Persona con get_nome, dato
# che il codice originale lo chiama esplicitamente.
class Persona:

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def get_nome(self):
        return self.nome


class Studente(Persona):

    matricola = 0  # attributo di classe: appartiene alla classe, non al singolo oggetto

    # NOTA: in Java, "votiStudente" viene inizializzato direttamente
    # nella dichiarazione dell'attributo (private ArrayList<Voto>
    # votiStudente = new ArrayList();), prima ancora che il corpo del
    # costruttore venga eseguito. In Python un attributo nasce sempre
    # dentro __init__: qui basta assegnarlo come una riga normale,
    # prima o dopo aver chiamato super().__init__(), senza bisogno di
    # nessun meccanismo speciale.
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        self.voti_studente = []
        Studente.matricola += 1
        self.matricola_studente = Studente.matricola

    def get_matricola(self):
        return Studente.matricola

    def ottieni_voto(self, v):
        self.voti_studente.append(v)

    def media_voti(self):
        somma = 0
        for voto in self.voti_studente:
            somma += voto.get_voto()
        return somma / len(self.voti_studente)

    def __str__(self):
        return self.get_nome() + " matricola=" + str(self.matricola_studente) + ", voti=" + str(self.voti_studente)


# ================== PROVA (equivalente del "main" di Java) ==================

arr_s = [
    Studente("Laura", "Bianchi", 48),
    Studente("Mario", "Rossi", 20),
    Studente("Giuseppe", "Verdi", 30),
]

for studente in arr_s:
    print("inserisci il voto di italiano per lo studente", studente.get_nome())
    studente.ottieni_voto(Voto("italiano", int(input())))
    print("inserisci il voto di storia per lo studente", studente.get_nome())
    studente.ottieni_voto(Voto("storia", int(input())))
    print("inserisci il voto di geografia per lo studente", studente.get_nome())
    studente.ottieni_voto(Voto("geografia", int(input())))

    if studente.media_voti() >= 6:
        print(studente, "media", studente.media_voti(), "promosso")
    else:
        print(studente, "media", studente.media_voti(), "bocciato")
