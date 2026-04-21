import random
etelek = []
def beolvasas():
    with open("feladat2_forras.txt", "r", encoding="UTF-8") as f:
        for i in f:
            etelek.append(i.strip())

def dbetel():
    print("2. feladat")
    print(f"2.2 A menüben {len(etelek)} darab étel szerepel.")

def hanyadik():
    sorszam = int(input("2.3 Hányadik ételre kíváncsi az étlapon? "))
    print(etelek[sorszam-1])

def napiajanlat():
    print(f"2.4 A nap ajanlata: {random.choice(etelek)}")

def kereses():
    talalat = False
    keresett = input("2.5 Adja meg a keresett étel pontos nevét! ")
    for i in etelek:
        if keresett == i:
            talalat = True
    if talalat:
        print("Az etel szerepel az elapon!")
    else:
        print("Az etel nem szerepel az etlapon!")

    

def main():
    beolvasas()
    dbetel()
    hanyadik()
    napiajanlat()
    kereses()

main()