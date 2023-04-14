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
# root.wyswietl()
minMax(root)
# root.wyswietl()
root.wyswietl_droge()
