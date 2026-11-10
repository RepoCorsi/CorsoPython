"""
Gestione di un elenco di partecipanti a un evento.

Creare un programma che consenta di aggiungere, rimuovere, visualizzare e
verificare se un determinato partecipante è presente in un elenco
utilizzando un insieme (set).

    Implementa il seguente menu:
        Opzione 1: Aggiungi partecipante
            Richiedi all'utente di inserire il nome del partecipante da aggiungere all'evento.
        Opzione 2: Rimuovi partecipante
            Richiedi all'utente di inserire il nome del partecipante da rimuovere dall'evento.
        Opzione 3: Visualizza partecipanti
            Stampa tutti i nomi dei partecipanti presenti nel set.
        Opzione 4: Verifica partecipante
            Richiedi all'utente di inserire il nome del partecipante da verificare.
        Opzione 5: Esci
            Termina il programma.

Implementa un ciclo che richieda all'utente di selezionare un'opzione dal
menu finché non sceglie Esci.
"""

partecipanti = set()

while True:
    print("Seleziona una opzione:\n1 aggiungi\n2 rimuovi\n3 visualizza\n4 verifica\n5 esci")
    scelta = int(input())
    nome = ""

    if scelta == 1:
        # aggiungi
        print("inserisci un partecipante")
        nome = input().upper()
        # NOTA: set.add() in Python non restituisce nulla: bisogna controllare la presenza PRIMA
        if nome not in partecipanti:
            partecipanti.add(nome)
            print("Aggiunto con successo")
        else:
            print("La persona che vuoi inserire esiste già")
    elif scelta == 2:
        print("inserisci il partecipante da rimuovere")
        nome = input().upper()
        # NOTA: anche set.remove() in Python non restituisce nulla; se l'elemento non esiste, remove() genera
        # addirittura un errore. Il metodo discard(), invece, rimuove l'elemento se c'è e non fa nulla se non c'è: 
        #per questo motivo qui controlliamo prima con "in", come sopra.
        if nome in partecipanti:
            partecipanti.remove(nome)
            print("persona rimossa con successo")
        else:
            print("la persona che vuoi rimuovere non è presente nell'elenco")
    elif scelta == 3:
        # visualizza
        if len(partecipanti) == 0:
            print("non c'è nessun partecipante all'evento")
        else:
            print("elenco partecipanti")
            for persona in partecipanti:
                print(persona, " ")
    elif scelta == 4:
        # verifica
        print("inserisci il nome da verificare se esiste")
        nome = input().upper()
        if nome in partecipanti:
            print("la persona è presente nell'elenco")
        else:
            print("non è presente")
    elif scelta == 5:
        # esci
        print("ciao e grazie")
        break
