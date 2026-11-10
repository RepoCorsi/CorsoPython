# attributi -> come è fatto il gatto (per convenzione "privati": vedi la
# nota sui modificatori di accesso in 01_persona.py)
class Gatto:

    # NOTA: come in 01_persona.py, i 2 costruttori in overload di Java
    # (con e senza razza) diventano un solo __init__ con un parametro di
    # default.
    def __init__(self, nome, eta, razza=None):
        self._nome = nome
        self._eta = eta
        self._razza = razza

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_eta(self):
        return self._eta

    def set_eta(self, eta):
        self._eta = eta

    def get_razza(self):
        return self._razza

    def set_razza(self, razza):
        self._razza = razza

    # cosa può fare -> metodi
    def miagola(self):
        print("miao miao")

    def mangia(self, cibo):
        print("sto mangiando", cibo)

    def fai_le_fusa(self):
        print("prrr prrr")

    def is_anziano(self):
        return self._eta > 10

    # __str__ permette di ridefinire cosa stampa print() per questo oggetto
    # (equivalente dell'override di toString() in Java)
    def __str__(self):
        return ("il gatto si chiama " + self._nome + " ha " + str(self._eta)
                + " anni ed è di razza " + str(self._razza))

    def __eq__(self, o):
        if isinstance(o, Gatto):
            return self._razza.lower() == o._razza.lower()
        return False


# ================== PROVA (equivalente del "main" di Java) ==================

x = 10

# g è l'oggetto di tipo Gatto
# g è un'istanza della classe Gatto
# istanza -> esemplare -> esempio di gatto
g = Gatto("fufi", 7, "persiana")

# g._nome = "sdgdfg"
# g._eta = 17
# g._razza = "dghdghdg"

g.miagola()
g.mangia("le crocchette")
g.fai_le_fusa()

print("è anziano?", g.is_anziano())

print(g)

g2 = Gatto("milù", 12)
# g2._nome = "milù"
# g2._eta = 12
g2.set_razza("siamese")

print(g2)  # <-- senza usare esplicitamente __str__
print("è anziano?", g2.is_anziano())

print(g == g2)

g2.set_razza("persiana")
g2.set_nome("fufi")
g2.set_eta(6)
print(g == g2)

print(g2.get_eta())


# Creare una classe che rappresenti delle macchine
# decidete voi quali attributi descrivono meglio una macchina
# la classe deve implementare l'incapsulamento (attributi "privati" e uso di get/set)
# deve avere almeno 2 modi per costruire l'oggetto (parametri di default)
# deve avere i metodi __str__ e __eq__ (decidete voi quando 2 macchine sono uguali)
# deve avere i metodi accelera e frena.
