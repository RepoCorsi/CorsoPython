class Persona:

    NUMERO_OCCHI = 2
    NUMERO_GAMBE = 2

    def __init__(self, nome=None, cognome=None, eta=0, maggiorenne=False, nazionalita=None):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.maggiorenne = maggiorenne
        self.colore_occhi = None
        self.altezza = None
        self.nazionalita = nazionalita
        self.patentato = False
        # attributi "privati" (per convenzione): accessibili solo tramite get/set
        self._sesso = None
        self._peso = None

    # ------------------- Metodi -----------------------

    def mangia(self, cibo, cena=None):
        if cena is None:
            print("Sto mangiando", cibo)
        else:
            print("A pranzo mangio", cibo, "e a cena mangio", cena)

    def dorme(self):
        print("zzzzzzzzzz")

    def is_maggiorenne(self):
        return self.eta >= 18

    def info(self):
        print("la persona si chiama", self.nome,
            "ha", self.eta, "anni",
            "nazionalità", self.nazionalita,
            "Maggiorenne?:", self.maggiorenne,
            "Ha come tutti", self.NUMERO_OCCHI, "occhi")

    # ------------------- Incapsulamento: get/set -----------------------
    def get_sesso(self):
        return self._sesso

    def set_sesso(self, sesso):
        self._sesso = sesso

    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso

    def __str__(self):
        return ("la persona si chiama " + str(self.nome)
                + " ha " + str(self.eta) + " anni"
                + " nazionalità " + str(self.nazionalita)
                + " Maggiorenne?: " + str(self.maggiorenne)
                + " Ha come tutti " + str(self.NUMERO_OCCHI) + " occhi")

    def __eq__(self, obj):
        if not isinstance(obj, Persona):
            return False
        return self.nome == obj.nome and self.cognome == obj.cognome


# ================== PROVA (equivalente del "main" di Java) ==================

# analogia classe con tipo di dato. Tipo di dato Astratto. ADT abstract data type
numero = 10

# posso creare tanti oggetti e tutti condividono le stesse caratteristiche
persona1 = Persona()  # costruisco un nuovo oggetto col costruttore di default

# per accedere alle proprietà e ai metodi di un oggetto si usa il punto
persona1.colore_occhi = "blu"
persona1.eta = 20
persona1.nome = "Luigi"
persona1.cognome = "bianchi"

print(persona1.eta)
print("è maggiorenne?", persona1.is_maggiorenne())

# OVERLOADING METODI
# Chiamiamo lo stesso metodo passando uno o due parametri
persona1.mangia("pizza")
persona1.mangia("pasta", "carne")

persona1.info()

# creo oggetto con costruttore "personalizzato"
persona2 = Persona("mario", "rossi", 33, True, "italiana")

persona2.info()

# chiamo implicitamente __str__ (equivalente Python dell'override di toString())
print(persona2)

# **** GETTER & SETTER: INCAPSULAMENTO ***************************
persona2.set_sesso('m')
sesso = persona2.get_sesso()
print(sesso)

# Perché usiamo i getter/setter?
# Astrazione del codice dai dati: se domani decidessimo di cambiare il nome interno della variabile
# (es. da self._peso a self._massa), il codice esterno continuerà a funzionare
# senza subire modifiche, poiché utilizzerà sempre il metodo get_peso().

persona2.set_peso(60)
print(persona2.get_peso())

# persona2.NUMERO_GAMBE = 4  # in Python questo, a differenza di Java, sarebbe TECNICAMENTE
# permesso (niente vero "final"): resta comunque una pessima idea, perché rompe
# la convenzione che il nome MAIUSCOLO comunica a chiunque legga il codice.

# EQUALS ****************************************
print(persona1 == persona2)  # chiama __eq__ che abbiamo ridefinito

Persona("aa", "bb", 10).mangia("mela")
