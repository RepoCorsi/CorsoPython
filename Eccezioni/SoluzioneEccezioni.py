# ----------------------------------------------------------------------------------------------------------
# ESERCIZIO 1: Somma di due numeri con controllo dello zero
# Creare un metodo che faccia la somma di 2 numeri scelti dall'utente.
# Il programma deve controllare che l'input dello scanner sia numerico, e deve sollevare una eccezione personalizzata nel caso che uno dei 2 numeri sia zero
# ----------------------------------------------------------------------------------------------------------

class ZeroInputException(Exception):
    pass

def somma_due_numeri(num1, num2):
    # Metodo che somma i due numeri e lancia un'eccezione se uno dei numeri è zero
    if num1 == 0 or num2 == 0:
        raise ZeroInputException("Errore: uno dei numeri è zero, non è permesso.")
    return num1 + num2

#--test---
print("inserisci 2 numeri")

try:
    # In Python usiamo input() e convertiamo esplicitamente in intero.
    # Se l'utente inserisce testo non numerico, Python solleva automaticamente ValueError
    # che corrisponde concettualmente a InputMismatchException di Java.
    num1 = int(input("Inserisci il primo numero: "))
    num2 = int(input("Inserisci il secondo numero: "))

    # Chiamata al metodo di somma
    risultato = somma_due_numeri(num1, num2)
    print("La somma dei due numeri è:", risultato)

except ZeroInputException as e:
    # Gestione dell'eccezione se uno dei numeri è zero
    print(e)
except ValueError:
    # Gestione di input non numerici (es. lettere)
    print("Errore nell'input. Per favore, inserisci numeri validi.")

print("-" * 50)


# ----------------------------------------------------------------------------------------------------------
# ESERCIZIO 2: Simulazione portamonete
# Creare un programma che simuli un portamonete.
# Nel portamonete c'è una quantità fissa di monete iniziale a piacere
# Creare un funzione "aggiungi" per aggiungere soldi nel portamonete
# Creare un funzione "spendi" per far spendere l'utente, con importi scelti a piacere.
# Se l'utente spende più della disponibilità del portamonete sollevare una eccezione personalizzata.

# ----------------------------------------------------------------------------------------------------------
class FondiInsufficientiException(Exception):
    pass    

def aggiungi(quanto):
    global disponibilita
    
    if quanto <= 0:
        raise ValueError("L'importo deve essere positivo.")

    disponibilita += quanto


def spendi(quanto):
    global disponibilita
    
    if quanto <= 0:
        raise ValueError("L'importo deve essere positivo.")
    
    if disponibilita < quanto:
        raise FondiInsufficientiException("Non hai tutti questi soldi!, ma solo " + str(disponibilita))
    disponibilita -= quanto
    print("Hai speso " + str(quanto) + " euro. Saldo attuale: " + str(disponibilita))

#------Test----
try:
        
    disponibilita = 10
    aggiungi(10)
    print("hai", disponibilita, "euro")
    
    while disponibilita > 0:
        quanto_spendere = int(input("quanto vuoi spendere? "))
        spendi(quanto_spendere)
        print("Hai ancora", disponibilita)
    
except ValueError as e:
    print("non è un valore valido ->",e)
except FondiInsufficientiException as e:
    print("Errore:", e)

print("-" * 50)


# ----------------------------------------------------------------------------------------------------------
# ESERCIZIO 3: Array (Lista a dimensione fissa) con reset in caso di overflow
# Creare un programma che permetta all'utente di scegliere la lunghezza di un array, e successivamente di riempirlo con dei valori a piacere.
# Il programma deve continuare ad accettare numeri fino a che l'utente non digita la parola "fine"
# Gestire l'eccezione in cui l'utente non digiti la parola fine, e metta più valori di quelli ammessi dall'array.
# In quel caso svuotare l'array e far inserire i valori all'utente.

# ----------------------------------------------------------------------------------------------------------
try:
    lunghezza_array = int(input("Inserisci la lunghezza dell'array: "))
except ValueError:
    print("Lunghezza non valida. Impostata a 3 di default.")
    lunghezza_array = 3

array = [None] * lunghezza_array
indice = 0

print("Inserisci i valori dell'array. Digita 'fine' per terminare.")

while True:
    input_utente = input("Inserisci un valore (oppure 'fine' per terminare): ")

    # Se l'utente digita "fine", esci dal ciclo
    if input_utente.lower() == "fine":
        break

    try:
        valore = int(input_utente)
        
        # Verifichiamo manualmente l'indice per simulare l'IndexOutOfBoundsException
        if indice >= len(array):
            raise IndexError()
            
        array[indice] = valore
        indice += 1

    except ValueError:
        print("Valore non valido. Inserisci un numero intero.")
    except IndexError:
        # Se l'array è pieno (abbiamo superato i limiti consentiti)
        print("Hai inserito più valori di quelli consentiti per l'array!")
        # Svuota l'array (lo ricreiamo) e ripartiamo da capo
        array = [None] * lunghezza_array
        indice = 0  # resettiamo l'indice
        print("Array resettato. inserisci di nuovo i valori.")

# Visualizza i valori finali dell'array inseriti fino a quel momento
print("I valori dell'array sono:")
for i in range(indice):
    print(array[i])

print("-" * 50)

# ----------------------------------------------------------------------------------------------------------
# ESERCIZIO 4: Manipolazione stringa e eccezioni sui tipi di dato
# Creare un metodo che accetti in input una stringa e un numero.
# Chiedere all'utente una stringa e un numero, e ritornare la parte di stringa che va da quel numero(posizione) in poi.
# Se la lunghezza della stringa è minore di 2, sollevare una eccezione personalizzata.
# Se il numero è più grande della lunghezza della stringa sollevare un'altra eccezione personalizzata.
# Sollevare l'eccezione giusta se i tipi di dati inseriti non sono rispettivamente una stringa o un numero.
# ----------------------------------------------------------------------------------------------------------
        
class StringaTroppoCortaException(Exception):
    pass


class NumeroTroppoGrandeException(Exception):
    pass


class TipoDatoErratoException(Exception):
    pass

#--Funzione
def estrai_parte_stringa(input_string, numero):
    # Verifica se i tipi di dato sono corretti (equivalente all'uso di instanceof in Java)
    if not isinstance(input_string, str) or not isinstance(numero, int):
        raise TipoDatoErratoException("I dati forniti devono essere una stringa e un numero intero.")

    # Verifica se la lunghezza della stringa è inferiore a 2
    if len(input_string) < 2:
        raise StringaTroppoCortaException("La stringa deve essere lunga almeno 2 caratteri.")

    # Verifica se la posizione è maggiore della lunghezza della stringa
    if numero > len(input_string):
        raise NumeroTroppoGrandeException("La posizione è troppo grande rispetto alla lunghezza della stringa.")

    # Ritorna la parte della stringa dalla posizione specificata in poi (slicing)
    return input_string[numero:]

#--Test----
print("Inserisci una stringa e una posizione:")

try:
    stringa_input = input("Stringa: ")
    posizione_stringa_raw = input("Posizione: ")
    
    # Simuliamo il controllo del tipo di dato per l'input numerico
    # Se l'utente non inserisce un numero intero, solleviamo un errore di tipo
    if not posizione_stringa_raw.isdigit():
        raise TipoDatoErratoException("I dati forniti devono essere una stringa e un numero intero.")
        
    posizione_stringa = int(posizione_stringa_raw)
    
    risultato_stringa = estrai_parte_stringa(stringa_input, posizione_stringa)
    print("Risultato:", risultato_stringa)
    
except (StringaTroppoCortaException, NumeroTroppoGrandeException, TipoDatoErratoException) as e:
    print("Errore:", e)
except Exception as e:
    print("Errore generico:", e)
        

# ----------------------------------------------------------------------------------------------------------
# ESERCIZIO 5:  Biglietteria: controllo dell'età
# ----------------------------------------------------------------------------------------------------------
#Scrivi un programma per una biglietteria che venda biglietti per un parco divertimenti.
#Crea due eccezioni personalizzate:
#EtaNonValida: da utilizzare quando l'età inserita è negativa.
#MinorenneNonAccompagnato: da utilizzare quando una persona ha meno di 14 anni e non è accompagnata.

# Se l'età è negativa, solleva EtaNonValida.
# Se l'età è inferiore a 14 e la persona non è accompagnata, solleva MinorenneNonAccompagnato.
# In tutti gli altri casi, stampa Accesso consentito!
#Creare una funzione def verifica_accesso(eta, accompagnato):


class EtaNonValida(Exception):
    pass


class MinorenneNonAccompagnato(Exception):
    pass


def verifica_accesso(eta, accompagnato):
    if eta < 0:
        raise EtaNonValida("L'età non può essere negativa.")

    if eta < 14 and not accompagnato:
        raise MinorenneNonAccompagnato(
            "I minori di 14 anni devono essere accompagnati."
        )

    print("Accesso consentito!")


# Test del programma
try:
    verifica_accesso(-2, False)

except EtaNonValida as e:
    print("Errore:", e)

except MinorenneNonAccompagnato as e:
    print("Errore:", e)


try:
    verifica_accesso(10, False)

except EtaNonValida as e:
    print("Errore:", e)

except MinorenneNonAccompagnato as e:
    print("Errore:", e)


try:
    verifica_accesso(10, True)

except EtaNonValida as e:
    print("Errore:", e)

except MinorenneNonAccompagnato as e:
    print("Errore:", e)


try:
    verifica_accesso(18, False)

except EtaNonValida as e:
    print("Errore:", e)

except MinorenneNonAccompagnato as e:
    print("Errore:", e)
