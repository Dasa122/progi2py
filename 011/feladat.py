import math


def feladat1(magassag):
    print(f"{math.ceil(magassag/10)}")
    
def feladat2(kapacitas:int, etel:int):
    print(int(kapacitas/etel))

def feladat3(magassag:int, diszek:int):
    print(int(magassag/diszek))

def feladat4(tavolsag:int, homerseklet:int):
    print(tavolsag * 60 * 1.1 if homerseklet < 0 else tavolsag * 60)

def feladat5(homerseklet:int):
    if homerseklet < 0:
        print("Vastag telikabat")
    elif 0 <= homerseklet <= 10:
        print("Belelt kabat")
    else:
        print("Konnyu dzseki")

def feladat6(ero:int, tavolsag:int):
    if ero * 2 >= tavolsag:
        print("igen")
    else:
        print("Nem")
        
def feladat7(emberek:int, etel:int):
    print(int(etel*emberek))
    
def feladat8(meret:str, diszek:int):
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
        
def feladat21(vastagsag:int, temp:int):
    if vastagsag < 5 and temp < 0:
        return "nem csuszos"
    elif 5 <= vastagsag <= 10:
        return "mersekelten csuszos"
    elif vastagsag > 10 and temp < 0:
        return "nagyon csuszos"
    

def feladat22(napok: int, arany: float) -> int:

    if not (0 <= arany <= 100):
        return int(round(napok * arany / 100))
    
def feladat23(egok: int, napi_atlag_orak: float):   
    teljesitmeny_per_ego = 0.05
    napok = 30
    return egok * napi_atlag_orak * napok * teljesitmeny_per_ego

def feladat24(vastagsag: int, szelsebesseg: int) -> int:
    perc = 30
    if vastagsag < 10:
        perc += 10
    if szelsebesseg > 15:
        perc += 5
    return perc

def feladat25(emberek: int, tej_dl: float) -> float:
    return (emberek * tej_dl) / 10.0

def feladat26(jatekos1: int, jatekos2: int) -> str:
    if jatekos1 > jatekos2:
        return "Játékos 1"
    if jatekos2 > jatekos1:
        return "Játékos 2"
    return "Döntetlen"

def feladat27(sebesseg: float, csuszasi_egyutthato: float) -> float:
    if csuszasi_egyutthato == 0:
        return sebesseg * 10.0 / csuszasi_egyutthato
        
def feladat28(vendeg_szam: int, adag_per_vendeg: int) -> int:
    return vendeg_szam * adag_per_vendeg

def feladat29(hom1: float, hom2: float) -> str:
    diff = abs(hom1 - hom2)
    if diff < 5:
        return "Kicsi"
    elif diff <= 10:
        return "Közepes"
    else:
        return "Nagy"
    

    
        

def main():
    #feladat1(102)
    #feladat2(1000, 250)
    #feladat3(150, 20)
    #feladat4(10, 8)
    #feladat5(234)
    feladat8("kicsi", 8)
    print(feladat21(12, -3))
    
main()
    