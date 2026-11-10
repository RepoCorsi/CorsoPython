# ==================== VARIABILI NUMERICHE ====================

# In Java bisogna dichiarare il TIPO della variabile (byte, short, int, long...).
# In Python questo non serve: una variabile nasce quando le assegni un valore
# con "=", e il tipo viene dedotto automaticamente da Python.
#
# NOTA per l'insegnante (concetto senza equivalente diretto):
# Java distingue byte (8 bit), short (16 bit), int (32 bit) e long (64 bit).
# Python ha un unico tipo intero (int) che non ha un limite di dimensione:
# cresce automaticamente quanto serve. Quindi la distinzione byte/short/int/long
# in Python non esiste.

i = 1  # in Java questo sarebbe stato "int i = 1;"

print(i)  # qui stampo il valore della variabile i
i = 25
print(i)  # 25

print("123")  # stampa 123 come parola (stringa)
print(123)  # stampa 123 come numero

print("il valore di i è", i)
print("cambio il valore")
i = 50  # cambio il valore di i
print("Adesso il valore di i è", i)

primo = 10
secondo = 5

somma = primo + secondo
print(somma)
sottrazione = primo - secondo
print(sottrazione)
moltiplicazione = primo * secondo
print(moltiplicazione)

# In Java "/" tra due int fa una divisione intera (tronca i decimali).
# In Python "/" fa sempre una divisione con virgola (float).
# Per la divisione intera "alla Java" Python usa l'operatore "//".
divisione = primo / secondo
print(divisione)  # 2.0, non 2 come in Java
divisione_intera = primo // secondo
print(divisione_intera)  # 2, equivalente al comportamento Java

print(10 * 10 / 5 + 3 - 1 * 4 / 2)

# a = "ciao"  # non è un vero errore come in Java: in Python "a" cambierebbe
#              solo tipo. Ma è comunque una cattiva pratica mischiare i tipi.

# NOTA: Java distingue long (con la "L" finale) da int.
# In Python non serve: esiste un solo tipo intero.
lungo = 66
print(lungo)

# ------------------------------------------------
# variabili numeriche con la virgola

# NOTA: Java distingue float (meno precisione) da double (più precisione).
# Python ha un solo tipo per i numeri con la virgola: float (equivale
# concettualmente al double di Java).
f = 1.5
d = 2.5

# ---------------------------------------------------------------
# tipo di dato carattere

# NOTA (concetto senza equivalente diretto):
# Java ha un tipo char dedicato a un singolo carattere, rappresentato tra apici
# singoli ('a'), e internamente è un numero (codice ASCII/Unicode).
# Python NON ha un tipo char: un carattere è semplicemente una stringa (str)
# di lunghezza 1, scritta con apici singoli o doppi indifferentemente.

carattere = 'a'
carattere2 = 'b'
print(carattere, carattere2)

# In Java si può assegnare un numero direttamente a un char (char c = 65)
# e Java lo converte nel carattere corrispondente. In Python questa
# conversione va fatta esplicitamente con la funzione chr().
a_maiuscola = chr(65)
print(a_maiuscola)  # A

# In Java "aMaiuscola++" incrementa direttamente il carattere.
# In Python le stringhe sono immutabili: non esiste l'operatore "++",
# quindi bisogna ricavare il codice numerico, incrementarlo e riconvertirlo.
codice = ord(a_maiuscola) + 1
a_maiuscola = chr(codice)
print(a_maiuscola)  # B

codice = ord(a_maiuscola) + 1
a_maiuscola = chr(codice)
print(a_maiuscola)  # C

# NOTA: Java ha gli operatori di pre/post incremento (++x e x++), che
# eseguono l'incremento e restituiscono un valore diverso a seconda che
# vengano usati prima o dopo. Python non possiede questi operatori:
# l'incremento va sempre fatto con un'assegnazione esplicita, ad esempio
# "x = x + 1" oppure la forma abbreviata "x += 1".

# ---------------------------------------------------------------
parola = "ciao"
print(parola)

parola2 = " a tutti"

parola3 = parola + parola2
print(parola3)

# -----------------------------------------------
vero = True
falso = False

eta = 12
maggiorenne = eta >= 18
print(maggiorenne)

# ----------------------------------------------------
# le costanti in Java si dichiarano con la parola chiave "final".
# Python non ha un vero meccanismo di costanti: per convenzione si usa
# un nome tutto MAIUSCOLO per segnalare che quella variabile non
# dovrebbe essere più modificata (ma nulla lo impedisce a livello di linguaggio).
PIGRECO = 3.14
# PIGRECO = 99  # per convenzione non lo facciamo, ma Python non lo vieta

# --------------------------------------------------------
# NOTA sui CAST (concetto in parte diverso da Java):
# in Java il cast serve a convertire un tipo di dato in un altro,
# a volte in modo implicito (automatico), a volte esplicito (con le parentesi).
# In Python, essendoci meno tipi numerici, il cast implicito non serve quasi
# mai: la conversione va quasi sempre fatta esplicitamente con funzioni
# come int(), float() e str().

var_numero = 56
lungo2 = var_numero  # qui non serve nessun cast, è già un int

x = 10
decimale = float(x)  # cast esplicito da int a float

l2 = 56
i2 = int(l2)  # non necessario in questo caso, ma mostra la sintassi del cast

d3 = 3.999999999
intera = int(d3)  # cast esplicito: tronca la parte decimale, non arrotonda
print(intera)  # 3

# //////////////////////////////////////////////////////////////////
mio_numero = 12
mio_numero2 = 15
tot = mio_numero + mio_numero2  # in Python non serve ricondurre il risultato a "byte"

lettera = 'a'
codice_ascii = ord(lettera)  # ord() converte un carattere nel suo codice numerico
print(codice_ascii)
# ------------------
carattere3 = chr(100)
print(carattere3)

w = 10

# In Java: System.out.println(w++) stampa 10 e POI incrementa (post-incremento).
# In Python questo comportamento va scritto in due passaggi separati.
print(w)
w += 1
print(w)  # 11

# In Java: System.out.println(++w) incrementa PRIMA e poi stampa (pre-incremento).
w += 1
print(w)  # 12

v = False
print(v)

v = 10 < 2
print(v)

z = 10
z += 1
print(z)  # 11

# NOTA: Java 10+ ha la parola chiave "var" per l'inferenza del tipo, ma la
# variabile resta comunque a tipo fisso una volta dichiarata (non si può
# riassegnare un valore di tipo diverso). In Python questa distinzione non
# esiste: ogni variabile è normale e può sempre ricevere un valore di
# qualunque tipo.
mia_variabile = 10  # prende il tipo dal valore assegnato
# mia_variabile = "ciao"  # in Python questo è perfettamente lecito,
#                           a differenza del "var" di Java

virgola = 3.14

nome = "fabio"

# progetto nuovo: calcolare perimetro e area
# di un rettangolo di base 25 e altezza 40
# definire 4 variabili col nome giusto: base, altezza, area e perimetro
# stampare tutte le variabili a video

# programma che calcola l'area e il perimetro del cerchio
# area = pi*r*r
# perimetro = 2*pi*r
# definire una costante PIGRECO
# dichiarare un raggio a piacere
# calcolare perimetro e area
# stampare tutto
