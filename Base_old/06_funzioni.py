# In Java una variabile "static" dichiarata nella classe mantiene il suo
# valore tra una chiamata di metodo e l'altra. In Python, per un semplice
# script, l'equivalente più diretto è una variabile definita a livello di
# modulo (fuori da ogni funzione): per poterla MODIFICARE dentro una
# funzione serve però la parola chiave "global".
x = 0
s = "*"


# ------------- INIZIO FUNZIONI ----------------------------------
# Cose obbligatorie in Python:
# - la parola chiave "def", il nome e le parentesi
# - i due punti ":" alla fine della riga, e il corpo indentato
# In Python non serve dichiarare il tipo restituito: se la funzione non usa
# "return" restituisce automaticamente None (equivalente concettuale del
# "void" di Java, anche se in Python quel valore esiste ed è utilizzabile).
def stampa():
    # corpo della funzione
    print("ciao")


# funzione con parametri in ingresso:
# nome + parametri di ingresso si chiama FIRMA DELLA FUNZIONE.
# In Python NON serve indicare il tipo dei parametri.
def stampa_con_parametri_ingresso(par1, par2):
    print("ho ricevuto i seguenti parametri:", par1, "e", par2)


# ------------------------- funzioni con valore di ritorno -----------------------------
def stampa_con_parametri_uscita(a, b):
    frase = "la funzione restituisce questa stringa con:" + a + " e " + b
    return frase  # <-- return fa restituire un valore dalla funzione


# funzione che prende in input 2 numeri e restituisce True se il resto è 0, altrimenti False
def is_divisibile(num1, num2):
    return num1 % num2 == 0


# funzione che prende in input una lista e stampa i valori
def leggi_lista(elementi):
    print("dentro la funzione stampo i valori della lista:")
    for elemento in elementi:
        print(elemento)


# funzione che restituisce in output una lista di stringhe a partire da 3 stringhe in input
def crea_lista(uno, due, tre):
    return [uno, due, tre]


# ----------------------OVERLOAD-------------------------------------------
# NOTA (concetto senza equivalente diretto):
# in Java si possono definire più metodi con lo STESSO nome ma parametri
# diversi (per tipo o per quantità): è l'"overload". Java sceglie in
# automatico il metodo giusto guardando i parametri passati.
#
# In Python questo non è possibile: se definisci due volte una funzione con
# lo stesso nome, la seconda definizione sostituisce semplicemente la prima.
# Non serve però quasi mai: essendo Python a tipizzazione dinamica, una
# SINGOLA funzione può già accettare argomenti di tipo diverso, perché il
# controllo dei tipi non avviene alla dichiarazione ma solo quando il
# codice viene davvero eseguito.
def somma(a, b):
    return a + b


print(somma(2, 2))  # funziona con gli interi
print(somma(2.5, 3.4))  # la stessa funzione funziona anche con i numeri decimali
print(somma("ciao", " a tutti"))  # e persino con le stringhe, grazie all'operatore "+"

# NOTA: se invece le stringhe rappresentano dei numeri (come "2" e "3"),
# in Python "+" le concatena e basta ("2"+"3" vale "23", non 5).
# A differenza di Java, Python non converte automaticamente: la conversione
# va sempre fatta esplicitamente con int() o float().
num1 = "2"
num2 = "3"
risultato_stringhe = int(num1) + int(num2)
print("la somma delle stringhe numeriche convertite è", risultato_stringhe)

# per unire più di 2 stringhe in una frase, in Python non serve una
# funzione diversa: basta continuare a usare "+" (o "*args", vedi sotto)
pap = "qui" + " " + "quo" + " " + "qua"
print("i nipoti di paperino sono", pap)

# ---------------------------VARARGS--------------------------
# NOTA: il "..." di Java (varargs) e il "*" di Python fanno concettualmente
# la stessa cosa: permettono di chiamare la funzione con un numero
# qualsiasi di argomenti, che dentro la funzione si comportano come una
# sequenza (in Java un array, in Python una tupla).
def somma_variabile(*numeri):  # *numeri raccoglie tutti gli argomenti in una tupla
    tot = 0
    for numero in numeri:
        print(numero)
        tot += numero
    return tot


def unisci_parole(*parole):
    frase = ""
    for parola in parole:
        print(parola)
        frase += parola + " "
    return frase


# ---------------------
def stampa_lista(elementi):
    for elemento in elementi:
        print(elemento)


# -----------------------------------------------
def statico():
    # per modificare "x", che è definita fuori dalla funzione, serve "global"
    global x
    x += 1
    print(x)


def aggiungi_asterischi():
    global s
    print(s)
    s += "*"  # concateno gli asterischi


# -------------------------------------------------------
# funzioni ricorsive --> chiamano se stesse, direttamente o indirettamente
def esegui_tot_volte(quanto):
    if quanto > 0:  # caso di uscita
        print("sto chiamando me stessa", quanto, "volte")
        quanto -= 1
        esegui_tot_volte(quanto)


def fattoriale(x):
    if x == 0:  # il fattoriale di 0 è 1, quindi usciamo
        return 1  # caso di uscita
    else:
        return x * fattoriale(x - 1)  # 9*8*7*6*5*4*3*2*1


# ================== CHIAMATE (equivalente del "main" di Java) ==================

# qui sto chiamando la funzione
# quando chiamo la funzione viene eseguito quello che c'è nel suo corpo
stampa()
stampa()

stampa_con_parametri_ingresso("ciao", "a tutti")
stampa_con_parametri_ingresso("xxx", "yy")
stampa_con_parametri_ingresso("aa", "bb")

# la funzione mi restituisce una stringa che metto dentro la variabile uscita_funzione
uscita_funzione = stampa_con_parametri_uscita("xx", "yy")
print(uscita_funzione)

print(stampa_con_parametri_uscita("xx", "yy"))

divisibile_o_no = is_divisibile(10, 3)
print("è divisibile?", divisibile_o_no)

# chiamo la funzione dentro l'operatore ternario di Python (if...else in riga)
print("si" if is_divisibile(10, 2) else "no")

# chiamo la funzione che stampa la lista paperopoli
paperopoli = ["qui", "quo", "qua"]
leggi_lista(paperopoli)

# chiamo crea_lista, passo 3 stringhe e ricevo in output una lista
paperi = crea_lista("paperino", "gastone", "nonna papera")

# leggiamo la lista che ci ha restituito crea_lista
leggi_lista(paperi)  # <-- la leggiamo con la funzione che ci siamo fatti noi

ris = somma_variabile(1, 2, 3, 4)
print("la somma è", ris)

ris2 = somma_variabile(1, 2)
print("la somma è", ris2)

unite = unisci_parole("ciao", "a", "tutti")
print("la concatenazione mi produce", unite)

# NOTA: in Java, ArrayList può contenere oggetti di tipo diverso (String,
# boolean, int, double...) solo se dichiarato senza tipo parametrico, ma è
# una situazione "particolare" e sconsigliata. In Python le liste sono
# SEMPRE in grado di contenere elementi di tipo diverso: è il comportamento
# normale del linguaggio, non un caso speciale.
elenco = ["aaa", True, 157, 3.14]

stampa_lista(elenco)

statico()  # 1
statico()  # 2
statico()  # 3

aggiungi_asterischi()
aggiungi_asterischi()
aggiungi_asterischi()
aggiungi_asterischi()

# chiamata della funzione ricorsiva
esegui_tot_volte(5)

# chiamo la funzione fattoriale ricorsiva
ris_fatt = fattoriale(9)
print(ris_fatt)
