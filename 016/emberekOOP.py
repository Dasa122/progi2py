class Ember:
    def __init__(self, nev:str, szuletesiEv:int, magassag:float):
        self.nev = nev
        self.szuletesiEv = szuletesiEv
        self.magassag = magassag
    
    def __str__(self):
        return f"Ember(nev={self.nev}, szuletesiEv={self.szuletesiEv}, magassag={self.magassag})"

lista = []
def konkretEmberekLetrehozasa():
    ember1 = Ember("Kovago Gergo", 2009, 170.1)
    print(ember1.nev)
    print(ember1.szuletesiEv)
    print(ember1.magassag)  
    ember2 = Ember("jancsi", 2010, 160.5)
    print(ember2)
    ember3 = Ember("juliska", 2011, 150.3)
    print(ember3)
    lista.append(ember1)
    lista.append(ember2)
    lista.append(ember3)

def kiratas():
    print("------------------------------------")
    for i in lista:
        print(i.nev)
    print("-----------magassagok---------------")
    for i in lista:
        print(i.magassag)

    print("legmagasabb ember:")
    legmagasabb = lista[0]
    for i in lista:
        if i.magassag > legmagasabb.magassag:
            legmagasabb = i
    print(legmagasabb)


def main():
    konkretEmberekLetrehozasa()
    kiratas()

main()