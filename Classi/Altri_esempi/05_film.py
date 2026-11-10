class Film:
    def __init__(self, titolo, genere, anno, durata, regista, vm):
        # In Python, gli attributi sono pubblici per default.
        # Evitiamo l'uso di getter e setter inutili, accedendo direttamente alle variabili.
        self.titolo = titolo
        self.genere = genere
        self.anno = anno
        self.durata = durata
        self.regista = regista
        self.vm = vm  # Booleano: True se vietato ai minori, False altrimenti
        
        self.attori = [] #lista attori

    def __str__(self):
        attori_str= ", ".join(self.attori)
        
        return f"Film{{titolo={self.titolo}, genere={self.genere}, anno={self.anno}, durata={self.durata}, autore={self.regista}\n Attori: {attori_str}}}"

    def __eq__(self, other):
        # Questo metodo speciale corrisponde all'equals() di Java.
        # Definisce come confrontare due oggetti con l'operatore '=='.
        if isinstance(other, Film):
            # Nel codice originale l'uguaglianza è basata solo sul regista
            return self.regista == other.regista
        return False


# Esecuzione:

# Creiamo il primo film
film1 = Film("Inception", "Fantascienza", 2010, 148.0, "Christopher Nolan", False)

# Popoliamo la lista degli attori usando gli indici (come in Java)
film1.attori.append("Leonardo DiCaprio") 
film1.attori.append("Joseph Gordon-Levitt")
film1.attori.append("Elliot Page")

# Stampiamo il film
print("Dettagli Film 1:")
print(film1)
print("-" * 40)

# Creiamo un secondo film con lo stesso regista
film2 = Film("Interstellar", "Fantascienza", 2014, 169.0, "Christopher Nolan", False)

# Popoliamo la lista degli attori usando gli indici (come in Java)
film2.attori.append("Leonardo DiCaprio") 
film2.attori.append("aaa")
film2.attori.append("bbb")

print("Dettagli Film 2:")
print(film2)
print("-" * 40)

# Testiamo l'uguaglianza (basata sul regista, come da logica del codice Java)
if film1 == film2:
    print("I due film sono 'uguali' perché hanno lo stesso regista.")
else:
    print("I due film hanno registi diversi.")