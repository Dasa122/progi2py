class horcsog:
    def __init__(self, nev: str, szin: str, eletkor: int, suly: float):
        self.nev = nev
        self.szin = szin
        self.eletkor = eletkor
        self.suly = suly
    def __str__(self):
        return f"horcsog(nev={self.nev}, szin={self.szin}, eletkor={self.eletkor}, suly={self.suly})"
lista = []
def horcsogokLetrehozasa():
    horcsog1 = horcsog("Cirmi", "barna", 2, 0.5)
    horcsog2 = horcsog("Morzsi", "feher", 3, 0.6)
    horcsog3 = horcsog("Bodri", "feher", 1, 0.4)
    horcsog4 = horcsog("Fifi", "fekete", 4, 0.7)
    horcsog5 = horcsog("Lili", "sarga", 2, 0.55)
    lista.append(horcsog1)
    lista.append(horcsog2)
    lista.append(horcsog3)
    lista.append(horcsog4)
    lista.append(horcsog5)

def szinkereso(szin: str):
    talalatok = []
    for horcsog in lista:
        if horcsog.szin.lower() == szin.lower():
            talalatok.append(horcsog)
    return talalatok

def pontoseletkorKeresese(eletkor: int):
    talalatok = []
    for horcsog in lista:
        if horcsog.eletkor == eletkor:
            talalatok.append(horcsog)
    return talalatok

def main():
    szin = input("Add meg a keresett színt: ")
    horcsogokLetrehozasa()
    talalatok = szinkereso(szin)
    print(f"A(z) {szin} színű hörcsögök:")
    for horcsog in talalatok:
        print(horcsog)
    eletkor = int(input("Add meg a keresett életkort: "))
    talalatok = pontoseletkorKeresese(eletkor)
    print(f"A(z) {eletkor} éves hörcsögök:")
    for horcsog in talalatok:
        print(horcsog)

main()