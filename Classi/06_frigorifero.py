# AGGREGAZIONE: QUANDO GLI OGGETTI SONO INDIPENDENTI
# SE ELIMINO IL FRIGO, I CIBI CONTINUANO A RIMANERE PERCHè SONO CREATI FUORI DAL FRIGORIFERO.

class Cibo:
    """
    Rappresenta un singolo alimento.
    """
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Frigorifero:
    """
    Classe principale che contiene la logica dimostrativa.
    """
    def __init__(self,lista_cibi):
        self.lista_cibi = lista_cibi 


    def elenca_cibi(self):
        print("nel frigorifero ci sono i seguenti cibi:")
        for cibo in self.lista_cibi:
            print(cibo)  # Chiama implicitamente __str__()


# ESEGUIAMO
cibo1 = Cibo("pizza")
cibo2 = Cibo("hamburger")
cibo3 = Cibo("hotdog")

lista_cibi=[cibo1,cibo2,cibo3]

# oppure:
#lista_cibi = [Cibo("pizza"), Cibo("hamburger"), Cibo("hotdog")] #creo gli oggetti direttamente nella lista

frigo = Frigorifero(lista_cibi)
frigo.elenca_cibi()

#------------------------------------------

## -- COMPOSIZIONE. I CIBI SONO CREATI DENTRO IL FRIGO, QUINDI SONO LEGATI E SE ELIMINO IL FRIGO, ELIMINO ANCHE I CIBI. 
# NON SONO PIù INDIPENDENTI

class Frigorifero_compo:
    def __init__(self):
        # Il frigo nasce vuoto, gestisce lui la sua lista interna
        self.lista_cibi = [] 

    def aggiungi_cibo(self, nome_cibo):
        # COMPOSIZIONE: L'oggetto Cibo viene istanziato DIRETTAMENTE dentro il Frigorifero
        nuovo_cibo = Cibo(nome_cibo)
        self.lista_cibi.append(nuovo_cibo)

    def elenca_cibi(self):
        print("Nel frigorifero ci sono i seguenti cibi:")
        for cibo in self.lista_cibi:
            print(cibo)


# ESEGUIAMO LA COMPOSIZIONE
frigo = Frigorifero_compo()

# Il mondo esterno non vede e non crea gli oggetti "Cibo", se ne occupa il Frigorifero
frigo.aggiungi_cibo("pizza")
frigo.aggiungi_cibo("hamburger")
frigo.aggiungi_cibo("hotdog")

frigo.elenca_cibi()

# Se facessimo: del frigo
# Anche tutti gli oggetti Cibo creati al suo interno verrebbero eliminati dalla memoria.
