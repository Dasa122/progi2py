import math
'''
# Bekérjük az adatokat
atmero = float(input("Add meg a medence átmérőjét (méterben): "))
melyseg = float(input("Add meg a medence mélységét (méterben): "))

# Térfogat számítása: V = π * r^2 * h
sugar = atmero / 2
terfogat = math.pi * math.pow(sugar, 2) * melyseg

print(f"A medencébe {terfogat} köbméter víz fér bele.")

##########################

szam = float(input("Adj meg egy pozitív valós számot: "))
also = math.floor(szam)
felso = math.ceil(szam)
kozelebbi = round(szam)
egesz_resz = math.floor(szam)
tort_resz = szam - egesz_resz

print(f"A megadott szám a {also} és a {felso} egész számok között van, és ezek közül a {kozelebbi} számhoz van közelebb.")
print(f"A szám egész része: {egesz_resz}")
print(f"A szám törtrésze: {tort_resz}")

###########################

A = float(input("Add meg az A együtthatót: "))
B = float(input("Add meg a B együtthatót: "))

# Megoldás if nélkül
megoldas = float(-B / A)

print(megoldas)

############################

tank_meret = float(input("Add meg a tank méretét (literben): "))
megtett_km = float(input("Add meg a megtett kilométereket az utolsó tankolás óta: "))

fogyasztas = (tank_meret / megtett_km) * 100

print(f"Az autó átlagfogyasztása: {fogyasztas} liter/100 km")

###########################

ar = float(input("Add meg a krumpli árát (Ft/kg): "))
mennyiseg = float(input("Hány kiló krumplit szeretnél venni? "))
osszeg = ar * mennyiseg
print(f"Ennyi pénzt kell magaddal vinned: {osszeg} Ft")

###########################

fizetes = float(input("Add meg a jelenlegi fizetésedet (Ft): "))
emeles_szazalek = float(input("Add meg a fizetésemelés mértékét (%): "))
uj_fizetes = fizetes * (1 + emeles_szazalek / 100)
print(f"Az emelés utáni fizetésed: {uj_fizetes} Ft")

###########################

havonta_felretett = float(input("Havonta mennyi pénzt tudsz félretenni? (Ft): "))
laptop_ar = float(input("Mennyibe kerül a kiválasztott laptop? (Ft): "))
honapok = math.ceil(laptop_ar / havonta_felretett)
print(f"{honapok} hónapot kell még spórolnod, hogy meg tudd venni a laptopot.")

###########################

kolcson_osszeg = float(input("Add meg a kölcsön összegét (Ft): "))
futamido_ev = float(input("Add meg a futamidőt (években): "))
havi_torleszto = kolcson_osszeg / (futamido_ev * 12)
print(f"A havi törlesztő részlet: {havi_torleszto} Ft")

###########################

szelesseg = float(input("Add meg a terület szélességét (méterben): "))
magassag = float(input("Add meg a terület magasságát (méterben): "))

terulet = szelesseg * magassag
csempe_terulet = 0.2 * 0.2  # 20cm x 20cm = 0.04 m^2

szukseges_csempe = terulet / csempe_terulet
szukseges_csempe = szukseges_csempe * 1.1  # 10% ráhagyás
szukseges_csempe = math.ceil(szukseges_csempe)

print(f"A szükséges csempék száma: {szukseges_csempe} darab")

###########################


print("Első időpont:")
ora1 = int(input("Óra: "))
perc1 = int(input("Perc: "))
mp1 = int(input("Másodperc: "))

print("Második időpont:")
ora2 = int(input("Óra: "))
perc2 = int(input("Perc: "))
mp2 = int(input("Másodperc: "))

elso_masodperc = ora1 * 3600 + perc1 * 60 + mp1
masodik_masodperc = ora2 * 3600 + perc2 * 60 + mp2

kulonbseg = abs(masodik_masodperc - elso_masodperc)
print(f"A két időpont közti különbség: {kulonbseg} másodperc")

###########################

ot_euro = int(input("Hány 5 eurósod van? "))
ketto_euro = int(input("Hány 2 eurósod van? "))
egy_euro = int(input("Hány 1 eurósod van? "))

osszeg = ot_euro * 5 + ketto_euro * 2 + egy_euro * 1
print(f"A teljes összeg: {osszeg} euró")

###########################
'''