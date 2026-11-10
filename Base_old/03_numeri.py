# In Java la classe Math offre metodi statici per i calcoli numerici
# (non si crea un oggetto, si chiama direttamente Math.max(...)).
# In Python le funzioni numeriche di base (max, min, round) sono funzioni
# predefinite del linguaggio; per le altre (potenza, arrotondamento per
# eccesso/difetto) si usa il modulo "math" della libreria standard.

import math
import random

massimo = max(5, 10)
print(massimo)

minimo = min(5, 10)

potenza = 2 ** 3  # Python ha l'operatore "**" per l'elevamento a potenza
print(minimo, potenza)

# NOTA: Math.round() di Java arrotonda sempre "per eccesso" a metà
# (5.5 -> 6). La funzione round() di Python usa invece l'arrotondamento
# bancario: arrotonda al numero pari più vicino quando il valore è
# esattamente a metà (round(5.5) in Python restituisce 6, ma round(2.5)
# restituisce 2, non 3 come in Java). È un dettaglio da far notare agli
# studenti se lavorano con gli arrotondamenti.
virgola = round(5.5)
print(virgola)

numero = 5.564323

# In Java si usa la classe DecimalFormat per formattare i numeri con un
# numero fisso di cifre decimali. In Python lo stesso risultato si ottiene
# con il metodo format() delle stringhe (o con le f-string).
numero_formattato = format(numero, ".2f")  # 2 cifre dopo la virgola
print(numero_formattato)

print(math.ceil(5.4))  # --> 6
print(math.floor(5.8))  # --> 5

# ////////////////////////////////////////////////////////////////////

# NOTA: in Java si crea un oggetto Random (new Random()) e poi si chiamano
# i suoi metodi. Python usa invece il modulo "random", le cui funzioni si
# chiamano direttamente senza creare nessun oggetto.

casuale = random.randint(-2147483648, 2147483647)  # simile a r.nextInt()
print(casuale)

limite = random.randint(0, 5)  # da 0 a 5 compresi
print(limite)

estremi = random.randint(2, 10)  # da 2 a 10 compresi
print(estremi)

estremi_virgola = random.uniform(2.5, 11.6)
print(estremi_virgola)

# non esiste una funzione random dedicata ai singoli caratteri o alle stringhe

casuale_booleano = random.choice([True, False])
print(casuale_booleano)

# ////////////////////////////////////////////////////
# 32 - 125
# regex -> espressioni regolari 12[aZ^]

num1 = random.randint(32, 125)
num2 = random.randint(32, 125)
num3 = random.randint(32, 125)

lettera1 = chr(num1)
lettera2 = chr(num2)
lettera3 = chr(num3)

password = lettera1 + lettera2 + lettera3
print("la password generata è", password)

# un programma che simula il lancio di 2 dadi, e mostra a schermo il risultato dei 2 dadi
# fare la somma dei valori casuali,
# dichiarare una variabile booleana che sia True se i 2 dadi sono uguali
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print(dado1, dado2)
somma = dado1 + dado2

uguali_o_no = dado1 == dado2
print(uguali_o_no)
