import random
def feladat01(meret:str, diszek:int):
    meret = meret.upper().strip()   
    if meret == "KICSI":
        if diszek > 3:
            print("eleg")
        else:
            print("nem eleg")
    elif meret == "KOZEPES":
        if diszek > 5:
            print("eleg")
        else:
            print("nem eleg")
    elif meret == "NAGY":
        if diszek > 8:
            print("eleg")
        else:
            print("nem eleg")
    else:
        print("Ismeretlen meret")

def szinvalaszto():
    szinek = ["piros", "kek", "zold", "sarga", "fekete", "feher"]
    Veletlenszin = random.choice(szinek)
    return Veletlenszin


def ruha():
    ruhak = ["polo", "zokni", "polo", "nadrag", "sapka"]
    ruha = random.choice(ruhak)
    return ruha

def kabat(ar:int, mertek:int):
    arok = ar - (ar / 100 * mertek)
    return arok



def main():
    feladat01("kicsi", 4)
    print(szinvalaszto())
    print(ruha())
    print(f"A kabat ara kedvezmennyel: {kabat(20000, 10)} Ft")

main()