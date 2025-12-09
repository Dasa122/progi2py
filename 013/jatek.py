def pinz():
    napbevetel = int(input("Add meg a napi bevételt: "))
    napicel = int(input("Add meg a napi célt: "))
    if napbevetel >= napicel:
        print("Cél teljesítve!")
    else:
        print("Cél nem teljesítve.")

def bankiszamla():
    aktualis_egyenleg = float(input("Add meg az aktuális egyenleget: "))
    kifizetesiOsszeg = float(input("Add meg a kifizetési összeget: "))
    if kifizetesiOsszeg <= aktualis_egyenleg:
        aktualis_egyenleg -= kifizetesiOsszeg
        print(f"Sikeres kifizetés! Az új egyenleg: {aktualis_egyenleg:.2f} Ft")
    else:
        print("Sikertelen kifizetés! Nincs elég fedezet az egyenlegen.")

def szalloda():
    szobatipus = input("Add meg a szobatípust (standard(15k), premium(25k)): ").strip().lower()
    ejszakakSzama = int(input("Add meg az éjszakák számát: "))
    if szobatipus == "standard":
        ar = 15000 * ejszakakSzama
    elif szobatipus == "premium":
        ar = 25000 * ejszakakSzama
    else:
        print("Ismeretlen szobatípus.")
    print(f"A szállás ára: {ar} Ft")

def vizfogyasztas():
    haviFogyasztas = float(input("Add meg a havi vízfogyasztást literben: "))
    kivantfogyasztas = float(input("Add meg a kívánt fogyasztást literben: "))
    if haviFogyasztas <= kivantfogyasztas:
        print("A fogyasztás megfelelő.")
    else:
        print("A fogyasztás meghaladja a kívánt értéket.")

def haviKoltsegvetes():
    jovedelem = int(input("Add meg a havi jövedelmet: "))
    kiadasok = int(input("Add meg a havi kiadásokat: "))
    honapvege = jovedelem - kiadasok
    print(f"A hónap végi egyenleg: {honapvege} Ft")
    if kiadasok > jovedelem:
        print("Mérleg veszteséges.")
    else:
        print("Mérleg nyereséges.")

def szallitasidij():
    csomagsuly = float(input("Add meg a csomag súlyát kg-ban: "))
    celorszag = input("Add meg a célországot (belfold/kulfold): ").strip().lower()
    if celorszag == "belfold":
        if csomagsuly <= 5:
            dij = 1500
        else:
            dij = 2000
    elif celorszag == "kulfold":
        if csomagsuly <= 5:
            dij = 3000
        else:
            dij = 3500
    else:
        print("Ismeretlen célország.")
    print(f"A szállítási díj: {dij} Ft")

def fitnessz():
    tipus = input("Add meg az edzés típusát (havi/eves): ").strip().lower()
    hanyevrehonapra = int(input("Add meg, hány évre/hónapra szeretnéd az előfizetést: "))
    if tipus == "havi":
        ar = 5000 * hanyevrehonapra
    elif tipus == "eves":
        ar = 50000 * hanyevrehonapra * 0.9
    else:
        print("Ismeretlen előfizetés típus.")
    print(f"Az előfizetés ára: {ar} Ft")

def filmar():
    kor = int(input("Add meg a korodat: "))
    filmcim = input("Add meg a film címét: ").strip().lower()
    if kor < 18:
        ar = 1500
    elif kor >= 65:
        ar = 1500
    else:
        ar = 2500
    print(f"A jegy ára a(z) {filmcim} filmre: {ar} Ft")

def main():
    print("1. Pinz")
    pinz()
    print("\n2. Banki Számla")
    bankiszamla()
    print("\n3. Szálloda")
    szalloda()
    print("\n4. Vízfogyasztás")
    vizfogyasztas()
    print("\n5. Havi Költségvetés")
    haviKoltsegvetes()
    print("\n6. Szállítási Díj")
    szallitasidij()
    print("\n7. Fitnessz Előfizetés")
    fitnessz()
    print("\n8. Filmár")
    filmar()
main()