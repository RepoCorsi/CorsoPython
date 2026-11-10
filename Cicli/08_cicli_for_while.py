# ****************** CICLO FOR *********************************
# Si usa la funzione integrata range(start, stop, step).
for i in range(10):  # 10 numeri da 0 a 9 (lo stop non è mai incluso)
    print("i=", i)


for i in range(2,5):  # 3 numeri da 2 a 4 (lo stop non è mai incluso)
    print("i=", i)

# al contrario: 10 numeri da 10 a 1
#partiamo da 10, ci fermiamo prima di 0 (quindi a 1), decrementando di 1
for i in range(10, 0, -1): #-1 è obbligatorio altrimenti non stampa nulla
    print("i=", i)

# salta di 2 ogni volta: solo i pari da 0 a 8
for i in range(0, 10, 2):  
    print("i=", i)

# caratteri stampabili della tabella ascii
for i in range(127):  
    print(f"{i}: {chr(i)}")


#stampare una lista di valori (ci torniamo dopo con una lezione apposta)
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeri:
    print("numero: ",numero)


# Stampa una stringa in verticale carattere per carattere
a = "ciao a tutti"
for lettera in a:
    print(lettera)

# Stampa  al contrario
parola="ciao"
for lettere in parola[::-1]:
    print(lettere, end=" ")


# Stampa NUMERI al contrario
numeri = 739162
cifre = str(numeri)

for cifra in cifre[::-1]:
    print(cifra, end=" ")

#se non serve l'indice si usa _
for _ in range(10):  # 0 a 9
    print("ciao")

# Conta il numero di spazi in una frase
frase = "Ciao a tutti oggi è una bella giornata"
numero_spazi = 0
for carattere in frase:
    if carattere == ' ':
        numero_spazi += 1
print("Spazi= " ,numero_spazi) #7

#-----
# molto più semplice usando le funzioni di stringa .count()
frase = "Ciao a tutti oggi è una bella giornata"
numero_spazi = frase.count(" ")
print("Spazi =", numero_spazi)
#--------------------------------------------

# Trovare un valore casuale tra altri
import random
trovato = False
casuale = random.randint(1, 20) #1, 20 inclusi
print("il numero casuale è:", casuale)

for i in range(1, 11): # Da 1 a 10
    if casuale == i:
        trovato = True
        break

if trovato:
    print("il numero è stato trovato")
else:
    print("il numero non è stato trovato")
    
# Con operatore ternario in Python: 'valore_se_vero if condizione else valore_se_falso'
risultato = "il numero è stato trovato" if trovato else "il numero non è stato trovato"
print(risultato)
#------------------
# Anche qui senza ciclo for ma con in 
# Usiamo 'in' direttamente sul range (da 1 a 10 inclusi)
if casuale in range(1, 11):
    print("Il numero è stato trovato")
else:
    print("Il numero non è stato trovato")
#---------------------------------------------


# fattoriale
fact = 1  # niente distinzione int/long
for i in range(1, 11): # Fattoriale di 10
    fact *= i
print("Fattoriale=", fact)

# *************** Cicli annidati: Tabella Pitagorica *******************************
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j}", end="\t") #tabulazione per non andare a capo
        #print("\t", i * j, end="")
    # Va a capo alla fine della riga esterna
    print()

# *************** Allineamenti **********************
# NOTA: la sintassi "%[flag][dimensione]d" di printf esiste anche in
# Python con lo stesso significato, dentro una f-string o con format():
print(f"numero=:{10000:08d}")  # zeri iniziali, minimo 8 cifre
print(f"numero=:{10000:<8d}#")  # allineato a sinistra, minimo 8 cifre
print(f"numero=:{10000:,}")  # separatore delle migliaia

print(f"{'left justified:':<25}")
print(f"{'right justified:':>25}")
print()  # Vado a capo


# ********* conta vocali**********************************
import string #per usare ascii_lowercase

vocale = 0
consonante = 0
for lettera in string.ascii_lowercase: #lettere da a - z
    if lettera in "aeiou":
        print(lettera, "è una vocale")
        vocale += 1
    else:
        print(lettera, "è una consonante")
        consonante += 1
print("vocali:", vocale, "consonanti:", consonante)

#******* CON MATCH-CASE ***************************
# Ciclo su tutte le lettere dell'alfabeto da 'a' a 'z'
for lettera in string.ascii_lowercase:
    match lettera:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print(f"{lettera} è una vocale")
            vocale += 1
        case _:
            print(f"{lettera} è una consonante")
            consonante += 1
            
print(f"vocali: {vocale} consonanti: {consonante}")

#----------------------------------------------------


# ******************** Break & Continue ************************************
# Esempio continue: salta l'istruzione quando n è uguale a 5
for n in range(1, 11):
    if n == 5:
        continue #salta solo il 5
    print(n)

# Esempio break: interrompe il ciclo quando n è uguale a 5
for n in range(1, 11):
    if n == 5:
        break #esce dal ciclo al 5
    print(n)


# **************  FIBONACCI  ***************************
#0 1 1 2 3 5 8 13 21  #il secondo è la somma del primo+il secondo
limite = random.randint(1, 20)
print(limite)

num1, num2 = 0, 1
for _ in range(limite):
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2 #il secondo è la somma del primo+il secondo
    # somma = num1 + num2
    # num1 = num2
    # num2 = somma
print()  # Va a capo alla fine della sequenza


# **************CICLO WHILE **********************************
contatore1 = 0
while contatore1 < 10:
    print("contatore1:", contatore1)
    contatore1 += 1


#   CICLO INFINITO 
# *** Do While non esiste in python
# Continua a chiedere finché non si mette 0
while True:
    print("Inserisci un numero, 0 per uscire:")
    if int(input()) == 0:
        print("ciao")
        break
#-----------------------
#con operatore walrus := dichiaro e uso direttamente il valore nel while
# Il ciclo continua finché il numero è diverso da 0
while (numero := int(input("Inserisci un numero (0 per uscire): "))) != 0:
    if numero<0: #opzionale gestione dei numeri negativi
        print("non puoi inserire numeri negativi")  #opzionale gestione dei numeri negativi
# Nel momento esatto in cui viene inserito 0, il ciclo termina e si arriva qui:
print("ciao")
#-----------------

#trovare la password:
password = "abcdef"
tentativoUser = ""
numTentativi = 0

while tentativoUser != password:
    tentativoUser = input("Inserisci la password: ")
    numTentativi += 1

print(f"Bravo, hai trovato la password in {numTentativi} tentativi")

# *********************** Con lettere *************************************
#Scorrere le lettere con il While (Tabella ASCII)
lettera = 'a'
while lettera <= 'z':
    print(lettera)
    lettera = chr(ord(lettera) + 1)

#stesso esempio con il for
print()
for lettera in range(ord("a"),ord("z")+1):
    print(chr(lettera))
    
#oppure:
import string

for lettera in string.ascii_lowercase:
    print(lettera)


#---Fibonacci  COL WHILE
print("")

i = 0
num_a = 0
num_b = 1
while i < limite:
    print(num_a, end=" ")
    numA, numB = numB, numA + numB
    # tot = num_a + num_b
    # num_a = num_b
    # num_b = tot
    i += 1
