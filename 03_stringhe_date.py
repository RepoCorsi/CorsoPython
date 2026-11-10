from datetime import datetime

# In Python le date si ottengono dal modulo "datetime"
# della libreria standard.

oggi = datetime.now()
print("Data e ora attuali:", oggi) # contiene sia la data che l'ora

print("************")

# estrarre parti di data
data = oggi.date() #solo data senza ora
print("Solo data:", data)

ora = oggi.time()#solo ora
print("Solo ora:", ora)

giorno=oggi.day#solo giorno
print("solo giorno",giorno)

mese=oggi.month #solo mese
print("solo mese",mese)

anno=oggi.year #solo anno
print("solo anno",anno)

data_con_ora = datetime.now() #di nuovo tutta la data
print("Data con ora:", data_con_ora)

# per formattare strftime()
formato = data_con_ora.strftime("%d/%m/%Y %H:%M:%S")#Anno di 4 cifre e ore 1-24
print(formato)

formato = data_con_ora.strftime("%d/%m/%y %I:%M:%S %p")#Anno di 2 cifre e ore 1-12 AM/PM
print(formato)

# Codice	Significato
# %d	giorno (01–31)
# %m	mese (01–12)
# %Y	anno con 4 cifre
# %y	anno con 2 cifre
# %H	ora (00–23) 24 ore
# %I	ora (1–12 ) 12 ore
# %p	AM/PM
# %M	minuti
# %S	secondi
# %A	nome completo del giorno della settimana

# NOTA: i nomi dei giorni/mesi che strftime() produce dipendono dalla
# "locale" del sistema. Per ottenerli in italiano in modo affidabile,
# si usa il modulo "locale";
import locale

locale.setlocale(locale.LC_TIME, "Italian_Italy.1252")

nome_giorno = datetime.now().strftime("%A")
nome_mese = datetime.now().strftime("%B")
print("nome giorno", nome_giorno)
print("nome mese", nome_mese)

#----Differenza tra 2 date:
inizio = datetime(2026, 9, 24, 10, 0, 0)  #non usare strftime perchè diventa stringa e non fa la differenza
fine = datetime(2026, 9, 25, 10, 0, 0)    #non usare strftime perchè diventa stringa e non fa la differenza

differenza = fine - inizio
# Converti la differenza totale in giorni
giorni = differenza.days
print(f"Differenza: {giorni} giorni") 

# Converti la differenza totale in ore. 1 ora sono 3600 secondi.
ore = differenza.total_seconds() / 3600 # Usare total_seconds() non seconds()! Seconds() sono i secondi rimanenti alla succesiva ora.
print(f"Differenza: {ore} ore") 


# ESERCIZIO: Stampare la data di oggi col formato "Oggi è il gg*MM*aaa. Sono le ore HH:mm:S di giovedì"
oggi = datetime.now()

print(oggi.strftime("Oggi è il %d*%m*%Y. Sono le ore %H:%M:%S di %A"))
print("*"*30)
print(f"Oggi è il giorno {oggi.day:02d}*{oggi.month:02d}*{oggi.year}. Sono le ore {oggi.hour:02d}:{oggi.minute:02d}:{oggi.second:02d} di {oggi.strftime('%A')}")

# **************STRINGHE***********************
parola = "ciao "
parola2 = "a tutti"
parola3 = parola + parola2
print(parola3)

# lunghezza della stringa
lunghezza = len(parola)
print(lunghezza)

# controlla se inizia/finisce con una parola: False se non trovato
finisce_con = parola3.endswith("tutti")
inizia_con = parola3.startswith("ciao")
print(finisce_con, inizia_con)

# find() restituisce l'indice della PRIMA occorrenza trovata, oppure -1 se non trovata
pos_tutti = parola3.find("tutti")
print(pos_tutti)

# find() a partire da una posizione specificata
seconda_t = parola3.find("t", pos_tutti + 1)
print(seconda_t)

# un "carattere" a una posizione: in Python basta l'indice tra parentesi quadre.
name = "Fabio"
ch = name[2]  # 3 carattere.se l'indice è troppo grande, Python solleva IndexError
print(ch)  # b

stringa = "ciao a tutti"
lungh = len(stringa)
print(stringa[0])  # primo carattere
print(stringa[lungh - 1])  # ultimo carattere
# NOTA: Python offre anche un indice negativo più comodo per l'ultimo
# carattere, senza dover calcolare la lunghezza:
print(stringa[-1])  # stesso risultato, più idiomatico

# contiene: in Python si usa l'operatore "in"
my_str = "ciao"
print("cia" in my_str)  # True
print("o" in my_str)  # True
print("Hello" in my_str)  # False

# confronto tra stringhe:
# Python le stringhe si confrontano già correttamente con "=="
stringa1 = "ciao"
stringa2 = "ciao"
uguali = stringa1 == stringa2
print("stringa1==stringa2", uguali)

stringa2 = "CIAO"
uguali_no_case = stringa1.lower() == stringa2.lower()  # equivalente di equalsIgnoreCase()
print("NoCase", uguali_no_case)

# è vuota?
print("è vuota?", stringa2 == "")
# oppure controllando se la lunghezza è 0.
stringa_vuota = ""
print("è vuota?", len(stringa_vuota) == 0)

# substring() diventa lo slicing con [inizio:fine] (estremo finale escluso, esattamente come in substring())
#inizio è incluso, fine è escluso.
parola4 = "ciao a tutti"
tutti = parola4[7:12]
print("substring =", tutti)#tutti

ciao = parola4[0:4]
print("substring =", ciao)#ciao

#Puoi anche omettere gli indici
#Dall'inizio fino a 4
ciao = parola4[:4]  #ciao
print("substring =", ciao)

#Da 7 fino alla fine
tutti =parola4[7:] #tutti
print("substring =", tutti)

#Tutta la stringa
parola4[:] #ciao a tutti

#puoi anche usare un terzo parametro
#sequenza[inizio:fine:passo]
passo=parola4[0:12:2] #parti da 0, arriva prima di 12, prendendo un carattere ogni 2.
print(passo)

#Passo negativo: andare al contrario
contrario=parola4[::-1]
print(contrario) #ittut a oaic

# replace: in Python replace() sostituisce già
# tutte le occorrenze, non serve un metodo separato per "tutte")
print(parola4.replace("tutti", "nessuno"))

print(parola4.replace(" ", "")) #elimina gli spazi

numero = float(input("inserisci un numero decimale: ").replace(',', '.')) #cambia la virgola con un punto

##--Esempio palindromo ------------------
palindromo="i topi non avevano nipoti"
contrario=palindromo[::-1]
print(contrario)

print(parola4.replace(" ","")) #tolgo gli spazi 
print(palindromo.replace(" ","")[::-1])#tolgo gli spazi e lo giro al contrario


# NOTA: le stringhe Python sono immutabili: ogni
# operazione ne restituisce una NUOVA, lasciando l'originale intatta.
print(parola4)

print(parola4.upper())
print(parola4.lower())

# CARATTERI DI ESCAPE:
print('ciao a "tutti"')
print("c:\\windows\\..")
print("ciao\na tutti")
print("ciao\ta tutti")

#--ESERCIZI:

#Dalla parola "Python" ottenere le sottostringhe:
# Py
# tho
# n
# Pyt
# hon
# Python
# Pto
# nohtyP

parola = "Python"

print(parola[0:2])    # Py
print(parola[2:5])    # tho
print(parola[-1])     # n
print(parola[:3])     # Pyt
print(parola[3:])     # hon
print(parola[:])      # Python
print(parola[::2])    # Pto
print(parola[::-1])   # nohtyP

#-------------------------------------------
# A partire dalla stringa "Python è un bel linguaggio di programmazione"

# ritagliare la parola linguaggio e stampare la posizione.
# trovare la posizione dell'ultimo carattere della frase.
# ritagliare a partire dalle posizioni trovate, la stringa "linguaggio di programmazione"        
# trovare la posizione della seconda g

frase="Python è un bel linguaggio di programmazione"
#trova linguaggio
# 1. Trovare la posizione della parola "linguaggio"
posizione = frase.find("linguaggio")
print(posizione)
linguaggio=frase[posizione:26]#estremo non compreso, qindi si fa +1.
print(linguaggio)

#posizione ultimo carattere:
# 2. Trovare l'ultimo carattere (in Python semplicemente l'indice della lunghezza - 1)
ultimo = len(frase) - 1
print(ultimo)
print(linguaggio[-1]) # oppure print(frase[43])

#Linguaggio di programmazione
# 3. Ritagliare "linguaggio di programmazione"
parte = frase[posizione:] 
print(parte)# oppure print(frase[16:])

# Posizione della seconda "g"
# 4. Trovare la posizione della seconda "g"
prima_g = frase.find("g")
seconda_g = frase.find("g", prima_g + 1)
print("Posizione della seconda g:", seconda_g)