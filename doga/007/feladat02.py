kepregenyek = ["Batman: A gyilkos tréfa", "Spider-Man: Hazatérés", "Watchmen", "Naruto 1.", "OnePiece 1.", "Attack on Titan 4.", "Sandman", "Saga 1.", "Tintin kalandjai", "Asterix ésObelix"]

def kepregenyszam():
    print(f"2.1 A listában {len(kepregenyek)} képregény szerepel.")



def szamokereses():
    talalat = []
    for i in kepregenyek:
        if "1" in i:
            talalat.append(i)
        elif "2" in i:
            talalat.append(i)
        elif "3" in i:
            talalat.append(i)
        elif "4" in i:
            talalat.append(i)
        elif "5" in i:
            talalat.append(i)
        elif "6" in i:
            talalat.append(i)
        elif "7" in i:
            talalat.append(i)
        elif "8" in i:
            talalat.append(i)
        elif "9" in i:
            talalat.append(i)
        elif "0" in i:
            talalat.append(i)
    print("2.2 Számot tartalmazó képregények:")
    print(*talalat, sep="\n")

def reszletkereses():
    szokereses = []
    keresett = input("2.3 Adjon meg egy szót! ")
    for i in kepregenyek:
        if keresett in i:
            szokereses.append(i)
    print(f"2.3 A szó {len(szokereses)} képregény címében szerepel.")

def mincaracter():
    mintk = [] 
    for i in kepregenyek:
        if len(i) >= 12:
            mintk.append(i)
    print("2.4 Legalább 12 karakter hosszú címek: ")
    print(*mintk, sep="\n")

def leghosszabb():
    temp = 0
    longest = ""
    for i in kepregenyek:
        if len(i) > temp:
            longest = i
            temp = len(i)
    print("2.5 A leghosszabb cím:")
    print(longest)

def main():
    print("2. feladat")
    kepregenyszam()
    szamokereses()
    mincaracter()
    leghosszabb()

main()