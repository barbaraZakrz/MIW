class Node:
    def __init__(self, protagonist, value=0, suma=0, parent=None):
        self.protagonist = protagonist
        self.value = value
        self.suma = suma + value
        self.parent = parent
        self.children = []
        if self.suma < 21:
            self.children.append(Node(not protagonist, 4, self.suma, self))
            self.children.append(Node(not protagonist, 5, self.suma, self))
            self.children.append(Node(not protagonist, 6, self.suma, self))
            self.result = None
        elif self.suma == 21:
            self.result = 0
        else:
            if protagonist:
                self.result = 1
            else:
                self.result = -1

    def __repr__(self):
        return "protagonista: {}, karta: {}, suma: {}, result: {}".format(self.protagonist, self.value, self.suma, self.result)

    def printRecur(self):
        print(self)
        for child in self.children:
            child.printRecur()

    def printRoute(self):
        print(self)
        if(self.children):
            print("dzieci: {")
            for child in self.children:
                print(child)
            print("},")
            sortedChildren = sorted(self.children.copy(), key=lambda x: x.result, reverse=self.protagonist)
            sortedChildren[0].printRoute()

def minMax(node):
    if node.result is not None:
        return node.result
    results = []
    for child in node.children:
        results.append(minMax(child))
    # results.sort(reverse=(not node.protagonist))
    results = sorted(results, reverse=node.protagonist)
    node.result = results[0]
    return results[0]

root = Node(False)
minMax(root)
root.printRoute()