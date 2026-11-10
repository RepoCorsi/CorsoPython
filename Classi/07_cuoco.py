class Cuoco:    
    def cucina(self, piatto):
        print("il cuoco cucina",piatto)


class Cameriere:

    #design pattern chiamato DEPENDENCY INJECTION (Iniezione delle Dipendenze).
    #il cameriere può gestire qualsiasi cuoco, non sono legati 
    def __init__(self, nome, cuoco):
        self.nome=nome
        self.cuoco=cuoco

    #principio Open/Closed (aperto alle estensioni(posso passare un camio, estensione di macchina), ma chiuso alle modifiche).
    def prendi_ordini(self, piatto):
        print(f"il cameriere {self.nome} ha preso questo ordine: {piatto}")
        self.cuoco.cucina(piatto)


cracco = Cuoco()
ambrogio = Cameriere("Ambrogio", cracco) #iniettiamo il cuoco
ambrogio.prendi_ordini("pasta al pesto")
