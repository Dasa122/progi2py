class ExportAdat:
    def __init__(self, halfajta, ev, mennyiseg, egysegar) -> None:
        self.halfajta = halfajta
        self.ev = int(ev)
        self.mennyiseg = int(mennyiseg)
        self.egysegar = float(egysegar)


    def __str__(self) -> str:
        return f"{self.halfajta} ({self.ev}): {self.mennyiseg} kg, {self.egysegar} EUR/kg"

halak = []



def beolvasas():
    with open("halak.txt", "r", encoding="UTF-8") as f:
        f.readline()
        for i in f:
            temp = i.strip().split(";")
            halak.append(ExportAdat(*temp))
            
def hossz():
    print("1. feladat: ")
    print(f"Az adatok száma: {len(halak)}")

def analitic():
    found = []
    total = 0.0
    evben = int(input("Kérek egy évet: "))
    for i in halak:
        if i.ev == evben:
            found.append(i)
    for item in found:
        total += item.mennyiseg * item.egysegar
    print(f"Az adott év teljes bevétele: {total} €")

def halfajtak():
    global halakfajtak
    print(" 3. feladat: ")
    halakfajtak = []
    for i in halak:
        if i.halfajta not in halakfajtak:
            halakfajtak.append(i.halfajta)
    print(*halakfajtak, sep=", ")

def export():
    print("4. feladat: ")
    for i in halakfajtak:
        total = 0
        for s in halak:
            if s.halfajta == i:
                total += s.mennyiseg
        print(f" {i}: {total} kg")

def nagyobb_export():
    print("5. feladat: ")
    evek = {}
    for fish in halak:
        if fish.ev not in evek:
            evek[fish.ev] = 0
        evek[fish.ev] += fish.mennyiseg
    
    max_ev = max(evek, key=evek.get) # pyright: ignore[reportCallIssue, reportArgumentType]
    print(f"A legnagyobb exportmennyiség éve: {max_ev}")


def main():
    beolvasas()
    hossz()
    analitic()
    halfajtak()
    export()
    nagyobb_export()

main()