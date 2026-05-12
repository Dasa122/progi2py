class kepregeny:
    def __init__(self, kategoria, cim, ar, chroma):
        self.kategoria = kategoria
        self.cim = cim
        self.ar = int(ar)
        self.chroma = chroma

    def __str__(self):
        return(f"{self.cim}")



kepregenyek = []



def beolvasas():
    with open("forras.csv", "r", encoding="UTF-8") as f:
        f.readline()
        for i in f:
            kepregenyek.append(kepregeny(*i.strip().split(";")))

def cimek_kiirasa():
    print("3.2 A képregények:")
    for i in kepregenyek:
        print(i.cim, end=", ")

def legdragabb():
    temp = 0
    for i in kepregenyek:
        if int(i.ar) > temp:
            temp = int(i.ar)
            talalat = i
    print(f"3.3 A legdrágább képregény: {talalat.cim} Ára: {talalat.ar} Ft")

def kategoriak():
    catt = []
    for i in kepregenyek:
        if i.kategoria not in catt:
            catt.append(i.kategoria)
    print("3.4 Kategóriák:")
    print(*catt, sep=", ")

def feketeFeherKategoriaban(kategoria):
    talalatok = []
    for i in kepregenyek:
        if i.kategoria == kategoria and i.chroma == "igen":
            talalatok.append(i.cim)
    if talalatok:
        print(f"Van fekete-fehér manga!", end=" ")
        print(f"(", end="")
        print(*talalatok, sep=", ", end="")
        print(f")", end="")

    else:
        print("3.5 Nincs ilyen képregény.")



def main():
    beolvasas()
    cimek_kiirasa()
    legdragabb()
    kategoriak()
    valasztas = input("3.5 Kérem adjon meg egy kategóriát: ")
    feketeFeherKategoriaban(valasztas)

main()