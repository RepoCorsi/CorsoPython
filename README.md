# Da Java a Python — guida di riferimento per l'insegnante

Questo documento raccoglie in un unico posto tutti i concetti Java che, nel
trasporre il materiale di [JAITA131](https://github.com/RepoCorsi/JAITA131),
**non hanno un equivalente diretto in Python**, o che richiedono un
equivalente concettualmente diverso. È pensato come riferimento rapido da
tenere sott'occhio durante le lezioni, non come sostituto dei commenti
`NOTA` presenti nei singoli file (che restano il riferimento più
dettagliato, applicato caso per caso).

---

## 1. Tipi di dato e variabili

| Java | Python | Nota |
|---|---|---|
| `byte`, `short`, `int`, `long` | un solo `int` | Python ha un unico tipo intero, senza limite di dimensione |
| `float`, `double` | un solo `float` | corrisponde concettualmente al `double` |
| `char` | stringa di 1 carattere | niente tipo carattere dedicato; niente `++` su un carattere: si passa da `ord()`/`chr()` |
| dichiarazione esplicita del tipo (`int x`) | nessuna dichiarazione | il tipo si deduce dal valore assegnato |
| `var` (type inference, Java 10+) | non serve | ogni variabile Python può comunque cambiare tipo in seguito, cosa che `var` in Java non permette |
| cast espliciti/impliciti tra tipi numerici | `int()`, `float()`, `str()` | la conversione va quasi sempre fatta a mano, anche perché i tipi numerici sono di meno |
| `final` (costanti) | nessun vincolo reale | per convenzione si usa un nome tutto MAIUSCOLO, ma nulla vieta di riassegnarlo |
| `++x` / `x++` (pre/post incremento) | non esistono | si usa `x += 1` (o `x = x + 1`), sempre come istruzione a parte |
| operatori logici `&&`, `\|\|` | `and`, `or` | stessa precedenza, parole invece di simboli |
| `Math.round()` | `round()` | Python usa l'arrotondamento "bancario" sulle metà esatte (`round(2.5)` vale 2, non 3) |
| `DecimalFormat` | `format(numero, ".2f")` | formattazione con un numero fisso di decimali |
| classe `Random` (`new Random()`) | modulo `random` | le funzioni (`random.randint(...)`) si chiamano direttamente, senza creare un oggetto |

## 2. Cicli e controllo di flusso

| Java | Python | Nota |
|---|---|---|
| `for` con 3 parti (init; cond; incremento) | `for x in range(...)` | il `for` di Python è sempre un for-each; `range()` genera la sequenza di numeri |
| `for` "destrutturato" (senza init o incremento) | `while` | Python non permette un `for` a pezzi variabili |
| più variabili di ciclo nello stesso `for` | `while` con più contatori | il `for` di Python gestisce una sola variabile per volta |
| `do-while` | non esiste | idioma più vicino: `while True: ... ; if condizione: break` (corpo eseguito almeno una volta) |
| `for(;;)` (for infinito) | `while True:` | nessuna sintassi di `for` infinito |
| `switch` (classico o con `->`, Java 14+) | `if / elif / else` | Python non ha uno switch; per più valori nello stesso caso si usa `valore in (a, b, c)` |
| operatore ternario `cond ? a : b` | `a if cond else b` | stesso concetto, ordine diverso |
| `instanceof` | `isinstance(oggetto, Classe)` | |

## 3. Funzioni e metodi

| Java | Python | Nota |
|---|---|---|
| overload (più metodi con lo stesso nome, parametri diversi) | **non esiste** | una sola funzione già accetta argomenti di tipo diverso (tipizzazione dinamica); per un numero variabile di parametri si usano valori di default o `*args` |
| varargs (`int... numeri`) | `*args` | dentro la funzione diventa una tupla anziché un array |
| tipo di ritorno dichiarato (incluso `void`) | nessuna dichiarazione | una funzione senza `return` restituisce `None` |
| variabili `static` locali a un metodo | variabile di modulo + `global` dentro la funzione | fuori da una classe è il modo più diretto di "ricordare" un valore tra una chiamata e l'altra |

## 4. Liste, Collections e Map

| Java | Python | Nota |
|---|---|---|
| array (dimensione fissa) **e** `ArrayList` (dimensione dinamica) | un solo tipo: `list` | Python non distingue: le liste sono già dinamiche e possono contenere tipi diversi |
| `array.length` / `arrayList.size()` | `len(...)` | stessa funzione per liste, stringhe, ecc. |
| `ArrayList.remove(int)` vs `remove(Object)` | **attenzione**: `.remove(valore)` rimuove sempre per VALORE | per rimuovere per indice: `.pop(indice)` o `del lista[indice]` |
| wrapper class (`Integer`, `Character`, `Boolean`...) | non servono | in Python tutto è già un oggetto, nessun involucro necessario per int/char/bool in una lista |
| `HashSet` / `TreeSet` | un solo tipo: `set` | nessun "TreeSet" nella libreria standard: per un insieme ordinato si usa `sorted(insieme)` al bisogno |
| `Set.add()` restituisce `boolean` | `set.add()` non restituisce nulla | va controllata la presenza con `in` *prima* di aggiungere/rimuovere |
| `HashMap` / `TreeMap` | un solo tipo: `dict` | dal 3.7 un `dict` mantiene l'ordine di INSERIMENTO (non quello alfabetico/numerico); per un ordine simile a TreeMap: `dict(sorted(d.items()))` |
| `map.put()`, `putIfAbsent()`, `remove()` | `d[chiave] = valore`, `d.setdefault(...)`, `del d[chiave]` | |
| `forEach(x -> ...)` su liste/mappe | `for x in ...:` | le collezioni Python non hanno un metodo `forEach` |
| `ArrayDeque` (coda FIFO) | `collections.deque` | `append()`/`popleft()` al posto di `add()`/`poll()`; niente `peek()`, si legge `coda[0]` |
| `Stack` (pila LIFO) | una `list` normale | `append()`/`pop()` lavorano già sull'ultimo elemento |

## 5. Eccezioni

| Java | Python | Nota |
|---|---|---|
| `try / catch / finally` | `try / except / finally` | `finally` esiste identico in Python |
| eccezioni **checked** vs **unchecked** | **non esiste distinzione** | tutte le eccezioni Python si comportano come le "unchecked" di Java: nessun controllo a compile-time |
| `throw` | `raise` | |
| multi-catch `catch (A \| B \| C e)` | `except (A, B, C) as e:` | |
| `InputMismatchException` | `ValueError` | tipicamente da `int(input())` su testo non numerico |
| `ArrayIndexOutOfBoundsException` | `IndexError` | |
| `ArithmeticException` (divisione per 0) | `ZeroDivisionError` | |
| `NullPointerException` | **nessun equivalente diretto** | l'errore più vicino su un valore `None` è `AttributeError` o `TypeError` |
| classe eccezione personalizzata (`extends Exception`) | `class MiaEccezione(Exception):` | stesso meccanismo in entrambi i linguaggi |

## 6. Generics

| Java | Python | Nota |
|---|---|---|
| `<T>` su classi e metodi | **non esiste, e non serve** | Java usa i generics per dare sicurezza di tipo a un linguaggio staticamente tipizzato; Python è dinamico e accetta già qualunque tipo, senza bisogno di dichiararlo |
| `Bottiglia<Acqua>`, `Cesto<T extends Frutta>` | classe "normale" | nessun parametro di tipo da scrivere: la classe funziona già con qualsiasi contenuto |
| getter/setter "necessari" per l'incapsulamento nei generics | accesso diretto agli attributi | se in futuro serve un controllo sull'accesso, si usano le `property` (argomento più avanzato) |

## 7. Programmazione a oggetti

### Visibilità e incapsulamento

| Java | Python | Nota |
|---|---|---|
| `public` / *(default, package)* / `private` / `protected` | **un solo livello per convenzione** | `_attributo` (underscore iniziale) segnala "uso interno", ma è solo una convenzione: Python non impedisce l'accesso dall'esterno, né distingue "privato" da "protetto" |

### Costruttori, override, uguaglianza

| Java | Python | Nota |
|---|---|---|
| overload dei costruttori (più `NomeClasse(...)`) | **un solo `__init__`** | con parametri opzionali (`=None`) si copre lo stesso ventaglio di casi |
| `@Override` | nessuna annotazione | si ridefinisce il metodo con lo stesso nome, Python capisce da solo |
| `toString()` | `__str__` | usato da `print()` |
| un oggetto stampato **dentro una lista** usa comunque `toString()` | serve **anche** `__repr__` | Python usa `__repr__`, non `__str__`, per gli oggetti dentro una collezione; il modo più semplice è `__repr__ = __str__` |
| `equals(Object o)` | `__eq__(self, o)` | comodità in più: una volta definito, l'operatore `==` lo richiama da solo (in Java `==` confronta sempre i riferimenti) |
| campo `static` (contatore condiviso) | attributo scritto nel corpo della classe (fuori da `__init__`) | è condiviso da tutte le istanze, proprio come uno `static` Java |

### Ereditarietà

| Java | Python | Nota |
|---|---|---|
| `extends` | `class Figlia(Genitore):` | |
| `super(...)` nel costruttore (deve essere la prima istruzione) | `super().__init__(...)` | in Python è buona norma, ma non è imposto dal linguaggio |
| `super.metodo()` | `super().metodo()` | |
| singola ereditarietà per le classi | **Python supporta l'ereditarietà multipla nativamente** | `class C(A, B):` è sintassi normale, non richiede nulla di speciale |

### Classi astratte

| Java | Python | Nota |
|---|---|---|
| `abstract class` | `class C(ABC):` (modulo `abc`) | va importato esplicitamente `from abc import ABC, abstractmethod` |
| metodo astratto (senza corpo) | `@abstractmethod` | |
| errore se una sottoclasse non implementa un metodo astratto | in Java: **non compila**; in Python: `TypeError` **al momento di creare l'oggetto** | in Python l'errore emerge più tardi rispetto a Java (a runtime, non "in compilazione", perché Python non compila in anticipo) |

### Interfacce

| Java | Python | Nota |
|---|---|---|
| parola chiave `interface` | **non esiste, e non serve** | l'equivalente è una classe astratta (`ABC` + soli `@abstractmethod`); dato che Python supporta l'ereditarietà multipla, non serve un meccanismo separato dalle classi |
| `implements` (anche di più interfacce insieme) | stessa sintassi di `extends`/ereditarietà multipla | `class C(Interfaccia1, Interfaccia2):` |
| classe che estende una classe **e** implementa un'interfaccia | nessuna distinzione sintattica | `class C(ClasseBase, Interfaccia):` |
| interfaccia che estende più interfacce | stessa sintassi dell'ereditarietà multipla | |
| campo di interfaccia (implicitamente `public static final`) | attributo di classe | stessa idea di "costante condivisa", ma non realmente immutabile |
| metodo "default" (Java 8+, con corpo già scritto) | **un metodo normale** (senza `@abstractmethod`) dentro la classe astratta | nessuna sintassi speciale richiesta |
| interfaccia "marcatrice" (nessun metodo) | classe vuota (`class I: pass`) | usata solo per raggruppare tipi o per `isinstance()` |

## 8. Concetti senza equivalente diretto (elenco riepilogativo)

Questi sono i casi in cui, più che "tradurre", abbiamo dovuto spiegare
*perché* il problema non si pone in Python, o trovare una soluzione
concettualmente diversa:

- **Overload** di metodi/costruttori → risolto con parametri di default o `*args`.
- **Generics** (`<T>`) → non servono, Python è dinamicamente tipizzato.
- **Distinzione checked/unchecked** tra le eccezioni → non esiste, tutte le eccezioni sono "unchecked".
- **`NullPointerException`** → nessuna eccezione Python dedicata a un valore `None`.
- **`do-while`** e **`for(;;)`** → nessuna sintassi diretta, si usa `while True` + `break`.
- **Distinzione `protected`/`private`** → un solo livello di convenzione in Python.
- **Package** con visibilità "solo nel package" → i moduli Python raggruppano il codice, ma non hanno questo livello di visibilità intermedio.
- **Classi anonime** (`new Classe() { ... }`) → nessuna sintassi equivalente; si usa una sottoclasse con nome esplicito.
- **`Collections.binarySearch`** → non c'è un metodo pronto sulle liste; per un principiante, `.index()` è l'idioma più semplice (la vera ricerca binaria vive nel modulo più avanzato `bisect`).

---

*Documento generato come riferimento per la trasposizione del corso
JAITA131 da Java a Python, modulo per modulo: fondamenta, Collections,
Generics, GestioneErrori, OOP (basi delle classi, ereditarietà, classi
astratte, interfacce).*

## Riepilogo Python vs Java:
|Java|	Python|	Nota didattica|
|---|---|---|
|int, long, short, byte|	int|	Python non distingue questi tipi numerici|
|double, float|	float|	In Python float è il tipo usuale|
|char|	str di lunghezza 1|	Non esiste un tipo char separato|
|String|	str|	Equivalente diretto|
|boolean|	bool|	Equivalente diretto|
|array Java|	list|	Per i primi corsi è la scelta naturale|
|ArrayList|	list|	Non serve simulare ArrayList|
|Scanner	|input()|	Con eventuale int() / float()|
|System.out.println()|	print()|	Equivalente naturale|
|for (int i=0; i<10; i++)|	for i in range(10)|	Python evita inizializzazione/condizione/incremento espliciti|
|for (String x : lista)|	for x in lista|	Iterazione idiomatica|
|++ / --|	x += 1 / x -= 1|	Python non possiede ++ e --|
|switch|	generalmente if/elif|	Non introdurrei match troppo presto|
|static|	nessun equivalente diretto|	Va spiegato in base al contesto|
|overload Java|	nessun overload tradizionale|	In Python normalmente si usa un'unica funzione con parametri opportuni|
|varargs Java|	*args|	Concetto abbastanza vicino|
|final|	nessun equivalente diretto obbligatorio|	Non simulerei final|
|package Java|	modulo/cartella Python|	Ma non serve costruire artificiosamente la stessa struttura|
|main obbligatorio|	nessun main obbligatorio|	Per gli esempi introduttivi preferisco codice eseguibile direttamente|