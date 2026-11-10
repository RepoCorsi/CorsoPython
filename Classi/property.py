#----------------------------------------------------------------------
# # PROPERTY 

# #esempio classico:
# class Studente:
#     def __init__(self, valore):
#         self.voto = valore

#     def get_voto(self):
#         return self._voto

#     def set_voto(self, nuovo_voto):
#         if nuovo_voto>=0:
#             self._voto = nuovo_voto
#         else:
#             raise ValueError("Il voto deve essere >=0")


# studente = Studente(8)

# print(studente.get_voto())  # 8

# studente.set_voto(9)
# print(studente.get_voto())  # 9

# #studente.set_voto(15)      # Errore!

# #-------
# #Esempio con @property: -> Per attivare la property, il NOME usato dopo self. nell'assegnazione DEVE coincidere con il NOME della property.
#la property fa sì che un attributo si comporti come un'interfaccia che, quando viene letto o modificato, esegue automaticamente un metodo.
#La property intercetta le operazioni di lettura e assegnazione che usano quel nome, chiamando i metodi della property

# class Studente:
#     def __init__(self, valore):
#         self.voto = valore #l'attributo non viene creato, perché l'assegnazione viene intercettata dalla property fin dall'inizio.

#     @property
#     def voto(self):
#         return self._voto

#     @voto.setter
#     def voto(self, nuovo_voto):
#         if nuovo_voto >=0:
#             self._voto= nuovo_voto #viene creato l'attributo _voto. 
#         else:
#             raise ValueError("Il voto deve essere >=0")

# studente = Studente(8)  # Chiama il costruttore che esegue self.voto = valore e richiama il setter, che salva 8 in self._voto. Viene creato _voto che è il vero attributo dell'oggetto. 

# studente.voto = 9 
# print(studente.voto)  # 9 

# # studente.voto = -9 
# # print(studente.voto)  #errore

# print(studente.__dict__) # dopo la creazione dell'oggetto, voto non compare nel __dict__, mentre _voto sì.

# se non conosco come è fatta la classe, non posso sapere se con studente.voto sto assegnando direttamente il valore ad un attributo, oppure sto chiamando un metodo!!

# print(studente.__dict__) #solo atributi
# print(dir(studente)) #attributi e metodi dell'oggetto
# print(studente.__class__) #a quale classe appartiene l'oggetto

#-----------------------

# PROPERTY

class ContoBancario:
    def __init__(self, titolare, saldo_iniziale):
        self.titolare = titolare
        self.saldo = saldo_iniziale  # Attributo privato

    # GETTER: Permette di leggere il saldo come se fosse un normale attributo
    @property
    def saldo(self):
        return self._saldo

    # SETTER: Permette di modificare il saldo inserendo dei controlli di logica
    @saldo.setter
    def saldo(self, valore):
        if valore >= 0:
            self._saldo = valore
        else:
            raise ValueError("Errore: Il saldo non può essere negativo!")            

# Utilizzo
conto = ContoBancario("Alice", 1000)

# Tentiamo di accedere al saldo tramite la property (Getter)
print(conto.saldo)  # Output: 1000

# Tentiamo di modificarlo tramite il Setter
conto.saldo = 1500  # Modifica valida
#conto.saldo = -50   # Output: Errore: Il saldo non può essere negativo!
print(conto.saldo)  # Output: 1500

#-------------------------------------------------------------------------

class Rettangolo:
    def __init__(self, width, height):
        self.width = width #assegno direttamente il valore all'attributo senza passare dalla property
        self.height = height #assegno direttamente il valore all'attributo senza passare dalla property

    @property #getter per leggere il valore
    def width(self):
        return f"{self._width:.1f}cm"

    @property #getter per leggere il valore
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter #setter per imnpostare il valore
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    # @width.deleter
    # def width(self):
    #     del self._width
    #     print("Width has been deleted")

    # @height.deleter
    # def height(self):
    #     del self._height
    #     print("Height has been deleted")

rettangolo = Rettangolo(3, 4) #assegna direttamente il valore all'attributo senza passare dalla property
print(rettangolo.width)
print(rettangolo.height)
print(rettangolo._width)
print(rettangolo._height)
rettangolo.width=10
rettangolo.height=2
print(rettangolo.width,rettangolo.height)
#------------------------------------------------------------------------------


