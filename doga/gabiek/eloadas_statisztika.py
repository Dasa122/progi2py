import random


class Eloadas:
    def __init__(self, cim, mufaj, bemutato_ev, nezoszam, bevetel):
        self.cim = cim
        self.mufaj = mufaj
        self.bemutato_ev = int(bemutato_ev)
        self.nezoszam = int(nezoszam)
        self.bevetel = int(bevetel)


def eloadasok_beolvasasa(fajlnev):
    eloadasok = []
    with open(fajlnev, encoding="utf-8") as fajl:
        fajl.readline()
        for sor in fajl:
            adatok = sor.strip().split(";")
            eloadasok.append(
                Eloadas(
                    adatok[0],
                    adatok[1],
                    adatok[2],
                    adatok[3],
                    adatok[4],
                )
            )
    return eloadasok


def drama_eloadasok_kiirasa(eloadasok):
    print("Drama előadások:")
    for eloadas in eloadasok:
        if eloadas.mufaj == "Dráma":
            print(f"{eloadas.cim} - {eloadas.bemutato_ev}")


def osszes_bevetel_szamitasa(eloadasok):
    osszes_bevetel = 0
    for eloadas in eloadasok:
        osszes_bevetel += eloadas.bevetel
    print(f"\nA színház összes bevétele: {osszes_bevetel} Ft")


def legnepszerubb_eloadas_kiirasa(eloadasok):
    legnepszerubb = eloadasok[0]
    for eloadas in eloadasok:
        if eloadas.nezoszam > legnepszerubb.nezoszam:
            legnepszerubb = eloadas
    print(f"Legnépszerűbb előadás: {legnepszerubb.cim}")


def musical_eloadasok_kiirasa(eloadasok):
    print("\nMusical előadások:")
    for eloadas in eloadasok:
        if eloadas.mufaj == "Musical":
            print(f"{eloadas.cim} - {eloadas.bemutato_ev}")


def veletlen_eloadas_ellenorzese(eloadasok):
    veletlen = random.choice(eloadasok)
    if veletlen.nezoszam > 500:
        minosites = "Sikerdarab"
    else:
        minosites = "Kamaradarab"
    print(f"\nVéletlen ellenőrzés: {veletlen.cim} - {minosites}")


def main():
    fajlnev = "eloadasok.csv"
    eloadasok = eloadasok_beolvasasa(fajlnev)
    drama_eloadasok_kiirasa(eloadasok)
    osszes_bevetel_szamitasa(eloadasok)
    legnepszerubb_eloadas_kiirasa(eloadasok)
    musical_eloadasok_kiirasa(eloadasok)
    veletlen_eloadas_ellenorzese(eloadasok)


main()
