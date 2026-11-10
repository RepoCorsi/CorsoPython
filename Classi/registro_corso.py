from studente import Studente


class RegistroCorso:
    """
    Rappresenta il registro di un corso.
    Gestisce una collezione di studenti e le operazioni di ricerca.
    """

    def __init__(self, nome_corso):
        self.nome_corso = nome_corso
        # NOTA DIDATTICA:
        # In Java useremmo List<Studente> studenti = new ArrayList<>();
        # In Python le liste sono dinamiche e pronte all'uso.
        self._studenti = []

    def iscrivi_studente(self, studente):
        self._studenti.append(studente)

    def numero_iscritti(self):
        return len(self._studenti)

    # NOTA DIDATTICA (Regola 10):
    # In Java potremmo fare l'Overloading del metodo cerca():
    #   - public Studente cerca(String cognome)
    #   - public Studente cerca(int matricola)
    #
    # In Python NON esiste il metodo Overloading basato sui tipi dei parametri.
    # Si risolve usando parametri opzionali impostati a None o metodi separati ed espliciti.
    def cerca_studente(self, cognome=None, matricola=None):
        """Cerca uno studente per cognome o per matricola."""
        for s in self._studenti:
            if cognome and s.get_cognome().lower() == cognome.lower():
                return s
            if matricola and s.get_matricola() == matricola:
                return s
        return None

    def mostra_elenco(self):
        print(f"--- Elenco Iscritti: {self.nome_corso} ---")
        for s in self._studenti:
            print(f"- {s.scheda_personale()}")


# Esecuzione autonoma del file per test
if __name__ == "__main__":
    print("--- TEST REGISTRO CORSO ---")

    registro = RegistroCorso("Programmazione Python")

    s1 = Studente("Mario", "Rossi", 20, "S001")
    s2 = Studente("Elena", "Bianchi", 22, "S002")

    registro.iscrivi_studente(s1)
    registro.iscrivi_studente(s2)

    registro.mostra_elenco()

    print("\nRicerca per cognome 'Bianchi':")
    trovato = registro.cerca_studente(cognome="Bianchi")
    if trovato:
        print(f"Trovato: {trovato}")

    print("\nRicerca per matricola 'S001':")
    trovato_mat = registro.cerca_studente(matricola="S001")
    if trovato_mat:
        print(f"Trovato: {trovato_mat}")