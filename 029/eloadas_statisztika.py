import random


class Eloadas:
    def __init__(self, cim, mufaj, bemutato_eve, nezoszam, bevetel):
        self.cim = cim
        self.mufaj = mufaj
        self.bemutato_eve = bemutato_eve
        self.nezoszam = nezoszam
        self.bevetel = bevetel


def beolvas_fajl(fajlnev: str) -> list[Eloadas]:
    eloadasok: list[Eloadas] = []

    with open(fajlnev, encoding="utf-8", newline="") as fajl:
        sorok = fajl.read().splitlines()
        for sor in sorok[1:]:
            adatok = sor.split(";")
            eloadasok.append(
                Eloadas(
                    cim=adatok[0],
                    mufaj=adatok[1],
                    bemutato_eve=int(adatok[2]),
                    nezoszam=int(adatok[3]),
                    bevetel=int(adatok[4]),
                )
            )

    return eloadasok


def main():
    eloadasok = beolvas_fajl("eloadasok.csv")

    print("Dráma előadások:")
    for eloadas in eloadasok:
        if eloadas.mufaj == "Dráma":
            print(f"{eloadas.cim} ({eloadas.bemutato_eve})")

    ossz_bevetel = sum(eloadas.bevetel for eloadas in eloadasok)
    print(f"\nA színház összes bevétele: {ossz_bevetel} Ft")

    legnepszerubb = max(eloadasok, key=lambda eloadas: eloadas.nezoszam)
    print(
        f"A legnépszerűbb előadás: {legnepszerubb.cim} "
        f"({legnepszerubb.nezoszam} néző)"
    )

    print("\nMusical előadások:")
    for eloadas in eloadasok:
        if eloadas.mufaj == "Musical":
            print(f"{eloadas.cim} ({eloadas.bemutato_eve})")

    veletlen_eloadas = random.choice(eloadasok)
    minosites = "Sikerdarab" if veletlen_eloadas.nezoszam > 500 else "Kamaradarab"
    print(
        f"\nVéletlen ellenőrzés: {veletlen_eloadas.cim} - {minosites}"
    )


main()
