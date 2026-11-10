from abc import ABC, abstractmethod


class Int1(ABC):
    # NOTA: un campo dichiarato in un'interfaccia Java è implicitamente
    # "public static final" (una costante condivisa da tutti). In Python,
    # un attributo scritto direttamente nel corpo della classe è un
    # attributo di classe: concettualmente molto simile (condiviso da
    # tutte le sottoclassi), anche se Python non impedisce davvero di
    # modificarlo in seguito (niente "final" reale, come già visto).
    x = 10

    # public abstract
    @abstractmethod
    def ciao(self):
        pass

    # NOTA: da Java 8 esistono i "metodi default": metodi di
    # un'interfaccia che hanno già un corpo pronto, così le classi non
    # sono obbligate a ridefinirli. In Python questo non richiede nessuna
    # sintassi speciale: è semplicemente un metodo NORMALE (senza
    # @abstractmethod) scritto dentro la classe astratta. Le classi che
    # ereditano da Int1 lo ricevono già pronto, esattamente come in Java.
    def stampa(self):
        print("ciao dall'interfaccia 1")


class Int2(ABC):
    # non si possono avere 2 attributi di classe con lo stesso nome nella
    # stessa classe, ma qui sono in 2 classi diverse, quindi non c'è conflitto
    y = 20

    def stampa2(self):
        print("ciao dall'interfaccia 2")


class A(Int1, Int2):

    def ciao(self):
        print("ciao")


# ================== PROVA (equivalente del "main" di Java) ==================

a = A()
a.ciao()  # --> deriva dal metodo astratto dell'interfaccia
a.stampa()  # --> il metodo "default" contiene già il corpo
a.stampa2()  # --> il metodo "default" contiene già il corpo
print(a.x)
print(a.y)

print(isinstance(a, Int1))
