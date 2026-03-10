class Gyanusitottak:
    def __init__(self, id, nev, kor, foglalkozas, lakhely):
        self.id = id
        self.nev = nev
        self.kor = kor
        self.foglalkozas = foglalkozas
        self.lakhely = lakhely

    def __str__(self):
        return f"{self.sorszam};{self.nev};{self.kor};{self.foglalkozas};{self.lakhely}"
    
class Helyszin_log:
    def __init__(self, nev, helyszin, ido):
        self.nev = nev
        self.helyszin = helyszin
        self.ido = ido

    def __str__(self):
        return f"{self.id};{self.helyszin};{self.datum}"

gyanusitottak= []
helyszinek = []

def beolvasas():
    with open("gyanusitottak.txt", "r", encoding="utf-8") as f:
        f.readline()
        for i in f:
            gyanusitottak.append(Gyanusitottak(*i.strip().split(";")))
        f.close()

def gyanusitottak_szama():
    print(f"1. feladat: Gyanúsítottak száma: {len(gyanusitottak)} fő")

def helyszin_log():
    with open("helyszin_log.txt", "r", encoding="utf-8") as f:
        for i in f:
            helyszinek.append(Helyszin_log(*i.strip().split(";")))
        f.close()

def bizonyitek():
    global buntett_helyszin, buntett_ido, foglalkozas, kamera_nem_lathatja, telefon_helyszin
    with open("bizonyitek.txt", "r", encoding="utf-8") as f:
        for i in f:
            if "buntett_helyszin" in i:    
                if "!=" in i:
                    buntett_helyszin = f"!{i.strip().split('!=')[1]}"
                else:
                    buntett_helyszin = i.strip().split("=")[1]
            elif "buntett_ido" in i:    
                if "!=" in i:
                    buntett_ido = f"!{i.strip().split('!=')[1]}"
                else:
                    buntett_ido = i.strip().split("=")[1]
            elif "foglalkozas" in i:    
                if "!=" in i:
                    foglalkozas = f"!{i.strip().split('!=')[1]}"
                else:
                    foglalkozas = i.strip().split("=")[1]
            elif "kamera_nem_lathatja" in i:    
                if "!=" in i:
                    kamera_nem_lathatja = not bool(i.strip().split('!=')[1])
                else:
                    kamera_nem_lathatja = bool(i.strip().split("=")[1])
            elif "telefon_helyszin" in i:    
                if "!=" in i:
                    telefon_helyszin = f"!{i.strip().split('!=')[1]}"
                else:
                    telefon_helyszin = i.strip().split("=")[1]

        f.close()

def szures():
    talalat = None
    gyanusitottak_szurt = []
    
    for gyanus in gyanusitottak:
        if foglalkozas.startswith("!"):
            if gyanus.foglalkozas != foglalkozas[1:]:
                gyanusitottak_szurt.append(gyanus)
        else:
            if gyanus.foglalkozas == foglalkozas:
                gyanusitottak_szurt.append(gyanus)
    
    with open("kamera.txt", "r", encoding="utf-8") as f:
        kameran_lathato = []
        for sor in f:
            adatok = sor.strip().split(";")
            if len(adatok) >= 3 and adatok[1] == "plaza" and adatok[2] == "21:15":
                kameran_lathato.append(adatok[0])
    
    gyanusitottak_szurt2 = []
    for gyanus in gyanusitottak_szurt:
        if gyanus.nev not in kameran_lathato:
            gyanusitottak_szurt2.append(gyanus)
    
    with open("telefon.txt", "r", encoding="utf-8") as f:
        telefonon_plaza = []
        for sor in f:
            adatok = sor.strip().split(";")
            if len(adatok) >= 3 and adatok[1] == "plaza" and adatok[2] == "21:15":
                telefonon_plaza.append(adatok[0])
    
    gyanusitottak_szurt3 = []
    for gyanus in gyanusitottak_szurt2:
        if gyanus.nev in telefonon_plaza:
            gyanusitottak_szurt3.append(gyanus)
    
    if len(gyanusitottak_szurt3) > 0:
        talalat = gyanusitottak_szurt3[0]
                
    
    if talalat:
        return f"A tettes neve: {talalat.nev}"
    else:
        return "Nem találtunk tettest"

def main():    
    beolvasas()
    gyanusitottak_szama()
    helyszin_log()
    bizonyitek()
    print(szures())

main()