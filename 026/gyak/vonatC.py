import math
import random


# 1.
class kesesek:
    def __init__(self, keses, ok, db, min, max, atlag):
        self.keses = keses
        self.ok = ok
        self.db = db
        self.min = min
        self.max = max
        self.atlag = atlag

    def __str__(self):
        return f"{self.keses} ;{self.ok} ;{self.db} ;{self.min} ;{self.max} ;{self.atlag}"


# 2.
def beolvas():
    lista = []
    with open("kesesek.csv", encoding="utf-8") as f:
        f.readline() 
        for sor in f:
            sor = sor.strip()
            if not sor:
                continue
            mezok = sor.split(";")
            keses = mezok[0].strip()
            ok = mezok[1].strip()
            db = int(mezok[2].strip())
            mn = int(mezok[3].strip())
            mx = int(mezok[4].strip())
            atlag = float(mezok[5].strip().replace(",", "."))
            lista.append(kesesek(keses, ok, db, mn, mx, atlag))
    return lista


# 3. 
def osszesito(lista):
    ossz_db = sum(k.db for k in lista)
    min_keses = min(k.min for k in lista)
    max_keses = max(k.max for k in lista)
    print(f"Az adatok alapján {ossz_db} vonat késett, minimum {min_keses} percet, maximum {max_keses} percet")


# 4.
def vihar_kovetkezmenyek(lista):
    vihar_lista = [k.keses for k in lista if "Vihar" in k.ok]
    print("Vihar miatti következmények: " + ", ".join(vihar_lista))


# 5.
def tajekoztato(lista):
    k = random.choice(lista)
    masodperc = math.ceil(k.atlag * 60 / 10) * 10
    jelentos = "Jelentős probléma." if k.db > 100 else "Nem jelentős probléma."
    print("Tájékoztató:")
    print(f"Következmény: {k.keses}")
    print(f"Időjárási ok: {k.ok}")
    print(f"Késő vonatok száma: {k.db} db; átlagos késés: {masodperc} másodperc")
    print(jelentos)


lista = beolvas()
print("Beolvasás")
osszesito(lista)
vihar_kovetkezmenyek(lista)
tajekoztato(lista)
