"""
NOTA DIDATTICA FONDAMENTALE (Regola 10):
In Java creeremmo un'interfaccia:
    public interface Notificabile {
        void inviaNotifica(String messaggio);
    }
e poi le classi farebbero 'implements Notificabile'.

In Python NON esistono le interfacce nel linguaggio base.
Python usa il 'Duck Typing': "Se cammina come un'anatra e starnazza come un'anatra,
allora per noi è un'anatra". 
Basta che oggetti diversi abbiano un metodo con lo stesso nome (.invia_notifica).
"""


class NotificaEmail:
    def __init__(self, indirizzo_email):
        self.indirizzo_email = indirizzo_email

    def invia_notifica(self, messaggio):
        print(f"[EMAIL a {self.indirizzo_email}]: {messaggio}")


class NotificaSMS:
    def __init__(self, numero_telefono):
        self.numero_telefono = numero_telefono

    def invia_notifica(self, messaggio):
        print(f"[SMS a {self.numero_telefono}]: {messaggio}")


class GestoreNotifiche:
    """
    Classe che invia notifiche a una lista di destinatari.
    Non importa di che classe siano i canali, l'importante è che abbiano
    il metodo 'invia_notifica'.
    """

    def __init__(self):
        self._canali = []

    def aggiungi_canale(self, canale):
        self._canali.append(canale)

    def invia_a_tutti(self, messaggio):
        for canale in self._canali:
            # Polimorfismo in azione senza bisogno di interfacce o ereditarietà
            canale.invia_notifica(messaggio)


# Esecuzione autonoma del file per test
if __name__ == "__main__":
    print("--- TEST DUCK TYPING E POLIMORFISMO ---")

    email = NotificaEmail("studenti@corso.it")
    sms = NotificaSMS("+393331234567")

    gestore = GestoreNotifiche()
    gestore.aggiungi_canale(email)
    gestore.aggiungi_canale(sms)

    gestore.invia_a_tutti("La lezione di domani è confermata alle ore 9:00.")