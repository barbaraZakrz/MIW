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
        max  =Probki.lista_probek[0].par.copy()

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

print(euklides(Probki.lista_probek[0], Probki.lista_probek[1]))

def knn(k, test, listaO):
    lista = {}
    grupy = {}
    for i in range(1, len(listaO)):
        lista.update({euklides(test, listaO[i]):listaO[i].grupa} )
    lista = dict(sorted(lista.items()))
    #print(lista)
    for m in list(lista.values())[:k]:
        if m not in grupy.keys():
            grupy.update({m:1})
        else:
            grupy[m] +=1
    grupy = list(dict(sorted(grupy.items())))
    return grupy[-1]

# def knn(k):
#     lista = {}
#     grupy = {}
#     for i in range(1, len(Probki.lista_probek)):
#         lista.update({euklides(Probki.lista_probek[0], Probki.lista_probek[i]):Probki.lista_probek[i].grupa} )
#     #lista = dict(sorted(lista.items(), key=lambda item: item[1]))
#     lista = dict(sorted(lista.items()))
#     print(lista)
#     for m in list(lista.values())[:k]:
#         if m not in grupy.keys():
#             grupy.update({m:1})
#         else:
#             grupy[m] +=1
#     grupy = list(dict(sorted(grupy.items())))
#     return grupy[-1]

def jeden(listaO):
    t = 0
    f = 0
    for i in range(len(listaO)):
        test1 = listaO.pop(i)
        if knn(3, test1, listaO) == test1.grupa:
            t +=1
        else:
            f+=1
        listaO.append(test1)
    print(t, f, len(listaO), t/len(listaO))

print('================')
#print(knn(3,Probki.lista_probek[0], Probki.lista_probek))
jeden(Probki.lista_probek)
print('==============')

a = {1:2,4:2, 3:1, 2:5,7:1, 8:3}
a = dict(sorted(a.items(), key=lambda item: item[1]))
b =sorted(a.items())
print(a)
print(b)









