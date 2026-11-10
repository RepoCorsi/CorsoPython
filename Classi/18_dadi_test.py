import random


class Giocatore:

    def __init__(self, nome):
        self.nome = nome
        self.punteggio = 30
        # NOTA: come già visto più volte, il modulo random di Python si
        # usa direttamente: non serve creare un oggetto Random come in Java.

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_punteggio(self):
        return self.punteggio

    def set_punteggio(self, punteggio):
        self.punteggio -= punteggio

    def perso(self):
        return self.punteggio <= 0

    def lancia(self):
        return random.randint(1, 6)

    def __str__(self):
        return self.nome + " punteggio=" + str(self.punteggio)


# ================== PROVA (equivalente del "main" di Java) ==================

giocatore1 = Giocatore("Fabio")
giocatore2 = Giocatore("Gino")
vincitore = ""

print(giocatore1.get_punteggio())
print(giocatore2.get_punteggio())

# finché nessuno ha perso: appena uno perde, "and" diventa falso e il ciclo si ferma
while (not giocatore1.perso()) and (not giocatore2.perso()):

    lancio_g1 = giocatore1.lancia()
    lancio_g2 = giocatore2.lancia()

    print("Fabio", lancio_g1, "Gino", lancio_g2)

    if lancio_g1 > lancio_g2:
        giocatore2.set_punteggio(lancio_g1)  # sottraiamo il punteggio più alto a chi ha perso
        print("Gino perde", lancio_g1, "punti. Ne rimangono", giocatore2.get_punteggio())
        vincitore = giocatore1.get_nome()
    elif lancio_g2 > lancio_g1:
        giocatore1.set_punteggio(lancio_g2)
        print("Fabio perde", lancio_g2, "punti. Ne rimangono", giocatore1.get_punteggio())
        vincitore = giocatore2.get_nome()
    else:
        print("pareggio")

print(giocatore1, giocatore2, "vince:", vincitore)
