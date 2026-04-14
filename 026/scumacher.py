class Versenyzo:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.date = adatok[0]
        self.grandprix = adatok[1]
        self.pos = adatok[2]
        self.lap = adatok[3]
        self.point = adatok[4]
        self.team = adatok[5]
        self.status = adatok[6]

versenyzok = []

def beolvas():
    with open("schumacher.csv", "r", encoding="utf-8") as f:
        f.readline()
        for sor in f:
            versenyzok.append(Versenyzo(sor))

def versenyzo_szama():
    print(f"3. feladat: {len(versenyzok)}")

def magyar_nagydij():
    print("4. feladat: Magyar Nagydíj helyezései")
    for v in versenyzok:
        if v.grandprix == "Hungarian Grand Prix" and v.pos != "0":
            ev, ho, nap = v.date.split("-")
            print(f"\t{ev}. {ho}. {nap}.: {v.pos}. hely")

def hibastatisztika():
    print("5. feladat: Hibastatisztika")
    hibak = {}
    for i in versenyzok:
        if i.status != "Finished" and not i.status.startswith("+"):
            hibak[i.status] = hibak.get(i.status, 0) + 1
    for hiba, db in hibak.items():
        if db > 2:
            print(f"\t{hiba}: {db}")

def main():
    beolvas()
    versenyzo_szama()
    magyar_nagydij()
    hibastatisztika()

main()
