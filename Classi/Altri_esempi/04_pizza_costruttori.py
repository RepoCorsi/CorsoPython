class Pizza:

    #Parametri opzionali
    def __init__(self, farina=None, salsa=None, mozzarella=None, extra=None):
        self.farina = farina  # tipo 00 o integrale
        self.salsa = salsa  # pomodoro o olio, per la focaccia
        self.mozzarella = mozzarella  # normale o di bufala
        self.extra = extra  # funghi, prosciutto, ecc.

    def __str__(self):
        if self.mozzarella is not None:
            return (f"Ecco la tua pizza: farina= {self.farina}, {self.salsa}, mozzarella={self.mozzarella}, extra={self.extra} ")
        else:
            return (f"Ecco la tua pizza/focacia: farina= {self.farina}, {self.salsa}")
    
# ================== PROVA  ==================

print("Che farina vuoi? 00 o integrale?")
farina = input()

print("Scegli la pizza: \n"
    "1 focaccia/pizza rossa \n"
    "2 margherita\n"
    "3 Altro ")

scelta = int(input())

if scelta == 1:
    print("pizza rossa o facaccia?")
    tipologia=input()
    tipo="pomodoro" if tipologia=="rossa" else "olio evo"
    p = Pizza(farina, tipo) #costruttore con 2 parametri
elif scelta == 2:
    print("Mozzarella di bufala o normale?")
    p = Pizza(farina, "pomodoro", input())#costruttore con 3 parametri
else:
    print("Scegli la mozzarella e l'extra")
    p = Pizza(farina, "pomodoro", input(), input()) #costruttore con 4 parametri # funghi e prosciutto

print(p)