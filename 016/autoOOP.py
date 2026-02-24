class Auto:
    def __init__(self, marka: str, evjarat: int, szin: str):
        self.marka = marka
        self.evjarat = evjarat
        self.szin = szin

    def __str__(self):
        return f"Auto(marka={self.marka}, evjarat={self.evjarat}, szin={self.szin})"
    
lista = []

def konkretAutokLetrehozasa():
    auto1 = Auto("Toyota", 2015, "piros")
    print(auto1)
    auto2 = Auto("Honda", 2018, "kek")
    print(auto2)
    auto3 = Auto("Ford", 2020, "fekete")
    print(auto3)
    lista.append(auto1)
    lista.append(auto2)
    lista.append(auto3)

def fiatalabbAutoKeresese():
    fiatalabb = lista[0]
    for i in lista:
        if i.evjarat > fiatalabb.evjarat:
            fiatalabb = i
    print("Legfiatalabb auto:")
    print(fiatalabb)


def export():
    f = open("autok.txt", "w")
    for i in lista:
        f.write(f"{i.marka},{i.evjarat},{i.szin}\n")
    f.close()

def imports():
    f = open("autok.txt", "r")
    for line in f:
        marka, evjarat, szin = line.strip().split(",")
        auto = Auto(marka, int(evjarat), szin)
        lista.append(auto)
    f.close()

def keres():
    keresettvalami = input("Add meg a keresett marka nevet szinet vagy evjaratot: ")
    talalatok = []
    for i in lista:
        if keresettvalami.lower() in i.marka.lower():
            if i not in talalatok:
                talalatok.append(i)
        if keresettvalami.lower() in i.szin.lower():
            if i not in talalatok:
                talalatok.append(i)
        if keresettvalami.isdigit() and int(keresettvalami) == i.evjarat:
            if i not in talalatok:
                talalatok.append(i)
    if talalatok:
        print("Talalatok:")
        for talalat in talalatok:
            print(talalat)
    else:
        print("Nincs talalat.")

def main():
    konkretAutokLetrehozasa()
    fiatalabbAutoKeresese()
    export()
    imports()
    keres()
main()
