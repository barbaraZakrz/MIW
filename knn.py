import math

class Probka:
    lista_probek = []

    def __init__(self, klasa, wartosci = None):
        self.klasa = klasa
        if wartosci == None:
            self.wartosci = []
        else:
            self.wartosci = wartosci
        Probka.lista_probek.append(self)

    @classmethod
    def wczytaj_z_pliku(cls, plik):
        items = []
        with open(plik, 'r') as f:
            reader = f.readlines()
            for line in reader:
                line = line.rstrip('\n')
                items.append(line.split('\t'))

            for item in items:
                Probka(
                    klasa = item.pop(len(item)-1),
                    wartosci = [float(x) for x in item])

    @classmethod
    def normalizacja(cls):
        min1 = Probka.lista_probek[0].wartosci.copy()
        max1 = Probka.lista_probek[0].wartosci.copy()

        for i in Probka.lista_probek:
            for j in range(len(i.wartosci)):
                if i.wartosci[j] < min1[j]:
                    min1[j] = i.wartosci[j]
                if i.wartosci[j] > max1[j]:
                    max1[j] = i.wartosci[j]
        #print(min, max)
        for p in Probka.lista_probek:
            for r in range(len(p.wartosci)):
                p.wartosci[r] = (p.wartosci[r] - min1[r])/(max1[r] - min1[r])
        return Probka.lista_probek

    def __repr__(self):
        return 'Probka({}, klasa: {}'.format(self.wartosci, self.klasa)


def euklides(obiekt1, obiekt2):
    suma = 0
    for i in range(len(obiekt1.wartosci)):
        suma += math.pow(obiekt1.wartosci[i] - obiekt2.wartosci[i], 2)
    return math.sqrt(suma)

def manhattan(obiekt1, obiekt2):
    suma = 0
    for i in range(len(obiekt1.wartosci)):
        suma += abs(obiekt1.wartosci[i] - obiekt2.wartosci[i])
    return suma

def czebyszew(obiekt1, obiekt2):
    suma = 0
    for i in range(len(obiekt1.wartosci)):
        if suma < abs(obiekt1.wartosci[i]-obiekt2.wartosci[i]):
            suma = abs(obiekt1.wartosci[i]-obiekt2.wartosci[i])
    return suma

def minkowski(obiekt1, obiekt2, p =2):
    suma = 0
    for i in range(len(obiekt1.wartosci)):
        suma += math.pow(abs(obiekt1.wartosci[i] - obiekt2.wartosci[i]), p)
    return math.pow(suma, 1/p)

def logarytm(obiekt1, obiekt2):
    suma = 0
    for i in range(len(obiekt1.wartosci)):
        if obiekt1.wartosci[i] == 0 or obiekt2.wartosci[i] == 0:
            suma = 0
        else:
            suma += abs((math.log(obiekt1.wartosci[i]))-(math.log(obiekt2.wartosci[i])))
        # print(suma)
    return suma

def knn(k, test, listaP, metryka):
#ZMIANA
    odleglosci = {}  # {odleglosc: klasa}
    wystapienia = {}  # {klasa: wystapienia}

#ZMIANA
    for i in range(0, len(listaP)):
        # odleglosci.update({metryka(test, listaP[i]):listaP[i].klasa})
        odleglosci[metryka(test, listaP[i])] = listaP[i].klasa
    odleglosci = dict(sorted(odleglosci.items())[:k])


    for m in list(odleglosci.values()):
        if m not in wystapienia.keys():
            wystapienia.update({m:1})
        else:
            wystapienia[m] +=1

    wynik = sorted(wystapienia.items(), key=lambda item: item[1])
    # print(wynik)
    if len(wynik) > 1:
        if wynik[-1][1] == wynik[-2][1]:
            # print(wynik,'\nremis, odmowa odpowiedzi')
            return None
    return wynik[-1][0]
    #return sorted(wystapienia.items(), key=lambda item: item[1])[-1][0]


def jeden_kontra_reszta(k, listaO, metryka, p=2):
    t = 0
    f = 0
    for i in range(len(listaO)):
        test1 = listaO.pop(0)
        if knn(k, test1, listaO, metryka) == test1.klasa:
            t+=1
        else:
            f+=1
        listaO.append(test1)
    #print(f"{metryka.__name__}: poprawnych: {t}, niepoprawnych: {f}, wszystkich: {len(listaO)} procent poprawnych: {t/len(listaO)}")
    print(f"procent poprawnych dla {metryka.__name__}: {t / len(listaO)}")
print('================')

def uruchom():
    k = int(input("Podaj k: "))
    # p = int(input("Podaj p: "))
    jeden_kontra_reszta(k, Probka.lista_probek, euklides)
    jeden_kontra_reszta(k, Probka.lista_probek, manhattan)
    jeden_kontra_reszta(k, Probka.lista_probek, czebyszew)
    jeden_kontra_reszta(k, Probka.lista_probek, minkowski)
    jeden_kontra_reszta(k, Probka.lista_probek, logarytm)


Probka.wczytaj_z_pliku('iris.txt')
# print(Probka.lista_probek)
Probka.normalizacja()
# print(Probka.lista_probek)
uruchom()