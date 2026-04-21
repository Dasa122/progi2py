etelek = []
class Etel():
    def __init__(self, kategoria, nev, ar, glutenTartalom):
        self.kategoria= kategoria
        self.nev= nev
        self.ar=ar
        self.glutenTartalom=glutenTartalom
    
    def __str__(self):
        return f"{self.kategoria} {self.nev} {self.ar} {self.glutenTartalom}"



def beolvas():
    with open("feladat3_forras.csv", "r", encoding="UTF-8") as f:
        f.readline()
        for i in f:
            asd = i.strip().split(";")
            etelek.append(Etel(*asd))

def kiiratas():
    for i in etelek:
        print(i.nev, end=", ")
    print()

def glutenmentes():
    van = False
    for i in etelek:
        if i.kategoria == "desszert" and i.glutenTartalom == "igen":
            van = True
            print(f"3.4 Van gluténmentes desszert! ({i.nev})")
            break
    if not van:
        print("Nimcs glutenmentes deszert!")


def legdragabb():
    price = 0
    for i in etelek:
        if int(i.ar) > int(price):
            price = i.ar
    for i in etelek:
        if price == i.ar:
            print(f"3.3 A legdrágább étel: {i.nev} Ára: {i.ar} Ft")

def kategoriak():
    cat = []
    for i in etelek:
        if i.kategoria not in cat:
            cat.append(i.kategoria)
    print("3.5 Az étlapon elérhető kategóriák: ")
    print(*cat, sep=", ")

def main():
    beolvas()
    kiiratas()
    legdragabb()
    glutenmentes()
    kategoriak()

main()