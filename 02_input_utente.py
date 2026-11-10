#notebook jupiter estensione ipynb
# In PYTHON, per leggere l'input da tastiera si usa la funzione predefinita input()
# legge sempre una riga di testo (una stringa) da tastiera.

# Nome (stringa)
nome = input("Qual è il tuo nome? ")
print(f"Ciao {nome}!")

print("colore preferito")
colore = input()
print("il colore è", colore)

# Età (intero)
eta = int(input("Quanti anni hai? "))
print(f"Hai {eta} anni.")

# #ATTENZIONE!: input() restituisce SEMPRE una stringa, anche se l'utente digita un numero!

# In Python bisogna SEMPRE convertire esplicitamente il testo nel tipo che serve, con int() o float().

# In Python NON possiamo SOMMARE direttamente stringhe e numeri con il '+'
# print("Hai " + 51 + " anni") NO! ERRORE STRINGA + NUMERO

#VERSIONE CORRETTA:
print("Hai " + str(51) + " anni") #CONVERSIONE NUMERO A STRINGA
#È ANCHE PER QUESTO MOTIVO CHE SI USANO LE FSTRING CHE NON NECESSTANO DI CONVERSIONE NEL PRINT

# Altezza In Python si usa il PUNTO, NON la virgola!
altezza = float(input("Quanto sei alto? "))
print(f"Sei alto {altezza} metri.")

# per sostituire automaticamente eventuali virgole inserite per errore.
# altezza_inserita = input("Quanto sei alto? (Usa il punto per i decimali, es: 1.75) ")
# altezza = float(altezza_inserita.replace(',', '.'))

# lettera preferita (prendiamo semplicemente il primo elemento [0] della stringa.)
iniziale = input("Qual è la tua lettera preferita? ")[0]
print(iniziale)

# Python non possiede un input booleano 
# Convertiamo quindi il testo inserito in un booleano.

piace_programmare = input("Ti piace la programmazione? (si/no) ").lower() == "si" #conversione in minuscolo e confronto
print(f"Ti piace la programmazione: {piace_programmare}")

# ---------------------------------------------
# ----------------------- ESERCIZI SCANNER --------------------------------------

# Chiedere all'utente una temperatura in °C e convertirla in °Kelvin
# Formula: K = C + 273.15

print("\n--- ESERCIZIO 1: Conversione Celsius -> Kelvin ---")
temp_str = input("Inserisci la temperatura da convertire in °C: ")
temp = float(temp_str.replace(',', '.')) 
print(f"la temp in ° kelvin è {temp + 273.15}")        

# ---------- ESERCIZIO 2 ----------
# Scrivere un programma che chiede all'utente 2 numeri con la virgola, 
# li somma e stampa il risultato come numero intero.

print("\n--- ESERCIZIO 2: Somma con arrotondamento a intero ---")
num1 = float(input("inserisci il primo numero con la virgola: "))
num2 = float(input("inserisci il secondo numero con la virgola: "))

# In Python il "cast" a intero si effettua passando il valore alla funzione int()
# Questo tronca la parte decimale, esattamente come (int) in Java.
ris = int(num1 + num2)
print(f"la somma è: {ris}")

# ----------------------- ESERCIZIO 5 -----------------------------------------
# Chiede all'utente 4 numeri e ne calcola la somma con 2 variabili.

print("\n--- ESERCIZIO 5: Somma di 4 numeri (con 2 variabili) ---")
totale = 0
# In Python non serve dichiarare preventivamente le variabili. 
# Vengono create direttamente al momento del primo utilizzo.

valore = int(input("inserisci il primo numero: "))
totale += valore

valore = int(input("inserisci il secondo numero: "))
totale += valore

valore = int(input("inserisci il terzo numero: "))
totale += valore

valore = int(input("inserisci il quarto numero: "))
totale += valore

print(f"totale= {totale}")

# ----------------------- ESERCIZIO 5 (Alternativa) ----------------------------      
# Chiede all'utente 4 numeri e ne calcola la somma con 1 sola variabile.

print("\n--- ESERCIZIO 5b: Somma di 4 numeri (con 1 sola variabile) ---")
tot = 0
tot += int(input("inserisci il primo numero: "))
tot += int(input("inserisci il secondo numero: "))
tot += int(input("inserisci il terzo numero: "))
tot += int(input("inserisci il quarto numero: "))
print(f"totale= {tot}")          

# ///////////////////// ESERCIZIO 6 //////////////////////////////////////////////
# Chiede all'utente un tempo espresso in ore con la virgola (es. 3.5 = 3 ore e mezza)
# e stampa il tempo espresso in minuti (intero, es. 210).
    
print("\n--- ESERCIZIO 6: Conversione Ore -> Minuti ---")
ore = float(input("inserisci le ore decimali (es. 3.5): ").replace(',', '.'))
minuti = int(ore * 60)
        
print(f"minuti= {minuti}")        