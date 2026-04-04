import math

class Szakasz:
    def __init__(self, szakasz, utvonal, tavolsag, szint, ido):
        self.szakasz = int(szakasz)
        self.utvonal = str(utvonal)
        self.tavolsag = float(tavolsag.replace(",", "."))
        self.szint = float(szint)
        self.ido = float(ido)

    def __str__(self):
        return f"Szakasz {self.szakasz}: {self.utvonal}, {self.tavolsag} km, {self.szint} m szintkülönbség, {self.ido} óra"

def beolvasas():
    global szakaszok
    with open("kekforras.txt", "r") as f:
        szakaszok = []
        f.readline()
        for line in f:
            lineee = line.strip().split("\t")
            szakaszok.append(Szakasz(*lineee))

def kiiratas():
    for szakasz in szakaszok:
        print(szakasz)

def hossz():
    length = len(szakaszok)
    print(f"{length} útvonal adatait találtam meg")

def atlag_szint():
    atlag = sum(szakasz.szint for szakasz in szakaszok) / len(szakaszok)
    print(f"Az átlagos szintkülönbség: {atlag:.2f} m")

def teljesIdoOraPerc():
    total_time = sum(szakasz.ido for szakasz in szakaszok)
    hours = int(total_time // 60)
    minutes = int(total_time - hours*60)
    print(f"A túra megtételéhez {hours} óra és {minutes} perc szükséges.")

def legkisebbAtlagsebesseguUtvonal():

    min_szakasz = min(szakaszok, key=lambda sz: sz.tavolsag / sz.ido)
    print(f"A legkisebb átlagsebességű útvonal: {min_szakasz.utvonal}")

def bekeres():
    telepules = input("Adjon meg egy települést: ").strip()
    talalatok = []
    print(f"\n{telepules} útvonalai:\n")
    for i in szakaszok:
        if telepules in i.utvonal:
        for szakasz in talalatok:
            print(f"{szakasz.szakasz} {szakasz.utvonal} {szakasz.tavolsag} {int(szakasz.szint)} {int(szakasz.ido)}")
        else:
            print("Nincs ilyen útvonal.")

def main():
    beolvasas()
    kiiratas()  
    hossz()
    atlag_szint()
    teljesIdoOraPerc()
    legkisebbAtlagsebesseguUtvonal()
    bekeres()

main()
