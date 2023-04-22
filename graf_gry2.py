from itertools import chain

class Node:
    def __init__(self, protagonista, wartosc=0, suma=0, rodzic=None):
        self.protagonista = protagonista
        self.wartosc = wartosc
        self.suma = suma + wartosc
        self.rodzic = rodzic
        self.dzieci = []
        if self.suma < 21:
            self.dzieci.append(Node(not protagonista, 4, self.suma, self))
            self.dzieci.append(Node(not protagonista, 5, self.suma, self))
            self.dzieci.append(Node(not protagonista, 6, self.suma, self))
            self.wynik = None
        elif self.suma == 21:
            self.wynik = 0
        else:
            if protagonista:
                self.wynik = 1
            else:
                self.wynik = -1

    def __repr__(self):
        #wyswietla wierzcholki, a ruch to krawedz, wiec wypisana tutaj karta to efekt poprzedniego ruchu
        return "protagonista: {}, karta: {}, suma: {}, result: {}".format(self.protagonista, self.wartosc, self.suma, self.wynik)

    def wyswietl(self):
        print(self)
        for dziecko in self.dzieci:
            dziecko.wyswietl()

    def wyswietl2(self):
        slownik = {}
        # if self.protagonista:
        #     print('"P - {}"'.format(self.suma))
        # else:
        #     print('"A - {}" [label = {}];'.format(self.suma, self.wartosc))
        if self.dzieci:
            for dziecko in self.dzieci:
                if self.protagonista is True:
                    if '"P - {}" -> "A - {}" [label = {}];'.format(self.suma, dziecko.suma, dziecko.wartosc) not in slownik.keys():
                        slownik.update({'"P - {}" -> "A - {}" [label = {}];'.format(self.suma, dziecko.suma, dziecko.wartosc):1})
                    # print('"P - {}" -> "A - {}" [label = {}];'.format(self.suma, dziecko.suma, dziecko.wartosc))
                else:
                    if '"A - {}" -> "P - {}" [label = {}];'.format(self.suma, dziecko.suma, dziecko.wartosc) not in slownik.keys():
                        slownik.update({'"A - {}" -> "P - {}" [label = {}];'.format(self.suma, dziecko.suma, dziecko.wartosc): 1})
                    # print('"A - {}" -> "P - {}" [label = {}];'.format(self.suma, dziecko.suma, dziecko.wartosc))
                dziecko.wyswietl2()
            for key in slownik.keys():
                print(key)

    def wyswietl3(self):
        slownik = {}
        # if self.protagonista:
        #     print('"P - {}"'.format(self.suma))
        # else:
        #     print('"A - {}" [label = {}];'.format(self.suma, self.wartosc))
        if self.wynik == 1:
            if self.dzieci:
                for dziecko in self.dzieci:
                    if self.protagonista is True:
                        if '"P - {}, wynik: {}" -> "A - {}" [label = {}];'.format(self.suma, self.wynik, dziecko.suma, dziecko.wartosc) not in slownik.keys():
                            slownik.update({'"P - {}, wynik: {}" -> "A - {}" [label = {}];'.format(self.suma, self.wynik, dziecko.suma, dziecko.wartosc):1})
                    # print('"P - {}" -> "A - {}" [label = {}];'.format(self.suma, dziecko.suma, dziecko.wartosc))
                    else:
                        if '"A - {}" -> "P - {}, wynik: {}" [label = {}];'.format(self.suma, self.wynik, dziecko.suma, dziecko.wartosc) not in slownik.keys():
                            slownik.update({'"A - {}, wynik: {}" -> "P - {}" [label = {}];'.format(self.suma, self.wynik, dziecko.suma, dziecko.wartosc): 1})
                    # print('"A - {}" -> "P - {}" [label = {}];'.format(self.suma, dziecko.suma, dziecko.wartosc))
                    dziecko.wyswietl3()
            for key in slownik.keys():
                print(key)

    def wyswietl_droge(self):
        print(self)
        if(self.dzieci):
            # print("dzieci: {")
            # for dziecko in self.dzieci:
            #     print(dziecko)
            # print("},")
            sortedChildren = sorted(self.dzieci.copy(), key=lambda x: x.wynik, reverse=self.protagonista)
            sortedChildren[0].wyswietl_droge()

def minMax(node):
    if node.wynik is not None:
        return node.wynik
    results = []
    for dziecko in node.dzieci:
        results.append(minMax(dziecko))
    results = sorted(results, reverse=node.protagonista)
    node.wynik = results[0]
    return results[0]

root = Node(True)
#root.wyswietl()
minMax(root)
# root.wyswietl()
#root.wyswietl_droge()
#root.wyswietl2()
root.wyswietl3()
