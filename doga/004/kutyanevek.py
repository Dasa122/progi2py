kutyanevek = ["Bodri", "Molly", "Buksi", "Luna", "Rex", "Pamacs", "Csoki", "Tappancs", "Zeusz", "Fanni", "Bella", "Zsömi", "Kormi", "Ares", "Mancs", "Lizi", "Daisy", "Max", "Áfonya", "Tobi"]

def kutyusokSzama():
    print(f"{len(kutyanevek)} kutya van a listaba.")

def szamolas(vegbetu):
    for i in kutyanevek:
        if i[-1] == vegbetu:
            vegszam =+ 1
    return vegszam

def leghosszabbNev():
    temp = 0
    for i in kutyanevek:
        if len(i) > temp:
            temp = len(i)
    return temp



def kereses(resz):
    talalatok = []
    for nev in kutyanevek:
        if resz in nev:
            talalatok.append(nev)
    
    if talalatok:
        for talalat in talalatok:
            print(talalat)
    else:
        print("Nincs találat")


def main():
    print(kutyanevek)
    kutyusokSzama()
    print(szamolas("a"))
    print(leghosszabbNev())
    kereses("odr")


main()