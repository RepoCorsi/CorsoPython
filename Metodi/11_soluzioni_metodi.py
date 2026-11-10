import random

#isDivisibile
# Creare un metodo che dati un numero intero a e un numero intero b in input, dica se a è divisibile per b. 
# Deve restituire un booleano.
def is_divisible(num1, num2):
    return num1 % num2 == 0
#---------------------------------------------

# 1) pari o dispari
#1) Creare un programma che controlli tramite una funzione se un numero passato in input è pari o dispari.
#Deve restituire un booleano .
def pari_dispari(num):
    return num % 2 == 0
#-----------------------------------------------

# 2) ripete una stringa n volte
# Scrivere una funzione Ripeti che chiede all’utente di inserire una stringa e un numero intero positivo, da passare in input alla funzione, 
#e che stamperà tante volte la stringa quante indicate nel numero inserito dall’utente. 
#Se il numero inserito dall’utente è negativo il metodo stamperà "ERRORE: numero negativo". 
def ripeti(s, n):
    if n < 0:
        print("errore. Numero negativo")
    else:
        for _ in range(n):
            print(s)
#------------------------------------------------

# 3) Creare una funzione che accetti una stringa in input, e la restituisca al contrario. 
def reverse(parola):
    contrario = ""
    for i in range(len(parola) - 1, -1, -1):
        contrario += parola[i]
    # NOTA: come già segnalato in altri file, Python offre anche lo
    # slicing "a passo -1" come scorciatoia: return parola[::-1]
    return contrario
#--------------------------------------------

# 4) se i 2 numeri sono uguali li incrementa di uno e li stampa
#Creare una funzione che accetti 2 numeri inseriti dall’utente:
#Se i numeri sono uguali li incrementa di uno e li stampa, altrimenti li stampa senza incrementarli.
def incrementa_se_uguali(n1, n2):
    if n1 == n2:
        n1 += 1
        n2 += 1
        print(n1, n2)
    else:
        print(n1, n2)
#------------------------------------------------

# 5) calcolatrice
#Creare una funzione calcolatrice che accetti in input 2 numeri e l'operatore(+  -  * / max min), e restituisca il risultato dell'operazione richiesta.
#Se nel caso della divisione il divisore è zero, scrivere un messaggio di errore e ritornare -99999.
def calc(num1, num2, operazione):
    ris = 0
    if operazione == "+":
        ris = num1 + num2
    elif operazione == "-":
        ris = num1 - num2
    elif operazione == "*":
        ris = num1 * num2
    elif operazione == "/":
        if num2 == 0:
            print("Errore, non puoi dividere per 0")
            return -99999
        else:
            ris = num1 / num2
    else:
        print("operazione non consentita")
    return ris
#-------------------------------------------

# 6) conversione dollari/euro
#Creare un programma che permetta la conversione tra Dollari ed Euro e viceversa.
# Creare due metodi: impostaCambio e converti.
# Il metodo impostaCambio prende in input il valore del tasso di Cambio tra le due valute Dollaro e Euro
# Il metodo converti prende in input 2 stringhe valutaDa e valutaA, l'importo da convertire ed esegue la conversione dell'importo in base delle valute specificate.
# Restituire l'importo convertito.
cambio = None

def imposta_cambio(tasso_cambio):
    global cambio
    print("Cambio impostato a", tasso_cambio)
    cambio = tasso_cambio


def converti(valuta_da, valuta_a, importo):
    if valuta_da == "dollari" and valuta_a == "euro":
        return importo * cambio
    elif valuta_da == "euro" and valuta_a == "dollari":
        return importo / cambio
    else:
        print("Le valute specificate non sono supportate.")
        return 0.0
#---------------------------------------------

#-- QUESTO! 1 ---
# 7) posizione di un numero in una lista
#)Creare una funzione che prenda in input una lista di 10 numeri casuali da 0 a 20, ed un numero intero.
#La funzione deve restituire la prima posizione del numero intero nella lista.
#Se il numero non è presente nella lista la funzione deve restituire -1

#--Con il for --
def posizione(lista, numero):
    for i in range(len(lista)):
        if numero == lista[i]:
            return i
    return -1
    
#-------Con i metodi delle stringhe --
def posizione(lista_numeri, target):
    # Verifichiamo prima se il target esiste per evitare che .index() generi un errore
    if target in lista_numeri:
        return lista_numeri.index(target)
    return -1

# Codice di Test
numeri_casuali = [random.randint(0, 20) for _ in range(10)]
print(f"Lista generata: {numeri_casuali}")
print(f"Indice del numero 12: {posizione(numeri_casuali, 12)}")

#---------------------------------------------------
# 8) media di un numero variabile di argomenti
#Creare una funzione che accetti un numero variabile di argomenti di tipo intero in input, e ne restituisca la media.
def media(*x):
    tot = 0
    print("Hai passato questi numeri:")
    for i in x:
        print(i)
        tot += i
    return tot / len(x)


# -- QUESTO-- 2--
#-------------------------------------------
# 9) unisce 2 array alternando gli elementi
#Creare una funzione che accetta in ingresso due liste a1, a2 di uguale lunghezza, e restituisce un'altra lista formata dal primo elemento di a1, seguito dal primo elemento di a2, dal secondo elemento di a1, seguito dal secondo elemento di a2, e così via. Se le due liste in ingresso non hanno uguale lunghezza, la funzione restituisce None
#Esempio:
#Input: a1 = [1, 2, 3], a2 = ['a', 'b', 'c'] → Output atteso: [1, 'a', 2, 'b', 3, 'c']
#Input: a1 = [1, 2], a2 = ['a', 'b', 'c'] → Output atteso: None

def unisci_liste(a1, a2):
    # Controllo di validazione (lunghezza diversa)
    if len(a1) != len(a2):
        return None
    
    risultato = []
    # Usiamo la lunghezza di una qualsiasi delle due (tanto sono uguali)
    for i in range(len(a1)):
        risultato.append(a1[i])
        risultato.append(a2[i])
        
    return risultato

#-- altro metodo CON ZIP --

def unisci_liste(a1, a2):
    if len(a1) != len(a2):
        return None
    
    risultato = []
    # zip(a1, a2) restituisce coppie di elementi: (a1[0], a2[0]), (a1[1], a2[1]), ...
    for x, y in zip(a1, a2):
        risultato.append(x)
        risultato.append(y)
        
    return risultato

#-- Altro metodo SLICING con PASSO ---
def unisci_liste(a1, a2):
    if len(a1) != len(a2):
        return None
    
    # Creiamo una lista vuota lunga il doppio
    risultato = [0] * (len(a1) * 2)
    # Riempiamo le posizioni pari con a1 e quelle dispari con a2
    risultato[0::2] = a1
    risultato[1::2] = a2
    
    return risultato

# Codice di Test
lista_a = [1, 2, 3]
lista_b = ['a', 'b', 'c']
print(unisci_liste(lista_a, lista_b))  # [1, 'a', 2, 'b', 3, 'c']

#-----------------------------------------------

#-- QUESTO! 3 ---
# Creare una funzione che accetta in input 2 stringhe, e restituisce true se e solo se la stringa s1 NON contiene alcun carattere della stringa s2, restituisce false altrimenti. 
#Ad esempio, per le stringhe “fila” e “computer” la funzione restituisce true perché non vi è alcun carattere in comune.

#Esempio sbagliato perchè controlla alla stessa posizione
# def caratteri_comuni(s1, s2):
    # for i in range(len(s1)):
        # if s2[i] == s1[i]:
            # return False
    # return True

#--Esempi corretti:--
#-Con 2 cicli:
def caratteri_comuni(s1, s2):
    for carattere1 in s1:
        for carattere2 in s2:
            if carattere1 == carattere2:
                return False  # Appena trova un carattere uguale, interrompe tutto
    return True  # Se i cicli finiscono senza trovare uguaglianze

#--Con in --
def caratteri_comuni(s1, s2):
    for carattere in s1:
        if carattere in s2:
            return False  # Trovata una lettera in comune!
    return True

#--con i set isdisjoint
def caratteri_comuni(s1, s2):
    # .isdisjoint() restituisce True se i due set non hanno elementi in comune
    return set(s1).isdisjoint(set(s2))

# Codice di Test
print(caratteri_comuni("fila", "computer"))  # True
print(caratteri_comuni("casa", "albero"))    # False



#---------------------------------------------------
# prima, ultima e terza lettera di una frase
#Creare un metodo che accetti in input una stringa dall' utente di almeno 6 lettere,
#e restituisca un array contenente la prima, l'ultima e la terza lettera
def crea_array(frase):
    return [frase[0], frase[-1], frase[3]]


#-----------------------------------------------------
# ordina 3 numeri con la virgola
#Scrivere un metodo che riceva in input tre numeri con la virgola, e ritorni un array ordinato. 
def ordina(num1, num2, num3):
    numeri = [num1, num2, num3]
    numeri.sort()
    return numeri


# ================== PROVA (equivalente del "main" di Java) ==================

divisibile = is_divisible(10, 2)
print("è divisibile?", divisibile)

print(pari_dispari(6))

ripeti("ciao", 5)

print(reverse("ciao"))

incrementa_se_uguali(3, 2)

ris = calc(10, 2, "/")
print(ris)

imposta_cambio(0.98)
risultato = converti("dollari", "euro", 250.0)
print("250 dollari equivalgono a", risultato, "euro.")


print(media(1, 2, 3, 4, 5))  # 3.0


print("Inserisci una stringa di almeno 6 lettere:")
frase = input()

if len(frase) >= 6:
    arr3 = crea_array(frase)
    print("Array risultato:")
    for lettere in arr3:
        print(lettere)
else:
    print("La stringa inserita non contiene almeno 6 lettere.")

sorted_array = ordina(3.14, 2.718, 1.618)
print("Array ordinato:")
for number in sorted_array:
    print(number)
