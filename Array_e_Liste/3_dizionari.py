# un insieme di elementi identificati da chiave e valore
# le chiavi sono uniche, non ammettono duplicati
# Mantiene l'ordine di INSERIMENTO (non l'ordine alfabetico/numerico).
#Per avere le chiavi ordinate bisogna ordinarle esplicitamente, come vedremo alla fine.

# I Dizionari ({chiave: valore})
# Un dizionario non usa indici numerici (0, 1, 2...) per trovare gli elementi, ma usa delle chiavi personalizzate. Immaginalo come una vera rubrica telefonica: cerchi il nome (chiave) per trovare il numero (valore).
# • Sintassi: Si usano le parentesi graffe {} con le coppie chiave: valore.
# • Regola d'oro: Le chiavi devono essere uniche (non puoi avere due chiavi identiche).
#Esempio pratico:

# Creazione di un dizionario
utente = {
    "nome": "Luca",
    "eta": 28,
    "citta": "Torino"
}

# Accedere a un valore tramite la sua chiave
print(utente["nome"])  # Output: Luca

#print(utente["telefono"]) #se la chiave non c'è da errore,

#allora usare get()
telefono = utente.get("telefono", "Dato non inserito") #se la chiave manca ritorna il messaggio oppure None se non c'è il messaggio
print(telefono)  # Output: Dato non inserito

# Aggiungere o modificare un elemento
utente["telefono"]=3287654321 # Aggiunge una nuova coppia chiave - valore
utente["professione"] = "Sviluppatore"  # Aggiunge una nuova coppia chiave - valore
utente["eta"] = 29   # Modifica il valore esistente

print(utente)

# Rimuovere un elemento
del utente["citta"]

print(utente)

#oppure
# Il metodo .pop() rimuove la chiave e ti restituisce il valore eliminato
professione_eliminata = utente.pop("professione") 
print("Eliminato",professione_eliminata,utente)

#-------------------------------
# Dizionario vuoto
paesi = {}
# in Python si assegna il valore direttamente con le
# parentesi quadre, come per una lista ma con la chiave al posto dell'indice
paesi["USA"] = "Washington"
paesi["Norvegia"] = "Oslo"
paesi["Russia"] = "Mosca"
paesi["Cina"] = "pechino"

# NOTA: per inserire solo se la chiave non esiste si usa il metodo setdefault().
paesi.setdefault("USA", "xxx")  # "USA" esiste già: il valore non cambia
paesi.setdefault("Italia", "Roma")  # "Italia" non c'è: viene inserita

print(paesi)

# tramite la chiave prendo il valore
print(paesi["Russia"])  # Mosca

# cerca la chiave: True se la trova, False se non c'è
print("Inghilterra" in paesi)
# cerca il valore: True se lo trova, False se non c'è
print("pechino" in paesi.values())

# visualizzo solo le chiavi
for chiave in paesi.keys():
    print(chiave)

# visualizzo solo i valori
for valore in paesi.values():
    print(valore)

# stampo chiave e valore
# NOTA: per scorrere un dizionario si usa il metodo .items(), che restituisce
# direttamente le coppie chiave-valore, da usare con un normale for.
for chiave, valore in paesi.items():
    print("chiave", chiave, "valore", valore)

del paesi["USA"] 
print(paesi)


print("creo una lista con le chiavi del dizionario: ")
print(list(paesi)) #in modo predefinito prende le chiavi
print("ordino le chiavi di un dizionario")
print(sorted(paesi))

print("stampa anche l'indice con enumerate:")
for i, v in enumerate(paesi.items()):
    print(i,v)

#in alternativa posso fare:
solo_chiavi = list(paesi.keys())
solo_valori = list(paesi.values())

print(solo_chiavi)
print(solo_valori)

#Ricomporre il dizionario:
dizio_paesi=dict(zip(solo_chiavi,solo_valori))
print(dizio_paesi)

#---------------------------------------
# ---------------------------------------------------------------------------------
montagne = {}

montagne["Everest"] = 8848
montagne["K2"] = 8630
montagne["Nanga Parbat"] = 8200

for nome, altezza in montagne.items():
    print(nome, "è alta:", altezza, "metri")

# -----------------------------------------------------------------
# Una chiave può avere più valori

autori_libri = {
    "Dan brown": ["Angeli e demoni", "Il Codice da Vinci", "Il simbolo perduto"],
    "Italo Calvino": ["Il barone rampante", "Le città invisibili"]
}
print (autori_libri)

autori_libri["Italo Calvino"].append("Marcovaldo")
print(autori_libri["Italo Calvino"])
# Output: ['Il barone rampante', 'Le città invisibili', 'Marcovaldo']

print(autori_libri)

#--Altro esempio:
autori = {}

# libri degli autori
libri_autore1 = ["l1", "l2", "l3"]  # libri dell'autore 1
libri_autore2 = ["l4", "l5", "l6"]  # libri dell'autore 2
libri_autore3 = ["l7", "l8", "l9"]  # libri dell'autore 3

#creo un autore e gli assegno una lista di valori
autori["autore1"] = libri_autore1 
autori["autore2"] = libri_autore2
autori["autore3"] = libri_autore3

for autore in autori.keys():
    print("Autore:", autore, "Libri", autori[autore])

#------Formattato:
for autore, libri in autori.items():
    print("Autore:", autore,"\nlibri:",end=" ")
    for libro in libri:
        print(libro,end=" ")
    print()
    
#---- Oppure senza il secondo ciclo for usando join
for autore, libri in autori.items():
    print("Autore:", autore)
    print("libri:", " ".join(libri))
#Il metodo .join() funziona solo se tutti gli elementi della lista sono stringhe.
#-----------------------------------------------------------------------------------------------------

# LISTE DI DIZIONARI:
# è una struttura dati molto comune, utile per rappresentare tabelle o insiemi di oggetti
# (ad esempio una lista di utenti, di prodotti o di studenti).
studenti = [
    {"nome": "Anna", "eta": 20, "voto": 28},
    {"nome": "Marco", "eta": 22, "voto": 25},
    {"nome": "Elena", "eta": 21, "voto": 30}
]

# Accedi al primo studente
print(studenti[0])  # Output: {'nome': 'Anna', 'eta': 20, 'voto': 28}

# Accedi al nome del secondo studente
print(studenti[1]["nome"])   # Output: Marco

#Iterare (scorrere) la lista con un ciclo for
for studente in studenti:
    print(f"{studente['nome']} ha preso {studente['voto']} all'esame.")

# Output:
# Anna ha preso 28 all'esame.
# Marco ha preso 25 all'esame.
# Elena ha preso 30 all'esame.

#inserire un nuovo studente:
nuovo_studente = {"nome": "Luca", "eta": 23, "voto": 24}
studenti.append(nuovo_studente)

print(studenti)

#eliminare un elemento:
# Elimina il primo elemento della lista (Anna)
del studenti[0]
print(studenti)

#Elimina e ritorna l'elemento in una variabile:
# Rimuove il secondo elemento (Elena) e lo salva
studente_rimosso = studenti.pop(1)
print(studente_rimosso) 
# Output: {'nome': 'Elena', 'eta': 21, 'voto': 30}

#----------------------------------------
#dizionario di dizionari --> per semplicità meglio non trattarlo:

# studenti_dict = {
#     "Anna": {"eta": 20, "voto": 28},
#     "Marco": {"eta": 22, "voto": 25}
# }

# del studenti_dict["Marco"]

# print(studenti_dict)
# # Output: {'Anna': {'eta': 20, 'voto': 28}}


# -----------------------------------------------------------------------------------

frutti = {}
frutti["mela"] = 1.50
frutti["uva"] = 2.00
frutti["banana"] = 3.00
frutti["kiwi"] = 2.50

# come spiegato in cima al file, un dict normale non ordina le chiavi da
# solo: bisogna ordinare esplicitamente con sorted
frutti_ordinati = dict(sorted(frutti.items()))
print(frutti_ordinati)
#-------------------------------------------------

#SCHEMA RIASSUNTIVO COLLECTIONS:
# Tabella riassuntiva di tutte le collezioni Python
# Collezione  Sintassi	Ordinata?	Permette duplicati?	Modificabile?	Caso d'uso ideale
# Lista	      [a, b, c]	   Sì		Sì					Sì				Sequenze di elementi modificabili (es. carrello spesa)
# Tupla	      (a, b, c)	   Sì		Sì					No				Dati protetti che non devono cambiare (es. coordinate GPS)
# Set	      {a, b, c}	   No		No					Sì				Eliminare duplicati e fare operazioni di insiemistica
# Dizionario  {"k": "v"}   Sì 		No (chiavi uniche)	Sì				Dati complessi con chiavi e valori (es. profilo utente)

#------------------------------

#Trattare prima le list comprehension!
#Dictionary comprehension:
# Hai una lista di prodotti e prezzi e vuoi creare un dizionario in cui la chiave è il nome del prodotto e il valore è il prezzo 

#associare 2 liste
prodotti = ["mela", "banana", "kiwi", "pitecantropo"]
prezzi = [1,2,3,4]

dizionario=dict(zip(prodotti, prezzi))
print (dizionario)
#Se una lista è più corta dell'altra, zip() si ferma automaticamente all'ultimo elemento della lista più corta senza mandare il programma in crash

# Uniamo e filtriamo in un colpo solo!
prezzoMag2 = {prodotto: prezzo for prodotto, prezzo in zip(prodotti, prezzi) if  prezzo> 2}

print(prezzoMag2)  # Output: {'kiwi': 3, 'pitecantropo': 4}

#-----------------------------------------------------------
