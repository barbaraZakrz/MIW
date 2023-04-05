
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






