import random
from datetime import datetime

# if / elif / else -----------------------------------------------------
print("Inserisci la tua età")
eta = int(input())

# Operatori di confronto:  (>, <, >=, <=, ==, !=)
if eta >= 18:
    print("Sei maggiorenne! puoi entrare")
else:
    print("Non sei maggiorenne!")
print("Grazie per aver usato il nostro servizio")
print("-" * 40)

# Elif (corrisponde a "else if" in Java)
num = 5
if num > 5:
    print("maggiore di 5")
elif num == 5:
    print("uguale a 5")
else:
    print("minore di 5")

#------------------------
# Controllo temperature
temperature = 19
if temperature > 30:
    print("Fa caldo")
elif temperature < 20:
    print("Fa freddo.")
else:
    print("Si sta bene")

#------------------------------------------
# Controlla se il voto è compreso tra 1 e 10 (inclusi)
voto=7.5
if 1<= voto <= 10:
    print("tra 1 e 10 hai preso",voto)
else:
    print("valore fori dal range")

#----------------
eta=20
#in python esiste la funzione range() che rappresenta un range di valori
if eta in range(0,19): #estremo superiore escluso. # Accetta solo numeri interi! non float! per float si usa il modo di sopra
    print("non sei maggiorenne")
else:
    print("sei maggiorenne")

#-----------------

# divisione con controllo del divisore
print("Inserisci due numeri interi:")
num1 = int(input())
num2 = int(input())
if num2 == 0:
    print("ERRORE: divisione per zero")
else:
# In Python, / esegue una divisione decimale. 
# Per la divisione intera usiamo l'operatore //    
    print("Quoziente:", num1 // num2)
    print("Resto:", num1 % num2)


# pari o dispari
print("inserisci un numero")
num3 = float(input())
if num3 % 2 == 0:
    print("il numero è pari")
else:
    print("il numero è dispari")
    
#--------------------------------------------   
x="Testo"
#isinstance confronta la varibile con un tipo. -> ritorna True se è lo stesso tipo
if isinstance(x,str): # str-> stringa
    print(f"la variabile {x} è una stringa")
elif isinstance(x, bool): # int -> intero,  float -> decimale
    print(f"la variabile {x} è un booleano")
elif isinstance(x, (int, float)): # int -> intero,  float -> decimale
    print(f"la variabile {x} è un numero")
else:
    print(f"la variabile {x} è qualche altro tipo")


#------- Vedere se la stringa contiene numeri
testo = "12345"

#NOTA: .isdigit() con "-5" o "3.14", restituirà False perché il segno meno e il punto sono considerati testo 
if testo.isdigit():
    print("La stringa contiene solo cifre intere positive!")
else:
    print("Non è un intero positivo puro.")
#isdigit() controlla esclusivamente numeri interi positivi. Se la stringa ha la virgola o il punto o è un numero negativo -123 is digit ritorna False, perchè - e . e , sono caratteri

#--------------------------------------------    
    
import random
# gioco dei dadi
# In Python usiamo il modulo 'random'. randint(a, b) include sia a che b.
valore1 = random.randint(1, 6)#estremi inclusi
valore2 = random.randint(1, 6)
totale = valore1 + valore2
print(f"Dado 1: {valore1} | Dado 2: {valore2} | Totale: {totale}")

if totale > 10:
    print("hai vinto")
else:
    print("hai perso")

from datetime import datetime
# saluto in base all'ora del giorno
orario = datetime.now().hour
print(orario)

if orario < 12:
    saluto = "Buon giorno"
elif orario < 18:
    saluto = "Buon Pomeriggio"
elif orario < 22:
    saluto = "Buona sera"
else:
    saluto = "Buona notte"

print(saluto)

# numero pari di lettere
stringa = "ciao"
# In Python usiamo la funzione built-in len()
lunghezza = len(stringa)
if lunghezza % 2 == 0:
    print("La parola", stringa, "ha un numero pari di lettere.")
else:
    print("La parola", stringa, "ha un numero dispari di lettere")

#----------------------------------------------------------
parola = "python"
lunghezza = len(parola)

if lunghezza > 3:
    print(f"La parola ha più di 3 lettere, {lunghezza}.")
    
#-- Con Walrus:
if (lunghezza := len("python")) > 3:
    print(f"La parola ha più di 3 lettere, {lunghezza}.")
#---------------------------------

punti = 12
# Calcoliamo il doppio, lo salviamo in 'bonus' e lo controlliamo 
bonus=punti * 2
if bonus>20:
   print(f"Hai raggiunto {bonus} punti.") 
else:
  print("Punteggio troppo basso.")

#con walrus:

if (bonus := punti * 2) > 20:
  print(f"Hai raggiunto {bonus} punti.")
else:
  print("Punteggio troppo basso.")

# Per confrontare il codice ASCII in Python usiamo la funzione ord() che restituisce il numero ascii corrispondente al carattere.
# numero = 1
# lettera = 'z'
# if ord(lettera) > numero: # True, perché l'ASCII di 'z' (122) è maggiore di 1
    # print("Sì, perché nella tabella ASCII la lettera viene dopo (ha un valore numerico maggiore)")
# else:
    # print("No")

# Ricerca di una sottostringa
# print("inserisci una frase")
# parola3 = input()#ciao a tutti
parola3 = "ciao a tutti"

# In Python usiamo l'operatore 'in'
if "tutti" in parola3:
    pos_tutti = parola3.find("tutti") #pos di tutti
    # pos_i = parola3.find("i", pos_tutti + 1)
    # tutti = parola3[pos_tutti:pos_i + 1]
    print("posizione tutti",pos_tutti)
else:
    print("tutti non fa parte della stringa")

#-------------------------------
#Con operatore di assegnazione walrus :=
# Verifichiamo se la parola "tutti" è presente e ne ricaviamo la posizione.
# Usiamo il walrus per salvare l'indice senza dover chiamare .find() due volte.
if (posizione := parola3.find("tutti")) != -1:
  print(f"Trovato alla posizione: {posizione}")
else:
  print("Parola non trovata")
#-----------------------------------

# ordine alfabetico
str1 = "abaco"
str2 = "zuzzurellone"

if str1 > str2:
    print(str2, "viene prima in ordine alfabetico")
elif str1 < str2:
    print(str1, "viene prima in ordine alfabetico")
else:
    print("Le parole coincidono")

# In Python: and, or, not (scritte a parole, molto più leggibili!)
print("***********OPERATORI LOGICI**********")
print(10 > 8 and 7 < 6)  # False
print(9 > 5 and 5 == 5)  # True
print(6 == 6 and 1 > 4)  # False
print(10 > 8 or 7 < 6)  # True
print(4 < 3 or 7 > 9)  # False

sole = True
temperatura = 25
if sole and temperatura > 20:
    print("esco")
else:
    print("sto a casa")

voto1 = 6
voto2 = 10
voto3 = 5

# "and" ha la priorità su "or"
if (voto1 >= 6 or voto2 >= 6) and voto3 >= 6: #bocciato
    print("promosso")
else:
    print("bocciato")

# controllo di ore e minuti
print("Inserire ore e minuti:")
ore = int(input("Ore: "))
minuti = int(input("Minuti: "))

# Metodo 1: Condizioni separate
if ore < 0:
    print("Non è un orario valido")
elif ore > 23:
    print("Non è un orario valido")
elif minuti < 0:
    print("Non è un orario valido")
elif minuti > 59:
    print("Non è un orario valido")
else:
    print("È un orario valido")

# Metodo 2: Più comodo con OR (or)
if ore < 0 or ore > 23 or minuti < 0 or minuti > 59:
    print("Non è un orario")
else:
    print("È un orario")

#ancora più semplice
ore_ok =(0 <= ore < 24)  # NOTA: Python permette il "confronto a catena", più leggibile di (ore>=0 and ore<24)
minuti_ok = (0 <= minuti < 60)

if ore_ok and minuti_ok:
    print("È un orario")
else:
    print("Non è un orario")

# ****************** TERNARIO ***************************
# In Python: valore_se_vero if cond else valore_se_falso
voto = 8
print("promosso" if voto >= 6 else "bocciato")

# Stesso esempio con IF classico
if voto >= 6:
    print("promosso")
else:
    print("bocciato")

altezza = 175
# Assegnamento con operatore ternario
tipologia = "alto" if altezza >= 180 else "normale"
print(f"Tipologia altezza: {tipologia}")

if altezza >= 180:
    tipologia = "alto"
else:
    tipologia = "normale"
print(tipologia)

# Massimo tra due numeri con ternario
a = 10
b = 20
massimo = a if a > b else b
print("Il maggiore tra", a, "e", b, " è:", massimo)

# Gestione del caso di numeri uguali (Ternario concatenato)
# NOTA DIDATTICA: Sebbene possibile, in Python si evita per la leggibilità.
max_o_uguali = a if a > b else (-1 if a == b else b)
print(f"Risultato max o uguali (-1 se uguali): {max_o_uguali}")

# Oppure con stringhe
max_uguali_str = (
    f"Il più grande è {a}" if a > b else
    "i numeri sono uguali" if a == b else
    f"Il più grande è {b}"
)
print(max_uguali_str)

# Massimo tra 3 valori con ternario
c = 5
max_3 = a if (a > b and a > c) else (b if b > c else c)
print(f"Il maggiore tra {a}, {b} e {c} è: {max_3}")
    
# **************** SWITCH MATCH-CASE*************************
# NOTA DIDATTICA: Python non ha avuto uno "switch" fino alla versione 3.10.
# Dalla versione 3.10 è stato introdotto il costrutto 'match-case'.
i = 3
match i:
    case 0:
        print("i è uguale a 0")
    case 1:
        print("i è uguale a 1")
    case 2:
        print("i è uguale a 2")
    case _: # Il carattere '_' funge da 'default'
        print("i è diverso da 0, 1 o 2")


# Esempio con if
i_ = 3
if i_ == 0:
    print("i è uguale a 0")
elif i_ == 1:
    print("i è uguale a 1")
elif i_ == 2:
    print("i è uguale a 2")
else:
    print("i è diverso da 0, 1 o 2")

# case gestisce solo uguaglianze non > maggiore o minore < 
#Caso SBAGLIATO!
match x:
    case > 10:  # NO! ❌ Sbagliato
        print("Maggiore di 10")
    case 3 <= x <= 15: # NO! ❌ Sbagliato
        print("Compreso tra 3 e 15")
--- 
#Caso CORRETTO, con IF. Si usano i casi di default  case _

match x:
    case _ if x > 10:
        print("Maggiore di 10")
    case _ if 3 <= x <= 15:
        print("Compreso tra 3 e 15")

#------------------------------------
# match funziona con stringhe, valori booleani, liste, tuple, dizionari e persino oggetti personalizzati

#match con lettere
comando="avvia"

match comando:
    case "avvia":
        print("motore avviato")
    case "stop":
        print("motore fermato")
    case "gira dx":
        print("vado a destra")
        
#--------------------------------------------
# Giorno della settimana
# datetime.now().weekday() restituisce un numero da 0 (Lunedì) a 6 (Domenica)
giorno = datetime.now().weekday()  #inizia da 0 -> lunedì datetime.now().isoweekday() inizia da 1 -> lunedì 

print(f"Numero del giorno della settimana: {giorno}")

match giorno:
    case 0:
        print("Oggi è Lunedì")
    case 1:
        print("Oggi è Martedì")
    case 2:
        print("Oggi è Mercoledì")
    case 3:
        print("Oggi è Giovedì")
    case 4:
        print("Oggi è Venerdì")
    case 5:
        print("Oggi è Sabato")
    case 6:
        print("Oggi è Domenica")
    case _: # Il carattere '_' funge da 'default'
        print("Errore nella data")

#---Con if normale
print(giorno)
if giorno == 0:
    print("Oggi è Lunedì")
elif giorno == 1:
    print("Oggi è Martedì")
elif giorno == 2:
    print("Oggi è Mercoledì")
elif giorno == 3:
    print("Oggi è Giovedì")
elif giorno == 4:
    print("Oggi è Venerdì")
elif giorno == 5:
    print("Oggi è Sabato")
else:
    print("Oggi è Domenica")

# Switch sequenziali (Accorpare più casi)
# In Python usiamo l'operatore OR logico rappresentato dalla barra verticale '|'
lettera = "i"
match lettera:
    case "a" | "e" | "i" | "o" | "u":
        messaggio = f"'{lettera}' è una vocale"
    case _:
        messaggio = f"'{lettera}' è una consonante"
        
print(messaggio)

# switch sequenziali con if-> valore in (...)
lettera_ = "i"
if lettera_ in ("a", "e", "i", "o", "u"):
    messaggio = lettera_ + " è una vocale"
else:
    messaggio = lettera_ + " è una consonante"
print(messaggio)


# ************************************************************************************************
# ***********************SOLUZIONI DEGLI ESERCIZI ***********************************

# 1 - Dati 2 numeri: scrivere "1" se uguali, "2" se il primo è maggiore, "3" altrimenti
print("inserisci il primo numero:")
primo = int(input())
print("inserisci il secondo numero:")
secondo = int(input())
if primo == secondo:
    print("1")
elif primo > secondo:
    print("2")
else:
    print("3")

# 2 - pari/dispari e positivo/negativo
print("inserisci numero positivo o negativo:")
val = int(input())
if val % 2 == 0:
    print("Pari e", end=" ")
else:
    print("Dispari e", end=" ")
if val < 0:
    print("Negativo")
else:
    print("Positivo")

# 3 - se B è pari scambia A e B, altrimenti li somma
a = int(input("\nInserisci A: "))
b = int(input("Inserisci B: "))
if b % 2 == 0:
    # In Python lo scambio si fa in modo super elegante senza variabile temporanea!
    a, b = b, a
    print(f"Scambiati! Ora A = {a} e B = {b}")
else:
    print(f"Somma A+B = {a + b}")

#------------------------------------------------------------
#  Esercizio BMI (Indice di Massa Corporea)
print("\n*** CALCOLO BMI ***")

peso = float(input("Inserisci il tuo peso in chilogrammi: "))
altezza_bmi = float(input("Inserisci la tua altezza in metri: "))

bmi = peso / (altezza_bmi * altezza_bmi)
# Arrotondiamo il BMI a due cifre decimali per una lettura più pulita
print("Il tuo BMI è:", round(bmi, 2))

if 20 <= bmi <= 25:
    print("Sei nella norma.")
elif bmi < 20:
    print("Sei sottopeso.")
else:
    print("Sei in sovrappeso.")

#----------------------
#esempio con Match-Case:
match bmi:
    case _ if bmi<20:
        print("sottopeso")
        #tutto il codice che vuoi ..........
    case _ if 20<= bmi<= 25:
        print("nella norma")
    case _:
        print("sei sovrappeso")

#-------------------------------------------------------------------
# ****** Numero pari di lettere + confronto con numero casuale ******
stringa_test = "ciao"
lungh2 = len(stringa_test)
num_cas = random.randint(1, 10)
print("parola:", stringa_test, "numero lettere:", lungh2, "numero casuale:", num_cas)

if lungh2 % 2 == 0:
    print("La parola ha un numero pari di lettere")
else:
    print("La parola ha un numero dispari di lettere")

if lungh2 > num_cas:
    print("il numero di lettere è più grande del numero casuale")
elif lungh2 < num_cas:
    print("il numero di lettere è più piccolo del numero casuale")
else:
    print("il numero di lettere è uguale al numero casuale")

# ------------------------------------------------

# esercizio voto/registrazione (fino a 30esimi)
passato = False
voto_esame = int(input("\nInserisci il voto d'esame (0-30): "))
if voto_esame < 0 or voto_esame > 30:
    print("Valore errato!")
elif 0 <= voto_esame <= 17:
    print("Esame non superato")
elif 18 <= voto_esame <= 24:
    print("Giudizio: Sufficiente")
    passato = True
elif 25 <= voto_esame <= 30:
    print("Giudizio: Buono/Ottimo")
    passato = True

if passato:
    registra = int(input("Vuoi registrare il voto? (0=No, 1=Sì): "))
    if registra == 0:
        print("Voto rifiutato")
    elif registra == 1:
        print("Voto accettato e registrato!")
    else:
        print("Scelta non valida")

#--------------------------------------------------------------
#  Gioco della Morra Cinese (Carta, Forbice, Sasso)
print("\n*** MORRA CINESE ***")
# f = forbice, s = sasso, c = carta
computer = random.choice(['f', 's', 'c'])
giocatore = input("Inserisci f (forbice), s (sasso), c (carta): ").lower()
print(f"tu: {giocatore}, pc: {computer}")

vincita = (giocatore == 's' and computer == 'f') or \
          (giocatore == 'f' and computer == 'c') or \
          (giocatore == 'c' and computer == 's')

if giocatore == computer:
    print("Parità")
elif vincita:
    print("Hai vinto")
else:
    print("Hai perso")
    
#--------------------------------------------------------------------
# chiede 3 numeri e stampa il maggiore
print("\nInserisci 3 numeri per trovare il maggiore:")
n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

# Soluzione con IF
if n1 > n2 and n1 > n3:
    print(f"Il maggiore con IF è: {n1}")
elif n2 > n3:
    print(f"Il maggiore con IF è: {n2}")
else:
    print(f"Il maggiore con IF è: {n3}")

# Soluzione elegantissima con la funzione nativa max() di Python.
# max() accetta già quanti argomenti servono
maggiore_veloce = max(n1, n2, n3)
print(f"Il maggiore con funzione max() è: {maggiore_veloce}")

# ********************* Esercizio calcolatrice *********************
print("primo numero:")
primo_num = int(input())
print("secondo numero:")
secondo_num = int(input())
print("operazione:")
operazione = input()

match operazione:
    case "+":
        print(f"{primo_num} + {secondo_num} = {primo_num + secondo_num}")
    case "-":
        print(f"{primo_num} - {secondo_num} = {primo_num - secondo_num}")
    case "*":
        print(f"{primo_num} * {secondo_num} = {primo_num * secondo_num}")
    case "/":
        if secondo_num == 0:
            print("Non puoi dividere per zero!")
        else:
            # Usiamo / per divisione decimale o // per intera
            print(f"{primo_num} / {secondo_num} = {primo_num / secondo_num}")
    case _:
        print("Operazione non valida!")

#----CON IF
if operazione == "+":
    risultato = primo_num + secondo_num
    print(primo_num, "+", secondo_num, "=", risultato)
elif operazione == "-":
    risultato = primo_num - secondo_num
    print(primo_num, "-", secondo_num, "=", risultato)
elif operazione == "*":
    risultato = primo_num * secondo_num
    print(primo_num, "*", secondo_num, "=", risultato)
elif operazione == "/":
    if secondo_num == 0:
        print("non puoi dividere per zero")
    else:
        risultato = primo_num / secondo_num
        print(primo_num, "/", secondo_num, "=", risultato)

#-----------------------------------------------------------------------------
# esercizio: dato il nome del mese, restituisce il numero dei giorni. con gestione anno bisestile
print("Inserisci il nome del mese: ")
mese = input().lower()

if mese in ("novembre", "aprile", "giugno", "settembre"):
    numero_giorni = 30
elif mese == "febbraio":
    print("Inserisci l'anno: ")
    anno_ = int(input())
    # bisestile: ogni 4 anni, ogni 400 e non divisibili per 100
    if anno_ % 4 == 0 and (anno_ % 100 != 0 or anno_ % 400 == 0):
        numero_giorni = 29
    else:
        numero_giorni = 28
else:
    numero_giorni = 31

print(mese, "ha", numero_giorni, "giorni")

#--------CON MATCH
mese = input("\nInserisci il nome del mese: ").lower()
numero_giorni = 0

match mese:
    case "novembre" | "aprile" | "giugno" | "settembre":
        numero_giorni = 30
    case "febbraio":
        anno = int(input("Inserisci l'anno per verificare se è bisestile: "))
        # Regola del bisestile: divisibile per 4 e non per 100, oppure divisibile per 400
        if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
            numero_giorni = 29
        else:
            numero_giorni = 28
    case "gennaio" | "marzo" | "maggio" | "luglio" | "agosto" | "ottobre" | "dicembre":
        numero_giorni = 31
    case _:
        print("Mese non valido!")

print(f"Il mese di {mese} ha {numero_giorni} giorni")


#--------------------------------------
# Partendo da una variabile intera:
# il programma deve stampare:
#
# "Il colore è Giallo" se il numero è dispari tra 3 e 15 compresi.
#
# "Il colore è Rosso" se il numero è pari tra 4 e 18 compresi, ma non 12.
#
# "Il colore è Blu" in tutti gli altri casi.

n = 3

# Condizione per il Giallo (Dispari tra 3 e 15 inclusi)
if n % 2 == 1 and 3 <= n <= 15:
    print("Il colore è Giallo")

# Condizione per il Rosso (Pari tra 4 e 18 inclusi, escluso il 12)
# Ci entra solo se la prima condizione è falsa
elif n % 2 == 0 and 4 <= n <= 18 and n != 12:
    print("Il colore è Rosso")

# In tutti gli altri casi
else:
    print("Il colore è Blu")

#------------------------------------------------------------
#oppure con gestione degli intervalli separati
n = 3

intervallo1 = (
    n % 2 == 1
    and 3 <= n <= 15
)

if intervallo1:
    print("Il colore è Giallo")


intervallo2 = (
    n % 2 == 0
    and 4 <= n <= 18
    and n != 12
)


if intervallo2 and not intervallo1:
    print("Il colore è Rosso")


if not intervallo1 and not intervallo2:
    print("Il colore è Blu")

#-------------------------------------------

# esercizio "immagine colore"

colore = "rosso"
match colore:
    case "blu":
        print("Il colore selezionato è blu")
    case "giallo":
        print("Il colore selezionato è giallo")
    case "verde":
        print("Il colore selezionato è verde")
    case "rosso":
        print("Il colore selezionato è rosso")
    case "arancione":
        print("Il colore selezionato è arancione")
    case _:
        print("Nessun colore corrispondente alla tua selezione")

#--CON IF
colore = "rosso"
if colore == "blu":
    print("Il colore selezionato è blu")
elif colore == "giallo":
    print("Il colore selezionato è giallo")
elif colore == "verde":
    print("Il colore selezionato è verde")
elif colore == "rosso":
    print("Il colore selezionato è rosso")
elif colore == "arancione":
    print("Il colore selezionato è arancione")
else:
    print("Nessun colore corrispondente alla tua selezione")
