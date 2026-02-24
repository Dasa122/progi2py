class Hianyzasok:
    def __init__(self, nev, osztaly, elso_nap, utolso_nap, mulasztott_orak):
        self.nev = nev
        self.osztaly = osztaly
        self.elso_nap = elso_nap
        self.utolso_nap = utolso_nap
        self.mulasztott_orak = mulasztott_orak

    def __str__(self):
        return f"{self.nev} ({self.osztaly})"

hianyzasok = []
osztalyok = []
osztalyHianyzas = []

def beolvasas():
    with open("szeptember.csv", encoding="utf-8") as f:
        f.readline()
        for line in f:
            adatok = line.strip().split(";")
            hianyzasok.append(Hianyzasok(adatok[0], adatok[1], int(adatok[2]), int(adatok[3]), int(adatok[4])))

def mulasztasok():
    osszes = 0
    for hianyzas in hianyzasok:
        osszes += hianyzas.mulasztott_orak
    print(f"2. feladat \n\t Osszes mulasztott orak szama: {osszes} ora.")

def hianyzaslekeres():
    global nev, nap
    h = False
    print("3. feladat")
    nap = int(input("\t Kerem adjon meg egy napot: "))
    nev = input("\t Tanulo neve: ")
    for i in hianyzasok:
        if i.nev == nev:
            h = True
            break

def hianyzok():
    hianyzok = []
    for i in hianyzasok:
        if i.elso_nap <= nap <= i.utolso_nap:
            hianyzok.append(i)
    return hianyzok
            
def osztalylista():
    for i in hianyzasok:
        if i.osztaly not in osztalyok:
            osztalyok.append(i.osztaly)

def osztalyHianyzasok():
    osztalyHianyzas = [0] * len(osztalyok)
    for i in range (len(osztalyok)):
        oh = 0
        for itme in hianyzasok:
            if itme.osztaly == osztalyok[i]:
                oh += itme.mulasztott_orak
            osztalyHianyzas[i] = oh

def fileba():
    with open("osszesitett.csv", "w", encoding="utf-8") as f:
        f.write("Osztaly;MulasztottOrak\n")
        for i in range(len(osztalyok)):
            f.write(f"{osztalyok[i]};{osztalyHianyzas[i]}\n")


def main():
    beolvasas()
    mulasztasok()

    if hianyzaslekeres() == True:
        print("4. feladat")
        print("\t A tanulo hianyzott szeptemberben.")
    else:
        print("4. feladat")
        print("\t A tanulo nem hianyzott szeptemberben.")
    print(f"5. feladat Hianzyok 2017.09.{nap}-n:")
    hianyzok_listaja = hianyzok()
    for i in hianyzok_listaja:
        print(f"\t {i.nev} ({i.osztaly})")


    fileba()

main()