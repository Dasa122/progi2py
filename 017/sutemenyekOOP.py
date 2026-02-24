class Suti:
    def __init__(self, nev: str, iz: str, forma: str, ar: int, kaloria: int):
        self.nev = nev
        self.iz = iz
        self.forma = forma
        self.ar = ar
        self.kaloria = kaloria

    def __str__(self):
        return f"Suti(nev={self.nev}, iz={self.iz}, forma={self.forma}, ar={self.ar}, kaloria={self.kaloria})"
    
lista = []
def sutikLetrehozasa():
    suti1 = Suti("csokitorta", "csoki", "kerek", 500, 300)
    suti2 = Suti("epresalom", "eper", "szivecskes", 600, 250)
    suti3 = Suti("vaniliáslet", "vanilia", "negyzet", 450, 200)
    lista.append(suti1)
    lista.append(suti2)
    lista.append(suti3)
    suti4 = Suti("diós", "dió", "kerek", 550, 280)
    lista.append(suti4)

def csokisutiKeresese():
    csokissutik = []
    for suti in lista:
        if suti.iz.lower() == "csoki":
            csokissutik.append(suti)
        print(suti)

def kiiratas():
    for suti in lista:
        print(suti)

def osszAr():
    ossz = 0
    for suti in lista:
        ossz += suti.ar
    print(f"A {len(lista)} sutik osszar: {ossz} Ft")


