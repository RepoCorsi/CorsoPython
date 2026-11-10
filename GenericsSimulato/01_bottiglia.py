# NOTA GENERALE SUI GENERICS (concetto senza equivalente diretto):
# Java è un linguaggio a tipizzazione STATICA: il tipo di ogni variabile è
# dichiarato e viene controllato dal compilatore. I "generics" (la
# sintassi <T>) servono a scrivere classi e metodi che funzionano con
# tipi diversi SENZA perdere questo controllo: una Bottiglia<Acqua>
# accetta solo Acqua, e il compilatore lo verifica.
#
# Python è invece a tipizzazione DINAMICA: una variabile non ha un tipo
# dichiarato, e una classe può già ricevere argomenti di qualunque tipo
# senza bisogno di nessuna sintassi speciale. Per questo in Python i
# generics, così come li intende Java, non esistono: il problema che
# risolvono in Java (scrivere codice riusabile con tipi diversi) è già
# risolto "di base" dal linguaggio, semplicemente non imponendo vincoli
# di tipo.
#
# NOTA sui file: in Java ogni classe pubblica deve stare nel proprio file
# (Acqua.java, Vino.java, Bottiglia.java, TestBottiglia.java). Python non
# ha questo vincolo: qui riuniamo tutte le classi in un unico file, come
# si fa normalmente in un piccolo progetto Python.


class Acqua:
    # equivalente del metodo toString() di Java: definisce come l'oggetto
    # viene rappresentato quando lo si passa a print()
    def __str__(self):
        return "Acqua"


class Vino:
    def __str__(self):
        return "vino"


class Bottiglia:
    """
    In Java questa classe si scriverebbe Bottiglia<T>: il parametro T
    indica che la bottiglia può contenere un tipo di oggetto scelto al
    momento della creazione (Bottiglia<Acqua>, Bottiglia<Vino>...).
    In Python questo vincolo non esiste: una bottiglia può contenere
    qualunque cosa, senza bisogno di dichiararlo in anticipo.
    """

    def __init__(self):
        self.contenuto = None

    def riempi(self, contenuto):
        print("ho riempito la bottiglia di", contenuto)
        self.contenuto = contenuto

    def svuota(self):
        print("ho svuotato la bottiglia")
        self.contenuto = None

    def __str__(self):
        if self.contenuto is None:
            return "la bottiglia è vuota"
        else:
            return "la bottiglia contiene " + str(self.contenuto)


# ================== PROVA (equivalente del "main" di Java) ==================

# creiamo una bottiglia per l'acqua
bottiglia_acqua = Bottiglia()

# riempiamola di acqua
bottiglia_acqua.riempi(Acqua())
print(bottiglia_acqua)

# svuotiamo la bottiglia d'acqua
bottiglia_acqua.svuota()
print(bottiglia_acqua)  # la bottiglia è vuota

# creiamo una bottiglia per il vino
bottiglia_vino = Bottiglia()

# riempiamola di vino
bottiglia_vino.riempi(Vino())
print(bottiglia_vino)

# svuotiamo la bottiglia di vino
bottiglia_vino.svuota()
print(bottiglia_vino)  # la bottiglia è vuota

# NOTA: in Java, per ottenere una bottiglia che accetti QUALSIASI tipo,
# bisogna dichiararla senza parametro generico (Bottiglia misto = new
# Bottiglia();): è un caso un po' "speciale" e sconsigliato. In Python,
# invece, ogni bottiglia si comporta già così per definizione: non c'è
# nulla di speciale in questo.
misto = Bottiglia()

# riempio d'acqua
misto.riempi(Acqua())
print(misto)

# riempio di vino
misto.riempi(Vino())
print(misto)

# svuotiamo la bottiglia
misto.svuota()
print(misto)
