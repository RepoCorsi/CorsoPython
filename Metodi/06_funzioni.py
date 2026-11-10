#----------------------------------
# Una funzione è un blocco di codice a cui diamo un nome, e che svolge un compito specifico. 
# Cose obbligatorie in Python:
# - la parola chiave "def", il nome e le parentesi
# - i due punti ":" alla fine della riga, e il corpo indentato

def saluta():
    # corpo della funzione
    print("ciao")

saluta()
#-------------------------------------------------


# funzione con parametri in ingresso:
# nome + parametri di ingresso si chiama FIRMA DELLA FUNZIONE.
# In Python NON serve indicare il tipo dei parametri.
def saluta(nome):       # nome è un parametro
    print("Ciao", nome)

saluta("Luca")         # "Luca" è un argomento
saluta("Giulia")       # "Giulia" è un argomento

#------------------------------------------------------
def stampa_con_parametri_ingresso(par1, par2):
    print("ho ricevuto i seguenti parametri:", par1, "e", par2)


stampa_con_parametri_ingresso("ciao", "a tutti")
stampa_con_parametri_ingresso("xxx", "yy")
stampa_con_parametri_ingresso("aa", "bb")
#---------------------------------------------------------

#puoi anche specificare il nome del parametro. Si parla di keyword arguments o argomenti nominali.
def descrivi(nome, eta, citta):
    print(nome, eta, "anni, vive a",citta)

descrivi("Marco", 25, "Roma") #devono essere posizionali

descrivi( #posso indicarli in qualsiasi ordine
    citta="Roma",
    nome="Marco",
    eta=25
)

# ------------------------- funzioni con valore di ritorno -----------------------------
def stampa_con_ritorno_valore(a, b):
    frase = "il nome è: " + a + " e il mio cognome è: " + b
    return frase  # <-- return fa restituire un valore dalla funzione

# la funzione mi restituisce una stringa che metto dentro la variabile uscita_funzione
uscita_funzione = stampa_con_ritorno_valore("xx", "yy")
print(uscita_funzione)

# oppure chiamare la funzione direttamente dentro il print:
print(stampa_con_ritorno_valore("xx", "yy"))
#------------------------------------------------------

#Una funzione può restituire più valori separandoli con una virgola:

def calcola(a, b):
    somma = a + b
    prodotto = a * b
    return somma, prodotto

s, p = calcola(4, 5) #con spacchettamento

print(s)  # 9
print(p)  # 20

#Tecnicamente, Python restituisce una tupla, che viene poi assegnata alle due variabili.

risultato = calcola(4, 5)
print(risultato)  # (9, 20) #senza spacchettamento

#--------------------------------------------------------------
#grazie ai parametri opzionali (con valori di default) posso anche non passare tutti gli argomenti:
#I parametri obbligatori devono precedere quelli con valori predefiniti!!! I default vanno dopo
def somma(a, b, c=0, d=0):
    # Questa singola funzione gestisce la somma di 2, 3 o 4 numeri (sia interi che decimali/float)
    return a + b + c + d

risultato = somma(1, 2)
print("Somma semplice (1 + 2):", risultato)
risultato = somma(1, 2,3)
print("Somma semplice (1 + 2 + 3):", risultato)
risultato = somma(1, 2, 3, 4)
print("Somma semplice (1 + 2 + 3 + 4):", risultato)
#----------------------------------------------------------------

#altro esempio
def saluta(nome, messaggio="Ciao"):
    print(f"{messaggio}, {nome}!")

saluta("Luca") #Ciao, Luca!
saluta("Giulia", "Buongiorno") #Buongiorno, Giulia!


#----------------------------------------------------
# return booleano 
#funzione che prende in input 2 numeri e restituisce True se il resto è 0, altrimenti False
def is_divisibile(num1, num2):
    return num1 % num2 == 0

divisibile_o_no = is_divisibile(10, 3)
print("è divisibile?", divisibile_o_no)

# chiamo la funzione dentro l'operatore ternario di Python (if...else in riga)
print("si" if is_divisibile(10, 2) else "no")
#-----------------------------------------------------


# funzione che prende in input una lista e stampa i valori
def leggi_lista(elementi):
    print("dentro la funzione stampo i valori della lista:")
    for elemento in elementi:
        print(elemento)
    #oppure senza for ma con join    
    #print(" ".join(elementi))

# chiamo la funzione che stampa la lista paperopoli
paperopoli = ["qui", "quo", "qua"]
leggi_lista(paperopoli)



#--------------------------------------------------------
# funzione che restituisce in output una lista di stringhe a partire da 3 stringhe in input
def crea_lista(uno, due, tre):
    return [uno, due, tre]

# chiamo crea_lista, passo 3 stringhe e ricevo in output una lista
paperi = crea_lista("paperino", "gastone", "nonna papera")

# leggiamo la lista che ci ha restituito crea_lista
leggi_lista(paperi)  # <-- la leggiamo con la funzione che ci siamo fatti noi


# ---------------------------------------------
# In Python le liste sono SEMPRE in grado di contenere elementi di tipo diverso: è il comportamento
# normale del linguaggio, non un caso speciale.
def stampa_lista(elementi):
    for elemento in elementi:
        print(elemento)

elenco = ["aaa", True, 157, 3.14]

stampa_lista(elenco)
#---------------------------------------------------

#Uso dei parametri opzionali con None:
#Passare una lista ad una funzione:

def aggiungi_materia(nome, lista_materie=None):
    # Se l'utente non ha passato una lista, ne creiamo una nuova NUOVA in quel momento
    #altrimenti usaiamo quella che mi passa
    if lista_materie is None:
        lista_materie = []
        
    lista_materie.append(nome)
    return lista_materie

# ---- Test ------------------
Lista_studente1 = aggiungi_materia("Matematica")
print(Lista_studente1)  # Output: ['Matematica']

#agg. fisica alla lista che già contiene ["chimica","biologia"]
materie=["chimica","biologia"]
Lista_studente2 = aggiungi_materia("Fisica",materie) 
print(Lista_studente2)  # Output: ['chimica', 'biologia', 'Fisica']

#per aggiungere un altra materia alla lista Lista_studente1, devo indicare il nome della lista
Lista_studente1= aggiungi_materia("xxx",Lista_studente1)
print(Lista_studente1)  # Output: ['Matematica', 'xxx']



#----------------------OVERLOAD-------------------------------------------
#In python non esiste overloading. Se definisci due volte una funzione con
# lo stesso nome, la seconda definizione sostituisce semplicemente la prima.
# Una SINGOLA funzione può già accettare argomenti di tipo diverso, perché il
# controllo dei tipi non avviene alla dichiarazione ma solo quando il
# codice viene davvero eseguito.
def somma(a, b):
    return a + b


print(somma(2, 2))  # funziona con gli interi
print(somma(2.5, 3.4))  # la stessa funzione funziona anche con i numeri decimali
print(somma("ciao", " a tutti"))  # e persino con le stringhe, grazie all'operatore "+"
print(somma(True, False)) #True vale 1 e false vale 0
#-----------------------------------------------------------------------------
#forzare il tipo di dato dei parametri:
# #type Hints 
from pydantic import validate_call #da installare con pip install pydantic

@validate_call #--> decoratori
def saluta_studente(nome: str, voto:int):
    print( f"Studente{nome},  voto{voto}")

saluta_studente("mario","cinque")
#--------------------------------------------------------------------
#senza pydantic
def saluta_studente(nome, voto):
    if not isinstance(nome,str): #controlla la tipologia di dato
        raise TypeError("nome deve essere una stringa")
    if not isinstance(voto,int):
        raise TypeError("voto deve essere un numero")
    print( f"Studente{nome},  voto{voto}")

saluta_studente("mario",5)

#------------------------------------------------------------
#accettare più tipi di dato per lo stesso parametro
def imposta_punteggio(punti):
    # Accetta sia int che float
    if not isinstance(punti, (int, float)):
        raise TypeError("Il punteggio deve essere un numero (intero o float)!")
        
    print(f"Punteggio impostato a: {punti}")

imposta_punteggio(10)
imposta_punteggio(8.5)
imposta_punteggio("8") #errore! TypeError

#-----------------------------------------------------------------------------
# NOTA: se invece le stringhe rappresentano dei numeri (come "2" e "3"),
# in Python "+" le concatena e basta ("2"+"3" vale "23", non 5).
# Python non converte automaticamente: LA CONVERSIONE
# VA SEMPRE FATTA ESPLICITAMENTE CON INT() O FLOAT().
# num1 = "2"
# num2 = "3"
# risultato_stringhe = int(num1) + int(num2)
# print("la somma delle stringhe numeriche convertite è", risultato_stringhe)

# ---------------------------VARARGS--------------------------
# il "*" di Python permette di chiamare la funzione con un numero qualsiasi di argomenti, che dentro la funzione si comportano come una
# sequenza (una tupla).
def somma_variabile(*numeri):  # *numeri raccoglie tutti gli argomenti in una tupla. SOLO PER NUMERI!!
    tot = 0
    print("Hai passato questi numeri:")
    for numero in numeri:
        print(numero)
        tot += numero
    return tot


ris = somma_variabile(1, 2, 3, 4)
print("la somma è", ris)

ris2 = somma_variabile(1, 2)
print("la somma è", ris2)

#--------------------------------------------

#SOLO PER PAROLE!!
def unisci_parole(*parole):
    frase = ""
    for parola in parole:
        print(parola)
        frase += parola + " "
    return frase

unite = unisci_parole("ciao", "a", "tutti")
print("la concatenazione mi produce", unite)
#-------------------------------------------------------

#-- doc String
def quadrato(n):
    """ Restituisce il quadrato del numero passato in input
        parametri: n
        restituisce n**2
    
    """ #doc string
    return n**2

print(quadrato(2))

print(help(quadrato))

print(quadrato.__doc__)
#----------------------------------------------------

# ** è KVargs argomenti con chiave e valore:
def mostra_dati(**dati):
    for chiave, valore in dati.items():
        print(f"{chiave}: {valore}")

mostra_dati(eta=22, nome="Anna", citta="Milano") #eta: 22 nome: Anna citta: Milano

#-----------------------------------------------------
#altro esempio:
def crea_profilo(nome, **informazioni): # 'informazioni' diventa un dizionario: {'ruolo': 'Admin', 'citta': 'Roma'}
    
    print("Utente:", nome) #parametro normale
    for chiave, valore in informazioni.items(): #ciclo sul dizionario chiave e valore
        print(f"- {chiave}: {valore}")

#se passo chiave e valore sto passando un dizionario e finisce in **
crea_profilo("Elena", ruolo="Admin", citta="Roma") 
# Output:
# Utente: Elena
# - ruolo: Admin
# - citta: Roma
#------------------------------------------------------

def registra_evento(livello, *messaggi, **dettagli):
    print(f"[{livello.upper()}]")
    
    # 1. Uniamo tutti i messaggi passati in *args usando il .join() che conosci!
    if messaggi:
        print(f"Messaggio: {' - '.join(messaggi)}")
    
    # 2. Stampiamo tutti i dettagli extra passati in **kwargs (dizionario)
    if dettagli:
        print("Dettagli Extra:")
        for chiave, valore in dettagli.items():
            print(f"  -> {chiave}: {valore}")
    print("-" * 20)

# Utilizzo 1: Solo livello e un messaggio
registra_evento("info", "Avvio del sistema completato")

# Utilizzo 2: Livello, più messaggi posizionali (*args) e dettagli con nome (**kwargs)
registra_evento(
    "errore", 
    "Connessione al database fallita", "Timeout dopo 30 secondi", # Finiscono in *args
    codice=500, utente="amministratore", ip="192.168.1.1"        # Finiscono in **kwargs
)
#---------------------------------------------------------

def crea_panino(tipo_pane, *ingredienti, **opzioni):
    print(f"Panino pronto con pane di tipo {tipo_pane}")
    if ingredienti:
        print("questi sono gli ingredienti:")
        print(f"{",".join(ingredienti)}")
    if opzioni:
        print("Hai scelto queste opzioni aggiuntive:")
        for chiave, valore in opzioni.items():
            print(f"  -> {chiave}: {valore}")
    print("-" * 20)
        

# Fai un test chiamando la funzione in questo modo:
crea_panino("Integrale", "Prosciutto", "Mozzarella", "Pomodoro", salsa="Maionese", tostato=True)
crea_panino("Con semi di sesamo", "Speck", "Brie", mozzarella="Bufala", asporto="Si")


# -----------------------------------------------
# --------------------Variabili esterne alla funzione ------------------------------------------
#python legge prima il contesto locale dentro la funzione e poi quello globale.
#Con lo stesso nome vince quella locale
x = 0
def esterna():
    # per modificare "x", che è definita fuori dalla funzione, serve "global" altrimenti da errore!
    #per leggere non c'è problema
    global x
    x += 1
    print(x)

esterna()  # 1
esterna()  # 2
esterna()  # 3

#----------------
s = "aaa"

def aggiungi_asterischi():
    global s
    print(s)
    s += "*"  # concateno gli asterischi

aggiungi_asterischi()
aggiungi_asterischi()
aggiungi_asterischi()
aggiungi_asterischi()
#----------------------------------------------------------------------------------

#come chiamare funzioni presenti in altri file. Dal file Elenco_funzioni.py
from Elenco_funzioni import doppio, esegui_tante_volte,crea_sandwich #con la virgila inserisco le funzionalità che voglio utilizzare

from Elenco_funzioni import * # con asterisco si importano tutto il contenuto del file

risultato=doppio(10)
print(risultato)

esegui_tante_volte(5)
#-------------------------------------------------------


# -------------------------------------------------------
# funzioni ricorsive --> chiamano se stesse, direttamente o indirettamente
#se una ricorsione non ha mai fine,python interrompe la ricorsione dopo circa 1000
# chiamate annidate, sollevando un RecursionError, per evitare di
# esaurire davvero la memoria dell'interprete.
def sempre():
    print("continua per sempre")
    sempre()


#-------------------------------------
def esegui_tot_volte(quanto):
    if quanto > 0:  # caso di uscita, per terminare l'esecuzione
        print("sto chiamando me stessa", quanto, "volte")
        quanto -= 1
        esegui_tot_volte(quanto)

# chiamata della funzione ricorsiva
esegui_tot_volte(5)


#--------------------------------------
def fattoriale(x):
    if x == 0:  # il fattoriale di 0 è 1, quindi usciamo
        return 1  # caso di uscita
    else:
        return x * fattoriale(x - 1)  # 9*8*7*6*5*4*3*2*1

# chiamo la funzione fattoriale ricorsiva
ris_fatt = fattoriale(9)
print(ris_fatt)
#-------------------------------------------------------------------------

#Passare una funzione come argomento --> Callback
def perDue(x):
    return x * 2

def applica(funzione, numero): #ad applica al primo parametro ci va una funzione
    return funzione(numero)

print(applica(perDue, 5))  # 25 #passo la funzione quadrato ad applica
#-----------------

def saluta(nome):
    print("ciao",nome)
    
#funzione che esegue qualunque funzione su un parametro
def esegui_azione(funzione,parametro):
    return funzione(parametro)

#saluta -> FUNZIONE DI CALLBACK  
esegui_azione(saluta,"mario") #ciao mario

#perDue -> FUNZIONE DI CALLBACK
print(esegui_azione(perDue,5)) #5*2 -> 10

#----- EVOLUZIONE: ------

# Accetta una funzione e qualsiasi combinazione di parametri successivi
def esegui_azione(funzione, *args, **kwargs):
    return funzione(*args, **kwargs)


# 1. Funzione con 1 parametro
def perDue(x):
    return x * 2

def saluta(nome):
    print("ciao",nome)

# 2. Funzione con 2 parametri
def somma(a, b):
    return a + b

# 3. Funzione con parametri con nome (valori di default)
def descrivi_persona(nome, eta, citta="Roma"):
    return f"{nome} ha {eta} anni e vive a {citta}."

# --- ESECUZIONE ---

# Caso 1: 1 parametro
print(esegui_azione(perDue, 5)) # Output: 10

esegui_azione(saluta,"mario") #ciao mario

# Caso 2: 2 parametri posizionali
print(esegui_azione(somma, 10, 20)) # Output: 30

# Caso 3: parametri posizionali + parametro con nome (citta)
print(esegui_azione(descrivi_persona, "Marco", 25, citta="Roma")) 
# Output: Marco ha 25 anni e vive a Milano.


#--------------------------------------------------------
#usato per esempio nelle funzioni di ordine superiore, per esempio map, filter...
lista=[2,3,4,5]
doppio=map(perDue,lista) #map applica una funzione ad un elenco di valori
print(list(doppio))

#anche se si preferisce usare una list comprehension
doppio=[x*2 for x in lista]
print(doppio)




#----------------------------------------
#NON TRATTARE PER SEMPLICITÀ

def fibonacci_ricorsivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_ricorsivo(n - 1) + fibonacci_ricorsivo(n - 2)

fibonacci_ricorsivo(10)

#---------------------------------------------
def fibonacci_no_ricorsivo(n):
    if n <= 1:
        return n
    else:
        num1 = 0
        num2 = 1
        somma_ = 0
        for i in range(1, n):
            somma_ = num1 + num2
            num1 = num2
            num2 = somma_
        return somma_
