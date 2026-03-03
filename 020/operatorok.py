class Operatorok:
    def __init__(self, szam, szoveg, szam2):
        self.szam = szam
        self.szoveg = szoveg
        self.szam2 = szam2

statisztika = {"mod": 0, "per": 0, "div": 0, "neg": 0, "multi": 0, "plus": 0}

def beolvasas():
    global operatorok
    with open("kifejezesek.txt", "r", encoding="utf-8") as file:
        operatorok = []
        for i in file:
            parts = i.strip().split(" ")
            operatorok.append(Operatorok(int(parts[0]), parts[1], int(parts[2])))
    file.close()

def hossz():
    print(f"2. feladat: Kifejezesek szama: {len(operatorok)}")

def maradekos():
    szamlalo = 0
    for i in operatorok:
        if i.szoveg == "mod":
            szamlalo += 1
    print(f"3. feladat: Kifejezesek maradekos osztassal: {szamlalo}")

def tizzelOszthato():
    van = False
    szamlalo = 0
    for i in operatorok:
        if i.szam % 10 == 0 and i.szam2 % 10 == 0:
            print(f"4. feladat: Van ilyen kifejezes!", sep="", end="")
            van = True
            break
    if van == False:
        print(f"4. feladat: Nincs ilyen kifejezes!", sep="", end="")  
    
def otfeladat():
    global statisztika
    for i in operatorok:
        if i.szoveg == "mod":
            statisztika["mod"] += 1
        elif i.szoveg == "/":
            statisztika["div"] += 1
        elif i.szoveg == "%":
            statisztika["per"] += 1
        elif i.szoveg == "*":
            statisztika["multi"] += 1
        elif i.szoveg == "+":
            statisztika["plus"] += 1
        elif i.szoveg == "-":
            statisztika["neg"] += 1
    print(f"""
5. feladat: Statisztika:
\tmod: {statisztika["mod"]} db
\t/: {statisztika["per"]} db
\tdiv: {statisztika["div"]} db
\t-: {statisztika["neg"]} db
\t*: {statisztika["multi"]} db
\t+: {statisztika["plus"]} db """)

def szamolas():
    szamolasok = input("6. feladat: Kérek egy kifejezést: ").split(" ")
    i = Operatorok(int(szamolasok[0]), szamolasok[1], int(szamolasok[2]))
    try:
        
        if i.szoveg == "mod":
            print(f"{i.szam} mod {i.szam2} = {i.szam % i.szam2}")
        elif i.szoveg == "/":
            print(f"{i.szam} / {i.szam2} = {i.szam / i.szam2}")
        elif i.szoveg == "div":
            print(f"{i.szam} div {i.szam2} = {i.szam // i.szam2}")
        elif i.szoveg == "*":
            print(f"{i.szam} * {i.szam2} = {i.szam * i.szam2}")
        elif i.szoveg == "+":
            print(f"{i.szam} + {i.szam2} = {i.szam + i.szam2}")
        elif i.szoveg == "-":
            print(f"{i.szam} - {i.szam2} = {i.szam - i.szam2}")
    except ZeroDivisionError:
        print("Egyeb hiba!")
    
    except ValueError:
        print("Egyeb hiba!")


def main():
    beolvasas()
    hossz()
    maradekos()
    tizzelOszthato()
    otfeladat()

main()