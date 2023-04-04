
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
                wiersz = []
                wiersz = line.split('\t')
                items.append(wiersz)

        for item in items:
            Probki(
                grupa = item.pop(len(item)-1),
                par = [float(x) for x in item],)

    def __repr__(self):
        return 'Probka({}, grupa: {}'.format(self.par, self.grupa)


Probki.wczytaj_z_pliku()
print(Probki.lista_probek)




