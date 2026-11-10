# Classe base Strumento
class Strumento:
    def __init__(self, nome):
        # In Python non è necessario definire attributi privati con getter e setter
        # per casi semplici. Usiamo attributi pubblici in modo più diretto e pythonico.
        self.nome = nome

    def suona(self):
        print("tutti gli strumenti suonano")

    # Equivalente del metodo toString() in Java
    def __str__(self):
        return f"Strumento{{nome={self.nome}}}"


# Sottoclasse Chitarra che eredita da Strumento
class Chitarra(Strumento):
    def __init__(self, nome, numero_corde):
        # Chiamata al costruttore della classe base tramite super()
        super().__init__(nome)
        self.numero_corde = numero_corde

    # Sovrascrittura (Override) del metodo suona
    def suona(self):
        print("la chitarra suona con le corde")


# Sottoclasse Pianoforte che eredita da Strumento
class Pianoforte(Strumento):
    def __init__(self, numero_tasti, nome):
        # Manteniamo l'ordine dei parametri del costruttore Java
        super().__init__(nome)
        self.numero_tasti = numero_tasti

    # Sovrascrittura (Override) del metodo suona
    def suona(self):
        print("il pianoforte si suona con i tasti")


# Sottoclasse Tromba che eredita da Strumento
class Tromba(Strumento):
    def __init__(self, nome, numero_tasti):
        super().__init__(nome)
        self.numero_tasti = numero_tasti

    # Sovrascrittura (Override) del metodo suona
    def suona(self):
        print("La tromba suona con l'aria")


# Funzione che accetta in input un oggetto.
# In Python non specifichiamo il tipo (grazie al Duck Typing),
# ma didatticamente assume lo stesso ruolo del metodo statico in Java.
def suona_main(strumento):
    strumento.suona()


# Blocco di esecuzione principale (equivalente del main in Java)

# Istanziamo gli oggetti
s = Strumento("generico")
c = Chitarra("Fender", 6)
p = Pianoforte(88, "piano")
t = Tromba("t1", 5)

# Chiamate singole ai metodi
s.suona()
c.suona()
p.suona()
t.suona()

print("-" * 30)

# Polimorfismo tramite funzione esterna
suona_main(p)

print("-" * 30)

# Una lista di Strumenti. In Python non dobbiamo dichiarare il tipo degli elementi.
# Usiamo una normale lista dinamica al posto dell'array statico Java.
lista_strumenti = [s, c, p, t]

# Il Polimorfismo è l'utilizzo di un metodo in molte forme diverse.
# Il ciclo for richiama il comportamento corretto per ciascun oggetto.
for strumento in lista_strumenti:
    strumento.suona()  # Metodo polimorfico