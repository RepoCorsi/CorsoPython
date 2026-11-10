# In Python TUTTE le eccezioni sono "unchecked" (a runtime). Non obbligano a gestirle come in java
# Non esiste il concetto di "Checked Exception" (eccezioni controllate in compilazione) come in Java.

a = 10
b = 2
c = 0
# gestione delle eccezioni
try:  # provo a eseguire questo blocco di codice
    c = a / b
    print(c)
    # se noto un problema, eseguo quello che c'è nell'except
    # posso mettere più except, uno dopo l'altro
except ZeroDivisionError as e:
    print("Niente panico, è solo una divisione per 0",e) #dentro e ho la descrizione dell'errore. # Se voglio il tipo devo usare e.__class__
    
    c = -1 #valore di default in caso di errore
except Exception:  # va messo per ultimo: gestisce tutti gli altri tipi di eccezione
    print("Errore che non so qual è, ma l'ho gestito lo stesso")
finally:  # eseguito comunque, a prescindere dall'errore
    print("io vengo eseguito lo stesso anche se non ci sono errori")


print("il codice può continuare con c=", c)
# -------------------------------------------------------------

#Errore di tipo sbagliato :TypeError
try:
    numero = 10
    testo = "5"

    risultato = numero + testo
    print(risultato)
except TypeError as e:
    print("errore di tipo:",e)

#----Altro esempio:
try:
    numero = 10
    print(len(numero)) #errore, un numero intero non ha lunghezza
except TypeError as e:
    print("errore di tipo:",e)    
    
#------------------------------------------------------------
#ValueError: 
#valore non valido o dato errato
#Si verifica quando il tipo di dato è corretto, ma il valore non può essere utilizzato nel modo richiesto.

try:
    numero = int("5") #si può fare
    print(numero,type(numero))
    
    numero = int("ciao") #non si può fare
except ValueError as e:
    print("Errore: Non puoi convertire una stringa in un numero: ",e)
else: #solo se il codice non ha errori. Qui invece ci sono
    print("Conversione riuscita:", numero)

finally:
    print("Operazione conclusa")
#--------------------------------------------------
try:
    numero = int(input("Inserisci un numero: "))#valueError
    risultato = 100 / numero #ZeroDivisionError
    print(risultato)

except ValueError:
    print("Devi inserire un numero valido!")

except ZeroDivisionError:
    print("Non puoi inserire zero!")

print("Programma terminato.")
#---------------------------------------------------------------------------------

#continua a chiedere finchè non si mette un numero corretto
while True:
    try:
        # Prova a chiedere l'input e a convertirlo in numero
        eta = int(input("Quanti anni hai? "))
        
        # Se la conversione riesce, esce dal ciclo con break
        break 
        
    except ValueError:
        # Questo blocco si attiva SOLO se l'utente ha inserito una parola o simboli
        print("Attenzione! Devi inserire un numero intero, non una parola. Quanti anni hai?")

# Da qui in poi la variabile 'eta' è sicuramente un numero intero
print(f"Hai {eta} anni.")
#-------------------------------------------------------

#--Altro esempio: Cercare un elemento che non esiste
try:
    testo.index("z")
except Exception as e:
    print("Errore: non trovato",e)
else: #Else scatta quando il codice è corretto e non ci sono eccezioni
    print("trovato")
finally: #finally viene eseguito sempre, in ogni caso
    print("vengo eseguito sempre a prescindere se è ok o errore")

# ---------------------------------------------------------------

#superamento limiti lista
lista = [1, 2, 3, 4, 5]

try:
    for i in range(6): #da 0 a 5 -> 6 numeri, uno in più. Oppure len(arr) + 1: 
        print(lista[i])
except IndexError as e:
    print("Hai superato i limiti della lista:", e)
# -------------------------------------------------------------------

#KeyError — chiave inesistente
#Si verifica quando cerchi una chiave che non esiste in un dizionario.
persona = {"nome": "Luca", "eta": 25}

try:
    print(persona["citta"])
except KeyError as e:
    print("Errore:",e,"non disponibile")

#Per evitare questo errore si può utilizzare get()
print(persona.get("citta", "citta Non disponibile"))
#----------------------------------------------------------

#AttributeError — attributo o metodo inesistente
#Si verifica quando si prova ad accedere a un attributo o a un metodo che un oggetto non possiede.
numero = 10

try:
    numero.append(5)
except AttributeError as e:
    print("Errore: ",e)

#--------------------------------------------------------
# possiamo sollevare qualunque tipo di eccezione anche se non c'è un errore
try:
    print("Ciao a tutti")
    raise Exception("Sono una eccezione lanciata a caso")  # sollevo un'eccezione a caso
except Exception as e:
    print("Ho catturato l'eccezione che hai sollevato a caso", e)
# --------------------------------------------------------------------

import math as m
try:
    num = -1 #16
    if num < 0:
        raise ValueError() #solleviamo l'eccezione
    print("la radice quadrata di", num, "è", m.sqrt(num))

except ValueError: #la gestiamo
    print("il numero non può essere negativo")

# ----------------------------------------------------------------------

# Non gestiamo l'errore qui dentro: lo lasciamo propagare a chi ha chiamato la funzione.
def dividi(a,b):
    return a / b #perchè l'errore non è della funzione ma dei valori che gli passiamo
    
    # in alternativa:
    # if b==0:
    #     raise Exception("il secondo numero non può essere negativo!")
    # return a / b 

try:
    ris = dividi(10, 0)
    print(ris)
except Exception as e:
    print("Errore nell'esecuzione della funzione:",e)

# ---------------------------------------------------------------

#Sollevare una eccezione dentro una funzione.  È diverso da gestire l'eccezione dentro la funzione. 
#Qui la stiamo solo sollevando, e la gestirà il chiamante

#Il principio da ricordare è questo: l'eccezione descrive che cosa è andato storto; 
#il codice che la intercetta decide che cosa fare.

def controlla_eta(eta):
    if eta < 0 or eta > 150: #con OR!! Non AND!
        raise ValueError("L'età deve essere compresa tra 0 e 150")


anni = [25, -1, 180, 30,-12]
for eta in anni:
    try:
        controlla_eta(eta)
        print(eta, "è una età valida")
    except ValueError as e:
        print(eta, "età non valida:", e)
    # --si può usare anche l'else al posto del print dopo la chiamata alla funzione controlla_eta(eta)
    # else:
    #     print(eta, "è una età valida")
#------------------------------------------------------------------------------------------

#propagazione eccezione dall'interno verso l'esterno
try:
    print("Blocco try Esterno")
    # l'eccezione si propaga dall'interno verso l'esterno alla ricerca del gestore corretto
    try:
        print("Blocco try interno")
        raise Exception("Eccezione sollevata dal blocco interno")
    except ZeroDivisionError: #non gestisce l'eccezione interna
        print("NON sto gestendo l'eccezione del try interno")
    finally:
        print("finally del try interno")
    print("non vengo mai eseguito")  # non viene eseguito perché si va subito all'except esterno
except Exception as e:
    print("gestisco l'eccezione del blocco interno che si è propagata al blocco esterno", e)
finally:
    print("finally blocco esterno")
# ------------------------------------------------------------------------
#Esempio riassuntivo:
#chiede all'utente la posizione e il valore di un elemento nella lista

# Creazione di una lista di 5 elementi inizializzati a 0
vettore = [0] * 5

try:
    # Chiediamo l'indice all'utente
    risposta_indice = input("Inserisci la posizione in cui vuoi inserire un valore (0-4): ")
    # La conversione in int() può sollevare un'eccezione ValueError
    if int(risposta_indice) >= len(vettore):
        raise IndexError
    index = int(risposta_indice)  

    # Chiediamo il valore all'utente
    risposta_valore = input(f"Inserisci un valore da inserire in posizione {index}: ")
    # Anche qui può essere sollevata un'eccezione ValueError
    value = int(risposta_valore)

    # Tentativo di inserimento nell'indice specificato
    # Se l'indice non esiste, Python solleva un IndexError
    vettore[index] = value  

    print("Valore inserito correttamente!")
    print(f"Stato attuale del vettore: {vettore}")

except ValueError:
    # Sostituisce l'InputMismatchException di Java.
    # Si attiva se l'utente inserisce una stringa non convertibile in intero.
    print("Errore: Devi inserire cifre numeriche intere.")

except IndexError:
    # Sostituisce l'ArrayIndexOutOfBoundsException di Java.
    # Si attiva se l'indice inserito è fuori dall'intervallo della lista.
    print("Errore: l'indice deve essere compreso tra 0 e 4.")

finally:
    # Questo blocco viene eseguito SEMPRE, sia in caso di successo che di errore.
    # In Python non abbiamo bisogno di chiudere uno "Scanner" per l'input da tastiera,
    # ma usiamo il blocco per mostrare il completamento dell'operazione.
    print("Esecuzione del programma terminata (blocco 'finally').")
#----------------------------------------------------------------------------------------------------


#-------- ECCEZIONI PERSONALIZZATE:--------------

class CaramelleFinite(Exception):
    """Eccezione sollevata quando le caramelle sono esaurite."""
    # NON TRATTARE ANCORA PERCHé NON ABBIAMO ANCORA FATTO LE CLASSI
    # def __init__(self, messaggio=None):
    #     if messaggio is None:
    #         print("Altro messaggio alternativo!")
    #     else:
    #         super().__init__(messaggio)
    #I print singoli dentro la classe non vengono stampati, ma devono stare dentro una funzione 
    pass # oppure #None



class QuantitaNegativa(Exception):
    """Eccezione sollevata in caso di quantità negativa"""

#---


num_caramelle = 10
quante = 0
print("Ci sono 10 caramelle")

while num_caramelle > 0:
    print("Quante ne vuoi comprare?")
    try:    
        quante = int(input())
        
        if quante<0:
            raise QuantitaNegativa("Il numero deve essere maggiore di zero")

        num_caramelle -= quante

        if num_caramelle <= 0:
            raise CaramelleFinite("Misurati la glicemia")
        print("ne rimangono", num_caramelle)

    except QuantitaNegativa as e:
        print("Quantita errata!", e)
    except CaramelleFinite as e:
        print("Hai mangiato tutte le caramelle!", e)
    except ValueError as e:
        print("Devi inserire un numero, non una lettera")
    except Exception as e:
        print("Errore altro",e)


#-----------------------------------------------------
#Altro esempio con la funzione:

class EtaInvalida(Exception):
    """Classe per controllare l'età"""
    # def __init__(self, messaggio=None):
        # if messaggio is None:
            # print("Età non valida")
        # else:
            # super().__init__(messaggio)

def controlla_eta(eta):
    if eta < 0 or eta > 150:
        raise EtaInvalida("L'età deve essere compresa tra 0 e 150")


anni = [25, -1, 180, 30]
for eta in anni:
    try:
        controlla_eta(eta)
        print(eta, "età valida")
    except EtaInvalida as e:
        print(eta, "età non valida:", e)
#-------------------------------------------------------------------------------------------


class PasswordDebole(Exception):
    pass


#--Funzione---
#  caratteri,una maiuscola, una minuscola, un numero e un simbolo.
def controlla_password(password):
    if (len(password) < 8 
        or not any(c.isupper() for c in password) #Almeno 1 carattere è una maiuscolo
        or not any(c.islower() for c in password) #Almeno 1 carattere è una minuscolo
        or not any(c.isdigit() for c in password) #Almeno 1 carattere è un numero
        or not any(not c.isalnum() for c in password)): #Almeno 1 carattere NON è una lettera o numero ma SPAZIO O SIMBOLI !#@
            
        raise PasswordDebole(
            "Password non sicura! Usa almeno 8 caratteri, "
            "una maiuscola, una minuscola, un numero "
            "e un simbolo."
        )

    print("Password accettata!")


#----Test--
try:
    controlla_password("Ciao123!")

except PasswordDebole as e:
    print(e)

# -------------------------------------------------------------
#Il principio da ricordare è questo: l'eccezione descrive che cosa è andato storto; 
#il codice che la intercetta decide che cosa fare.
#-------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------
# ESERCIZIO: Simulazione portamonete
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
    disponibilita += quanto


def spendi(quanto):
    global disponibilita
    if disponibilita < quanto:
        raise FondiInsufficientiException("Non hai tutti questi soldi!, ma solo " + str(disponibilita))
    disponibilita -= quanto
    print("Hai speso " + str(quanto) + " euro. Saldo attuale: " + str(disponibilita))

#------Test----
disponibilita = 10
aggiungi(10)
print("hai", disponibilita, "euro")

try:
    quanto_spendere = int(input("quanto vuoi spendere? "))
    spendi(quanto_spendere)
    print("ne rimangono", disponibilita)
except ValueError:
    print("non è un numero")
except FondiInsufficientiException as e:
    print("Errore:", e)

print("-" * 50)


#----------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#-- ESEMPIO DA FARE DOPO AVER TRATTATO LE CLASSI:
class NumeroTroppoGrande(Exception):
    def __init__(self, numero, limite):
        self.numero = numero
        self.limite = limite

        super().__init__(f"Il numero {numero} supera il limite di {limite}!")

    def eccesso(self):
        return self.numero - self.limite

    def e_grave(self):
        return self.eccesso() >= 50

#--Funzione--
def verifica_limite(numero):
    limite_massimo = 100
    if numero > limite_massimo:
        raise NumeroTroppoGrande(numero, 100)
    print(f"Il numero {numero} è accettabile.")

#--test--
try:
    verifica_limite(250)
except NumeroTroppoGrande as e:
    print(e)
    print("Eccesso:", e.eccesso())
    print("Errore grave?", e.e_grave())