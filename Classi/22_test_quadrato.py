"""
Creare una classe Quadrato, che dichiari un attributo lato. Quindi creare
un metodo pubblico che si chiami perimetro() e che ritorni il perimetro
del quadrato, e un metodo pubblico area() che ritorni l'area del
quadrato. Creare una classe TestQuadrato che istanzi un oggetto q1 di
tipo Quadrato, con lato di valore 5. Stampare il perimetro e l'area
dell'oggetto appena creato. Successivamente creare un array (in Python:
una lista) di tipo Quadrato di dimensione n a piacere, inserire come
primo elemento l'oggetto q1 già creato. Tutti gli altri elementi devono
essere inseriti da tastiera. Stampare per ogni quadrato l'area, sommare
il perimetro totale e indicare in quale posizione si trova il Quadrato
con il perimetro più grande (in caso di parità, il primo inserito).
"""


class Quadrato:

    def __init__(self, lato):
        self.lato = lato

    def perimetro(self):
        return self.lato * 4

    def area(self):
        return self.lato * self.lato


# ================== PROVA (equivalente del "main" di Java) ==================

q1 = Quadrato(5)
perimetro_q1 = q1.perimetro()
area_q1 = q1.area()
perimetro_tot = 0
perimetro_max = 0
pos = 0

print("perimetro", perimetro_q1, "area:", area_q1)

arr_q = [None] * 3
arr_q[0] = q1

for i in range(1, len(arr_q)):
    print("inserisci il lato:")
    lato = int(input())
    arr_q[i] = Quadrato(lato)

perimetro_max = arr_q[0].perimetro()

for i in range(len(arr_q)):
    print("l'area del quadrato è:", arr_q[i].area())
    print("il perimetro è:", arr_q[i].perimetro())
    perimetro_tot += arr_q[i].perimetro()
    if arr_q[i].perimetro() > perimetro_max:  # se sono uguali non entra nell'if: resta il valore precedente
        perimetro_max = arr_q[i].perimetro()
        pos = i

# bonus: trova le posizioni dei perimetri massimi uguali
for i in range(len(arr_q)):
    if perimetro_max == arr_q[i].perimetro():
        print("le posizioni uguali sono:", i)

print("somma dei perimetri", perimetro_tot)
print("perimetro max", perimetro_max, "alla posizione", pos)
