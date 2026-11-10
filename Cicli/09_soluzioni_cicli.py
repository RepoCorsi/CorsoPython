import random

# Esercizio 3:
#Chiede di inserire un numero maggiore di zero e stampa tutti i numeri da 0 fino al numero inserito.
# Se il valore è negativo stampa un errore.
numero = int(input("inserisci un numero: "))
if numero < 0:
    print("errore! numero negativo")
for i in range(numero + 1):
    print(i)

#--variazione: continuare a chiedere finchè non mette 0. col while:
while True:
  numero = int(input("Inserisci un numero maggiore di 0: "))

  if numero <= 0:
    print("Errore: Il valore è zero oppure negativo. Riprova!")
  else:
    # Se il numero è valido, usciamo dal ciclo
    break

print(f"Ecco i numeri da 0 a {numero}:")
for i in range(numero + 1):
  print(i)
#-------------------------------------------------

# Esercizio 4: Disegna un triangolo di asterischi in base al numero di righe inserito.
num_righe = int(input("inserisci il numero di righe: "))
for i in range(num_righe):
    for x in range(i + 1):
        print("*", end="")
    print()
#-----oppure
for i in range(num_righe):
    print("*" * (i + 1))

#-------------------------------------
# Inserisce numeri finché non si mette 0 (variante do-while )
while True:
    y = int(input("inserisci un numero "))
    print("hai inserito", y)
    if y == 0:
        break

# Esercizio 5: # Chiede quanti numeri sommare e ne calcola il totale
somma = 0
numeri = int(input("quanti numeri vuoi sommare? "))
for i in range(1, numeri + 1):
    num = int(input(f"inserisci il numero {i} "))
    somma += num
print("la somma è", somma)

# Esercizio 6: quanti pari e quanti dispari da 0 a un numero casuale
pari = 0
dispari = 0
n = random.randint(0, 100)
for i in range(n + 1):
    if i % 2 == 0:
        pari += 1
    else:
        dispari += 1
print("numero casuale:", n)
print(f"Nell'intervallo tra 0 e {n} ci sono: {pari} pari e {dispari} dispari")

# Esercizio 8: Visualizza i numeri dispari da 1 a 10, uscendo quando il valore è 7
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i == 7:
        break
    print(i)

# Esercizio 9:  Cerca se un numero casuale da 1 a 20 è presente nell'intervallo da 1 a 10
trovato = False
casuale = random.randint(1, 20)
print("il numero casuale è:", casuale)
for i in range(1, 11):
    if casuale == i:
        trovato = True
        break
ris = f"il numero {casuale} è stato trovato" if trovato else f"il numero {casuale} non è stato trovato"
print(ris)

# Esercizio 12: stampa una frase andando a capo a ogni spazio
frase = "tanto va la gatta al lardo..."
for c in frase:
    if c == ' ':
        print()
        continue
    print(c, end='')

# Esercizio 13: frase al contrario
# frase = "tanto va la gatta al lardo..."
frase = "tanto va la gatta al lardo..."
contrario = frase[::-1]
print(contrario)

#metodo lungo
# contrario = ""
# for i in range(len(frase) - 1, -1, -1):
    # contrario += frase[i]
# print(contrario)


# Esercizio 17: Conta gli spazi presenti in una frase
frase = "tanto va la gatta al lardo..."
numero_spazi = 0
for spazio in frase:
    if spazio == ' ':
        numero_spazi += 1
print(numero_spazi)
#--oppure più semplice:
numero_spazi = frase.count(' ')
print(numero_spazi)

#-----
# Esercizio 19: indovina il numero misterioso casuale da 0 a 10 con un massimo di 10 tentativi
import random
num_misterioso = random.randint(0, 10)

# Facciamo un ciclo da 1 a 10 tentativi
for tentativo in range(1, 11):
  indovina = int(input(f"Tentativo {tentativo}/10 - Inserisci un numero: "))

  if indovina == num_misterioso:
    print(f"Indovinato! in {tentativo} tentativi.")
    break

  if indovina < num_misterioso:
    print("Il numero misterioso è più grande!")
  else:
    print("Il numero misterioso è più piccolo!")
    
  if tentativo==10:
    print("hai finito i tentativi! il numero era",num_misterioso)

#-----
# Esercizio 11: gioco dei dadi tra due giocatori A e B
punti_a = 30
punti_b = 30
while punti_a > 0 and punti_b > 0:
    dado_a = random.randint(1, 6)
    dado_b = random.randint(1, 6)
    print("dadoA=", dado_a, "dadoB=", dado_b)
    if dado_a > dado_b:
        punti_b -= dado_a
        print("Vince A.", end=" ")
    elif dado_b > dado_a:
        punti_a -= dado_b
        print("Vince B", end=" ")
    print("PuntiA", punti_a, "puntiB=", punti_b)
    if punti_a <= 0:
        print("Vince B")
    elif punti_b <= 0:
        print("Vince A")

#-----------------------------------------
# Esercizio 12: caramelle
caramelle = 50 #costanti in MAIUSCOLO
PREZZO = 0.5
while caramelle > 0:
    print("Sono disponibili", caramelle, "caramelle")
    num = int(input("Quante ne vuoi comprare? "))
    if num < 0:
        print("Numero errato")
    else:
        if num > caramelle:
            num = caramelle
            print("Hai chiesto troppe caramelle")
            print("Te ne darò soltanto", num)
        caramelle -= num # Sottrazione dal negozio
        print("Costo:", num * PREZZO, "euro")
print("CARAMELLE TERMINATE!")

#-----------------------------------------------
# Esercizio: frase divisa in caratteri di posto pari e dispari
frase = "tanto va la gatta al lardo..."
pari = ""
dispari = ""
for i in range(len(frase)):
    if frase[i] == ' ':
        continue
    if i % 2 == 0:
        pari += frase[i]
    else:
        dispari += frase[i]
print(pari)
print(dispari)

# ************** FIBONACCI (soluzione, col for e col while) *****************
# limite = random.randint(0, 20)
# print(limite)
# num1 = 0
# num2 = 1
# for i in range(limite):
#     print(num1, end=" ")
#     somma = num1 + num2
#     num1 = num2
#     num2 = somma
#
# print("")
# i = 0
# num_a = 0
# num_b = 1
# while i < limite:
#     print(num_a, end=" ")
#     tot = num_a + num_b
#     num_a = num_b
#     num_b = tot
#     i += 1
