"""
Presentare all'utente un menù di 5 voci con cui l'utente possa fare le seguenti operazioni:

Inserire un nome dentro la lista
Cancellare un nome dalla lista
Cercare un nome dentro la lista (dire se c'è oppure no)
Visualizzare l'elenco di tutti i nomi all'interno della lista
Uscire dal programma.

Il programma deve presentare il menù finché l'utente non sceglie di uscire.
"""

nomi = []

while True:
    print("Seleziona una opzione:")
    print("1 per inserire un nome")
    print("2 per cancellare un nome")
    print("3 per cercare un nome e sapere se esiste nell'elenco")
    print("4 per visualizzare tutti i nomi")
    print("5 per uscire")

    scelta = int(input())
    nome = ""

    # NOTA: Java ha l'istruzione switch per scegliere tra più casi.
    # Python non ha uno switch "storico": la scelta idiomatica per un
    # principiante è una catena di if/elif/else, che qui fa esattamente
    # lo stesso lavoro dello switch originale.
    if scelta == 1:
        # inserisci il nome
        print("inserisci un nome")
        nome = input().upper()
        nomi.append(nome)
        print("nome inserito")
    elif scelta == 2:
        # cancella il nome
        print("che nome vuoi cancellare?")
        nome = input().upper()
        if nome in nomi:  # equivalente di nomi.contains(nome)
            nomi.remove(nome)  # qui .remove() rimuove per VALORE, come voluto
            print("nome eliminato")
        else:
            print("il nome che vuoi cancellare non è nell'elenco")
    elif scelta == 3:
        # cerca il nome
        print("che nome vuoi cercare?")
        nome = input().upper()
        if nome in nomi:
            print("il nome è presente nell'elenco")
        else:
            print("il nome non è presente nell'elenco")
    elif scelta == 4:
        # visualizza tutti i nomi
        if len(nomi) == 0:  # equivalente di nomi.isEmpty()
            print("la lista è vuota")
        else:
            print("ecco tutti i nomi dell'elenco:")
            for persona in nomi:
                print(persona)
    elif scelta == 5:
        # esci
        print("grazie per aver usato il nostro programma")
        break  # esce dal ciclo while (equivalente del "return" usato in Java qui)
    else:
        # scelta non valida
        print("Scelta non valida, Riprova")
