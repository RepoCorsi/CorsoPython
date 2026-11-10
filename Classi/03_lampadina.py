class Lampadina:

    def __init__(self, stato):
        self._stato = stato
        self._n_accensioni = 0

    def is_rotta(self):
        return self._n_accensioni >= 6

    def stato(self):
        if self.is_rotta():
            return "Lampadina rotta!"
        else:
            return "Lampadina accesa" if self._stato else "Lampadina spenta"

    def click(self):
        self._stato = not self._stato
        self._n_accensioni += 1
        print(self.stato())


# ================== PROVA (equivalente del "main" di Java) ==================

l = Lampadina(True)
for i in range(10):
    l.click()
