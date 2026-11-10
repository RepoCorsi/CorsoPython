# In Java, per leggere l'input da tastiera, serve creare un oggetto Scanner
# collegato a System.in e poi chiamare i suoi metodi (nextLine(), nextInt()...).
# In Python non serve creare nessun oggetto: la funzione predefinita input()
# legge sempre una riga di testo (una stringa) da tastiera.

print("inserisci il nome")

nome = input()

print("hai scritto", nome)

print("quanti anni hai?")

# NOTA: input() restituisce SEMPRE una stringa, anche se l'utente digita un
# numero. In Java, Scanner ha metodi diversi per leggere direttamente un
# intero (nextInt()) o una riga di testo (nextLine()). In Python bisogna
# sempre convertire esplicitamente il testo letto nel tipo che serve, con
# int() o float().
eta = int(input())

print("la tua età è", eta)

print("colore preferito")

colore = input()

print("il colore è", colore)

# ---------------------------------------------
