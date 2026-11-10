# Continua il discorso sui generics iniziato in 01_bottiglia.py.

class Esempio:
    # NOTA: Java usa spesso getter e setter (getX/setX) per accedere agli
    # attributi in modo controllato. In Python questa scelta non è
    # obbligatoria: gli attributi si possono leggere e modificare
    # direttamente (persona.x, persona.x = 5). Se in futuro servirà
    # aggiungere un controllo sull'accesso, Python offre le "property",
    # un argomento più avanzato che vedremo più avanti nel corso.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Esempio [x=" + str(self.x) + ", y=" + self.y + "]"


class ClasseGenerica:
    """
    In Java: ClasseGenerica<Tipo, AltroTipo>. I due parametri generici
    Tipo e AltroTipo servono solo a dire al compilatore quali tipi
    useranno gli attributi x e y, per farglieli controllare.
    In Python questa dichiarazione non serve: x e y possono già essere di
    qualunque tipo, quindi la classe è "generica" senza scriverci nulla
    di speciale.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


# NOTA: in Java, "public static <T> void stampa(T[] i)" è un metodo
# generico: il parametro <T> dice al compilatore che il metodo accetta un
# array di un tipo qualsiasi, sempre lo stesso per tutti gli elementi
# dell'array. In Python questa dichiarazione non serve: una funzione
# normale accetta già una lista di qualunque tipo di elementi.
def stampa(elementi):
    for valore in elementi:
        print(valore)


# ================== PROVA (equivalente del "main" di Java) ==================

# I generics in Java funzionano solo con le classi (non con i tipi
# primitivi come int, ma con le loro wrapper class Integer, Double...).
# In Python questa distinzione non esiste: liste di numeri, stringhe,
# booleani o decimali si trattano tutte allo stesso identico modo.
numeri = [1, 2, 3, 4]
parole = ["miao", "bau", "cip", "coccode"]
vero_falso = [True, False, True, False]
virgola = [1.1, 2.2, 3.3, 4.4]

stampa(numeri)
stampa(parole)
stampa(vero_falso)
stampa(virgola)

e = Esempio(10, "ciao")
print(e)

oggetto_interi = ClasseGenerica(1, 9)
print(oggetto_interi)

oggetto_double = ClasseGenerica(3.14, 3.3)
print(oggetto_double)

stringa_booleana = ClasseGenerica("ciao", True)
print(stringa_booleana)

# NOTA: in Java, ClasseGenerica misto= new ClasseGenerica('#',99); crea un
# oggetto "non parametrizzato" (un caso particolare, sconsigliato, che il
# compilatore segnala con un avviso). In Python questa distinzione non
# esiste: è semplicemente il modo normale in cui la classe funziona.
misto = ClasseGenerica('#', 99)
print(misto)
