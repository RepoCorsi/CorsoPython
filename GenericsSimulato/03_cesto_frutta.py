# Questo esempio unisce i generics a due argomenti che vedremo meglio più
# avanti nel corso: l'ereditarietà tra classi e le eccezioni
# personalizzate. Qui ci concentriamo sulla parte "generics".


# NOTA: in Java "abstract class Frutta" impedisce di creare direttamente
# un oggetto Frutta (si possono creare solo le sue sottoclassi Mela,
# Pesca, Arancia). Python non ha una parola chiave "abstract" di base:
# per ottenere questo stesso vincolo servirebbe il modulo "abc", che è un
# argomento più avanzato e che vedremo quando parleremo di classi astratte
# vere e proprie. Per ora scriviamo Frutta come una classe normale,
# tenendo a mente che concettualmente non andrebbe mai creata da sola.
class Frutta:
    def __init__(self):
        self.peso = 0.0


# NOTA (concetto senza equivalente diretto):
# in Java, toString() viene usato SIA quando si stampa l'oggetto
# direttamente, SIA quando l'oggetto si trova dentro una collezione
# (System.out.println(listaDiFrutti) chiama comunque toString() su ogni
# elemento). In Python, invece, __str__ viene usato solo quando l'oggetto
# è stampato direttamente: quando un oggetto si trova dentro una lista,
# Python usa un metodo diverso, __repr__, per decidere come mostrarlo.
# Per ottenere lo stesso comportamento di Java in entrambi i casi, si
# definiscono sia __str__ sia __repr__ (qui semplicemente uguali).
class Mela(Frutta):
    def __init__(self):
        super().__init__()
        self.peso = 0.2  # peso medio di una mela in kg

    def __str__(self):
        return "Mela: peso " + str(self.peso)

    __repr__ = __str__


class Pesca(Frutta):
    def __init__(self):
        super().__init__()
        self.peso = 0.3  # peso medio di una pesca in kg

    def __str__(self):
        return "Pesca: peso " + str(self.peso)

    __repr__ = __str__


class Arancia(Frutta):
    def __init__(self):
        super().__init__()
        self.peso = 0.5  # peso medio di un'arancia in kg

    def __str__(self):
        return "Arancia: peso " + str(self.peso)

    __repr__ = __str__


# CLASSE ECCEZIONE PERSONALIZZATA
# NOTA: creare un'eccezione personalizzata funziona in modo molto simile
# in Java e in Python: si crea una classe che eredita dalla classe delle
# eccezioni (Exception in entrambi i linguaggi) e si passa il messaggio
# al costruttore della classe padre.
class PesoException(Exception):
    def __init__(self, messaggio):
        super().__init__(messaggio)


class Cesto:
    """
    In Java: class Cesto<T> (con la possibilità, mostrata anche nel
    commento originale, di scrivere Cesto<T extends Frutta> per obbligare
    T a essere una Frutta o una sua sottoclasse). In Python il cesto
    accetta già qualunque oggetto: il controllo che l'oggetto sia
    davvero un tipo di frutta, se serve, va fatto dentro il metodo, non
    dichiarato nella classe.
    """

    def __init__(self):
        self.frutti = []
        self.peso_massimo = 5.0
        self.peso_attuale = 0.0

    def get_peso(self):
        return self.peso_attuale

    def aggiungi(self, x):
        # NOTA: in Java serve un cast esplicito ((Frutta) x) per poter
        # leggere x.peso, perché il compilatore conosce x solo come "T
        # generico". In Python questo cast non serve: basta usare
        # direttamente x.peso, perché il tipo si verifica solo quando il
        # codice viene davvero eseguito.
        if self.peso_attuale + x.peso > self.peso_massimo:
            raise PesoException("Limite massimo di peso superato.")
        self.frutti.append(x)
        self.peso_attuale += x.peso

    def __str__(self):
        return ("Cesto{" + str(self.frutti) + "pesoMassimo=" + str(self.peso_massimo)
                + ", pesoAttuale=" + str(self.peso_attuale) + "}")


# ================== PROVA (equivalente del "main" di Java) ==================

try:
    cesto = Cesto()  # non "parametrizzato": posso aggiungere qualsiasi tipo di frutta

    mela = Mela()
    pesca = Pesca()
    arancia = Arancia()

    for i in range(4):  # cicliamo per simulare l'aggiunta di tanti frutti
        cesto.aggiungi(mela)
        cesto.aggiungi(pesca)
        cesto.aggiungi(arancia)
        cesto.aggiungi(arancia)
        print(cesto)

    cesto_mele = Cesto()  # in Java sarebbe Cesto<Mela>: qui in teoria potrei
    # aggiungere qualunque cosa, ma per convenzione ci mettiamo solo mele
    mela2 = Mela()
    cesto_mele.aggiungi(mela2)

    print(cesto_mele)

except PesoException as ex:
    print(ex)
