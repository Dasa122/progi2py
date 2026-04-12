class Noveny:
    def __init__(self, nev, resz, kezdes, befejezes):
        self.nev = nev
        self.resz = resz
        self.kezdes = int(kezdes)
        self.befejezes = int(befejezes)

    def __str__(self):
        return f"{self.nev} ({self.resz}): {self.kezdes}-{self.befejezes}"


def beolvas(fajlnev):
    novenyek = []
    with open(fajlnev, encoding="utf-8") as f:
        for sor in f:
            sor = sor.strip()
            if sor:
                reszek = sor.split(";")
                n = Noveny(reszek[0], reszek[1], reszek[2], reszek[3])
                novenyek.append(n)
    return novenyek


# 1. A gyöngyvirág melyik részét gyűjtik
def gyongyvirag_resze(novenyek):
    for n in novenyek:
        if n.nev.lower() == "gyongyvirag":
            print(f"A gyöngyvirág gyűjtött része: {n.resz}")
            return


# 2. Hány növényt gyűjtenek a leveléért
def level_szama(novenyek):
    db = 0
    for n in novenyek:
        if n.resz == "level":
            db += 1
    print(f"Leveléért gyűjtött növények száma: {db}")


# 3. Mely részekért gyűjtik a növényeket
def reszek_listaja(novenyek):
    reszek = []
    for n in novenyek:
        if n.resz not in reszek:
            reszek.append(n.resz)
    reszek.sort()
    print("Gyűjtött részek:")
    for r in reszek:
        print(f"  {r}")


# 4. Melyik növényeket kezdik el ősszel gyűjteni
def oszi_gyujtes(novenyek):
    print("Ősszel gyűjteni kezdett növények:")
    for n in novenyek:
        if n.kezdes == 9 or n.kezdes == 10 or n.kezdes == 11:
            print(f"  {n.nev}")


# 5. Hány növényt gyűjtenek virággal kapcsolatos részéért
def viragos_szama(novenyek):
    db = 0
    for n in novenyek:
        if "virag" in n.resz:
            db += 1
    print(f"Virággal kapcsolatos részért gyűjtött növények száma: {db}")


# 6. Melyik növényt hány hónapig gyűjtik
def gyujtesi_idotartam(novenyek):
    print("\nNövény gyűjtési időszakok:")
    for n in novenyek:
        if n.befejezes >= n.kezdes:
            honapok = n.befejezes - n.kezdes + 1
        else:
            honapok = (12 - n.kezdes + 1) + n.befejezes
        print(f"  {n.nev}: {honapok} hónap")


# Segédfüggvény: gyűjtenek-e az adott hónapban
def gyujtik_e(honap, novenyek):
    for n in novenyek:
        if n.befejezes >= n.kezdes:
            if n.kezdes <= honap and honap <= n.befejezes:
                return True
        else:
            if honap >= n.kezdes or honap <= n.befejezes:
                return True
    return False


# 7. Van-e olyan hónap, amikor semmit nem gyűjtenek
def ures_honapok(novenyek):
    ures = []
    for h in range(1, 13):
        if not gyujtik_e(h, novenyek):
            ures.append(h)
    if ures:
        print(f"\nOlyan hónapok, amikor semmit nem gyűjtenek: {ures}")
    else:
        print("\nNincs olyan hónap, amikor semmit nem gyűjtenek.")


def main():
    novenyek = beolvas("gyogynovenyek.txt")

    gyongyvirag_resze(novenyek)
    level_szama(novenyek)
    reszek_listaja(novenyek)
    oszi_gyujtes(novenyek)
    viragos_szama(novenyek)
    gyujtesi_idotartam(novenyek)
    ures_honapok(novenyek)


main()
