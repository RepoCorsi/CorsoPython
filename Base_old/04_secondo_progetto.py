print("secondo progetto")

# commento: ho scritto questo programma per .......
# In Java il commento su più righe si scrive tra /* e */.
# Python non ha una vera sintassi di commento multi-riga: la convenzione
# è ripetere il simbolo "#" a inizio di ogni riga, oppure (fuori da questo
# contesto didattico) usare una stringa su più righe tra triple virgolette
# come "docstring", che però tecnicamente non è un commento ma una stringa
# che Python valuta e poi ignora.
# questo
# è
# un commento
# su più
# righe

print("seconda linea")
print("terza linea")

# In Java System.out.print() non va a capo, System.out.println() sì.
# In Python la funzione print() aggiunge sempre "a capo" alla fine, a meno
# di passare il parametro end="" per evitarlo.
print("aaaaaaa", end="")
print("bbbbbb")
print("cccc")
