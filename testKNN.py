import math

class Probki:
    lista_probek = []

    def __init__(self, grupa, par = None):
        self.grupa = grupa
        if par == None:
            self.par = []
        else:
            self.par = par
        Probki.lista_probek.append(self)

    @classmethod
    def wczytaj_z_pliku(cls):
        items = []
        with open('iris.txt', 'r') as f:
            reader = f.readlines()
            for line in reader:
                line = line.rstrip('\n')
                items.append(line.split('\t'))

        for item in items:
            Probki(
                grupa = item.pop(len(item)-1),
                par = [float(x) for x in item])

    @classmethod
    def normalizacja(cls):
        min = Probki.lista_probek[0].par.copy()
        max = Probki.lista_probek[0].par.copy()

        for i in Probki.lista_probek:
            for j in range(len(i.par)):
                if i.par[j] < min [j]:
                    min[j] = i.par[j]
                if i.par[j] > max [j]:
                    max[j] = i.par[j]
        #print(min, max)
        for i in Probki.lista_probek:
            for j in range(len(i.par)):
                i.par[j] = (i.par[j] - min[j])/(max[j]-min[j])
        return Probki.lista_probek


    def __repr__(self):
        return 'Probka({}, grupa: {}'.format(self.par, self.grupa)


Probki.wczytaj_z_pliku()
print(Probki.lista_probek)
Probki.normalizacja()
print(Probki.lista_probek)

def euklides(obiekt1, obiekt2):
    suma = 0
    for i in range(len(obiekt1.par)):
        suma += math.pow(obiekt1.par[i] - obiekt2.par[i], 2)
    return math.sqrt(suma)

def manhattan(obiekt1, obiekt2):
    suma = 0
    for i in range(len(obiekt1.par)):
        suma += abs(obiekt1.par[i]- obiekt2.par[i])
    return suma

def czebyszew(obiekt1, obiekt2):
    suma = 0
    for i in range(len(obiekt1.par)):
        if suma < abs(obiekt1.par[i]-obiekt2.par[i]):
            suma = abs(obiekt1.par[i]-obiekt2.par[i])
    return suma

def minkowski(obiekt1, obiekt2, p =2):
    suma = 0
    for i in range(len(obiekt1.par)):
        suma +=math.pow(abs(obiekt1.par[i] - obiekt2.par[i]),p)
    return math.pow(suma, 1/p)

def logarytm(obiekt1, obiekt2):
    suma = 0
    for i in range(len(obiekt1.par)):
        print(obiekt1.par[i], obiekt2.par[i])
        suma += abs((math.log(obiekt1.par[i]))-(math.log(obiekt2.par[i])))
        print(suma)
    return suma

print(euklides(Probki.lista_probek[0], Probki.lista_probek[1]))

def knn(k, test, listaO, metryka):
    odleglosci = {}  # {odleglosc: klasa}
    wystapienia = {}  # {klasa: wystapienia}

    for i in range(0, len(listaO)):
        odleglosci.update({metryka(test, listaO[i]):listaO[i].grupa} )
    odleglosci = dict(sorted(odleglosci.items())[:k])

    for m in list(odleglosci.values()):
        if m not in wystapienia.keys():
            wystapienia.update({m:1})
        else:
            wystapienia[m] +=1
    return sorted(wystapienia.items(), key=lambda item: item[1])[-1][0]


def jeden(k, listaO, metryka):
    t = 0
    f = 0
    for i in range(len(listaO)):
        test1 = listaO.pop(0)
        if knn(k, test1, listaO, metryka) == test1.grupa:
            t+=1
        else:
            f+=1
        listaO.append(test1)
    #print(f"{metryka.__name__}: poprawnych: {t}, niepoprawnych: {f}, wszystkich: {len(listaO)} procent poprawnych: {t/len(listaO)}")
    print(f"procent poprawnych dla {metryka.__name__}: {t / len(listaO)}")
print('================')
def uruchom():
    k = int(input("Podaj k: "))
    jeden(k, Probki.lista_probek, euklides)
    jeden(k, Probki.lista_probek, manhattan)
    jeden(k, Probki.lista_probek, czebyszew)
    jeden(k, Probki.lista_probek, minkowski)
    #jeden(k, Probki.lista_probek, logarytm)
#print(knn(3,Probki.lista_probek[0], Probki.lista_probek))
# jeden(Probki.lista_probek,euklides)
# jeden(Probki.lista_probek, manhattan)
# jeden(Probki.lista_probek, czebyszew)
# jeden(Probki.lista_probek, minkowski)
# jeden(Probki.lista_probek, logarytm)

uruchom()
a = {1:2,4:2, 3:1, 2:5,7:1, 8:3}
a = dict(sorted(a.items(), key=lambda item: item[1]))
b =sorted(a.items())









