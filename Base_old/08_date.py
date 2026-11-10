# In Java esistono diverse classi per gestire data e ora: la vecchia
# classe Date (ormai in gran parte deprecata) e le classi più moderne
# LocalDate, LocalTime, LocalDateTime del package java.time.
# In Python la libreria standard offre un unico modulo, "datetime", con le
# classi date, time e datetime che coprono gli stessi tre casi d'uso.

from datetime import datetime

adesso = datetime.now()
print(adesso)  # contiene sia la data che l'ora, come il LocalDateTime di Java

data = adesso.date()
print(data)

ora = adesso.time()
print(ora)

data_con_ora = adesso
print(data_con_ora)

# In Java si usa un DateTimeFormatter con un pattern (dd/MM/yyyy HH:mm:ss...).
# In Python il metodo strftime() fa la stessa cosa, con codici di formato
# leggermente diversi ma con la stessa idea di fondo.
formato = data_con_ora.strftime("%d/%m/%Y %H:%M:%S\nOggi è il %A %d %B %Y")

print(formato)

# stampare la data di oggi col formato Oggi è il 10**10**2024
# sono le ore ora**minuti**secondi** di giovedì
