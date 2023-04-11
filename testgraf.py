class Root:
    graf = []
    def __init__(self, name, wartosc=0, suma=0):
        self.name = name
        self.wartosc = wartosc
        self.suma = suma +wartosc
        self.dzieci = []
        Root.graf.append(self)

    def __repr__(self):
        return "{}(wartość: {}, suma: {})".format(self.name, self.wartosc, self.suma)

class Node(Root):
    graf = []
    def __init__(self, name, wartosc, suma, rodzic):
        super().__init__(name, wartosc, suma)
        self.rodzic = rodzic
        self.dzieci = []
        Node.graf.append(self)

    def __repr__(self):
        return "{}(wartość: {}, suma: {}, rodzic: {}, {})".format(self.name, self.wartosc, self.suma, self.rodzic.name, self.rodzic.suma)


def generate_children(node):
    if node.name == 'Protagonista':
            node.dzieci.append(Node("Antagonista", 4, node.suma, node))
            node.dzieci.append(Node("Antagonista", 5, node.suma, node))
            node.dzieci.append(Node("Antagonista", 6, node.suma, node))
    else:
            node.dzieci.append(Node("Protagonista", 4, node.suma, node))
            node.dzieci.append(Node("Protagonista", 5, node.suma, node))
            node.dzieci.append(Node("Protagonista", 6, node.suma, node))

def graff(node):
        generate_children(node)
        for child in node.dzieci:
            if child.suma >= 21:
                break
            else:
                graff(child)


root = Root("Protagonista")
# print(root)

graff(root)
# print(*Node.graf, sep='\n')

# print(len(Node.graf))
# print(len(Root.graf))

# for elem in Root.graf:
#     if elem.suma == 21:
#         print("REMIS")
#     if elem.suma > 21:
#         print(f'Wygrana {elem.rodzic.name}')

def minmax():
    lista = []
    for elem in Root.graf:
        if elem.suma == 21:
            lista.append()








