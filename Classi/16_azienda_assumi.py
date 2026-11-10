class Persona:

    contatore = 0  # equivalente Python di "static int contatore"

    # NOTA: in Java, i 3 costruttori si richiamano a catena tra loro con
    # "this(...)" (persona(nome) chiama persona(nome,"",0), e così via).
    # In Python questo meccanismo di "concatenamento" tra costruttori non
    # serve: basta un solo __init__ con valori di default, che copre
    # automaticamente tutti e 3 i casi.
    def __init__(self, nome, sesso="", eta=0):
        self.nome = nome
        self.sesso = sesso
        self.eta = eta
        Persona.contatore += 1

    def stampa(self):
        print(self.get_eta(), self.get_sesso(), self.get_nome())

    @staticmethod
    def get_contatore():
        return Persona.contatore

    def get_nome(self):
        return self.nome

    def set_nome(self, n):
        self.nome = n

    def get_sesso(self):
        return self.sesso

    def set_sesso(self, s):
        self.sesso = s

    def get_eta(self):
        return self.eta

    def set_eta(self, eta):
        self.eta = eta

    def __str__(self):
        return str(self.get_eta()) + " " + self.get_sesso() + " " + self.get_nome()

    def __eq__(self, o):
        if isinstance(o, Persona):
            return self.nome == o.nome and self.eta == o.eta and self.sesso == o.sesso
        return False


class Azienda:

    def __init__(self, nome):
        self.nome = nome
        self.p = []  # lista di persone (equivalente dell'array persona[] di Java)

    def assumi(self):
        print("quanti dipendenti vuoi assumere?")
        quanti = int(input())
        self.p = [None] * quanti
        for i in range(quanti):
            print("inserisci il nome")
            nomedip = input()
            print("inserisci l'età")
            eta = int(input())
            print("inserisci il sesso")
            sesso = input()
            self.p[i] = Persona(nomedip, sesso, eta)  # riempio la lista in base ai valori inseriti

    def __str__(self):
        s = "Azienda= " + self.nome + "\n"
        s += str(Persona.contatore) + " dipendenti assunti:\n"
        for pers in self.p:  # leggo la lista popolata da assumi()
            s += "nome: " + pers.get_nome() + " sesso: " + pers.get_sesso() + " età: " + str(pers.get_eta()) + "\n"
        return s


# ================== PROVA (equivalente del "main" di Java) ==================

print("Inserisci il nome della azienda")
nome = input()

a = Azienda(nome)

a.assumi()
print(a)  # stampa l'oggetto grazie a __str__ della classe Azienda
