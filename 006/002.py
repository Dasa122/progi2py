import math
#ez a feladat mar volt

################################################

a = float(input("Add meg a háromszög első oldalát: "))
b = float(input("Add meg a háromszög második oldalát: "))
c = float(input("Add meg a háromszög harmadik oldalát: "))

if a == b == c:
    print("Szabályos háromszög.")
else:
    print("Nem szabályos háromszög.")
    
################################################

num = int(input("Adj meg egy egész számot: "))

if num == 10:
    print("A szám egyenlő 10-zel.")
elif num == 100:
    print("A szám egyenlő 100-zal.")
elif num == 1000:
    print("A szám egyenlő 1000-rel.")
else:
    print("A szám nem egyenlő 10-zel, 100-zal vagy 1000-rel.")
    
################################################

szam = float(input("Adj meg egy számot: "))

if 1 <= szam <= 9:
    print("A szám benne van az [1,9] intervallumban.")
else:
    print("A szám nincs benne az [1,9] intervallumban.")
    
################################################

szam = int(input("Adj meg egy egész számot: "))

if szam < 0 and szam % 2 != 0:
    print("A szám negatív páratlan szám.")
else:
    print("A szám nem negatív páratlan szám.")
    
################################################

elso = int(input("Add meg az első egész számot: "))
masodik = int(input("Add meg a második egész számot: "))

if masodik % elso == 0:
    print("Az első szám osztója a második számnak.")
else:
    print("Az első szám nem osztója a második számnak.")
    
################################################

szam = int(input("Adj meg egy egész számot: "))
if szam >= 0:
    gyok = math.sqrt(szam)
    print(f"A szám négyzetgyöke: {gyok}")
else:
    print("Negatív számnak nincs valós négyzetgyöke.")
    
################################################

#volt mar ez a feladat

################################################

tav = float(input("Add meg, hány km-t tett meg: "))
ido = float(input("Add meg, mennyi idő alatt (órában): "))

if ido > 0:
    atlag_sebesseg = tav / ido
    if atlag_sebesseg > 145 or atlag_sebesseg < 80:
        print("Nem megfelelő sebességgel közlekedett!")
    else:
        print("Minden rendben!")
else:
    print("Az időnek pozitívnak kell lennie!")

################################################

#mar volt a feladat

################################################

x = float(input("Add meg az első számot: "))
y = float(input("Add meg a második számot: "))

if x > y:
    print("Az első szám nagyobb a másodiknál.")
elif x < y:
    print("Az első szám kisebb a másodiknál.")
else:
    print("A két szám egyenlő.")
    
################################################

#volt mar ez a feladat

################################################

x = float(input("Add meg az x koordinátát: "))
y = float(input("Add meg az y koordinátát: "))

if x > 0 and y > 0:
    print("Első síknegyedben van.")
elif x < 0 and y > 0:
    print("Második síknegyedben van.")
elif x < 0 and y < 0:
    print("Harmadik síknegyedben van.")
elif x > 0 and y < 0:
    print("Negyedik síknegyedben van.")
elif x == 0 and y == 0:
    print("A pont az origóban van.")
elif x == 0:
    print("A pont az y tengelyen van.")
elif y == 0:
    print("A pont az x tengelyen van.")
    
################################################

#volt mar ez a feladat

################################################

eletkor = int(input("Add meg az életkorodat (nemnegatív egész szám): "))

if 0 <= eletkor <= 13:
    print("Gyerek")
elif 14 <= eletkor <= 17:
    print("Fiatalkorú")
elif 18 <= eletkor <= 23:
    print("Ifjú")
elif 24 <= eletkor <= 59:
    print("Felnőtt")
elif eletkor >= 60:
    print("Idős")
else:
    print("Az életkor nem lehet negatív!")
    
################################################

targy_suruseg = float(input("Add meg a tárgy sűrűségét (kg/m^3): "))
folyadek_suruseg = float(input("Add meg a folyadék sűrűségét (kg/m^3): "))

if targy_suruseg > folyadek_suruseg:
    print("A tárgy elmerül.")
elif targy_suruseg < folyadek_suruseg:
    print("A tárgy úszik.")
else:
    print("A tárgy lebeg.")
    
################################################

hianyzas = int(input("Add meg az igazolatlan hiányzások számát: "))

if hianyzas == 0:
    print("Magatartás jegy: 5")
elif 1 <= hianyzas <= 3:
    print("Magatartás jegy: 4")
elif 4 <= hianyzas <= 9:
    print("Magatartás jegy: 3")
else:
    print("Magatartás jegy: 2")
    szuletesi_ev = int(input("Add meg a tanuló születési évét: "))
    aktualis_ev = 2024
    eletkor = aktualis_ev - szuletesi_ev
    if eletkor < 18:
        print("szülői értesítés szükséges")
    else:
        print("felszólítás kiküldése szükséges")
        
################################################

karakter = input("Adj meg egy karaktert: ")

if len(karakter) != 1:
    print("Csak egy karaktert adj meg!")
else:
    kod = ord(karakter)
    print(f"A karakter ASCII kódja: {kod}")
    if 48 <= kod <= 57:
        print("A karakter szám.")
    elif 65 <= kod <= 90:
        print("A karakter nagybetű.")
    elif 97 <= kod <= 122:
        print("A karakter kisbetű.")
    else:
        print("A karakter egyéb.")
        
################################################

sebesseg = float(input("Add meg az autó sebességét km/h-ban: "))

if 0 <= sebesseg <= 1:
    print("A sebesség egy csiga sebességéhez hasonlítható.")
elif 1 < sebesseg <= 6:
    print("A sebesség egy csuka sebességéhez hasonlítható.")
elif 7 <= sebesseg <= 32:
    print("A sebesség egy bálna sebességéhez hasonlítható.")
elif 32 < sebesseg <= 48:
    print("A sebesség egy ezüst sirály sebességéhez hasonlítható.")
elif 48 < sebesseg <= 64:
    print("A sebesség egy nyúl sebességéhez hasonlítható.")
elif 65 <= sebesseg <= 70:
    print("A sebesség egy strucc sebességéhez hasonlítható.")
elif 71 <= sebesseg <= 110:
    print("A sebesség egy gepárd sebességéhez hasonlítható.")
elif 111 <= sebesseg <= 320:
    print("A sebesség egy vadászsólyom (zuhanórepülésben) sebességéhez hasonlítható.")
else:
    print("A sebesség egyik állathoz sem hasonlítható.")
    
################################################

tavolsag = float(input("Add meg a megtett távolságot (km): "))

if 1 <= tavolsag <= 2:
    print("Díjazás: 500 Ft")
elif 3 <= tavolsag <= 5:
    print("Díjazás: 700 Ft")
elif 6 <= tavolsag <= 10:
    print("Díjazás: 900 Ft")
elif 11 <= tavolsag <= 20:
    print("Díjazás: 1 400 Ft")
elif 21 <= tavolsag <= 30:
    print("Díjazás: 2 000 Ft")
else:
    print("Erre a távolságra nincs díjazás megadva.")
    
################################################

szelesseg = float(input("Add meg a telek szélességét (m): "))
hosszusag = float(input("Add meg a telek hosszúságát (m): "))
ado = float(input("Add meg a helyi telek adót (Ft): "))

if szelesseg <= 15 or hosszusag <= 25:
    ado_kedvezmeny = ado * 0.2
    korrigalt_ado = ado - ado_kedvezmeny
    print(f"Az adó kedvezménnyel: {korrigalt_ado} Ft")
else:
    print(f"Az adó kedvezmény nélkül: {ado} Ft")
    
################################################

ev = int(input("Add meg az évszámot (1800-2099): "))

if 1800 <= ev <= 2099:
    A = ev % 19
    B = ev % 4
    C = ev % 7
    D = (19 * A + 24) % 30
    E = (2 * B + 4 * C + 6 * D + 5) % 7
    # Kivétel vizsgálata
    if E == 6 and D == 29:
        nap = 50
    elif E == 6 and D == 28 and A > 10:
        nap = 49
    else:
        nap = 22 + D + E
    if nap <= 31:
        print(f"Húsvét dátuma: március {nap}.")
    else:
        print(f"Húsvét dátuma: április {nap - 31}.")
else:
    print("Az évszámnak 1800 és 2099 között kell lennie.")
    
################################################

# volt mar ez a feladat

#################################################

nap_szam = int(input("Add meg a hét napját (1-7): "))

if nap_szam == 1:
    print("A hét 1. napja: Hétfő")
elif nap_szam == 2:
    print("A hét 2. napja: Kedd")
elif nap_szam == 3:
    print("A hét 3. napja: Szerda")
elif nap_szam == 4:
    print("A hét 4. napja: Csütörtök")
elif nap_szam == 5:
    print("A hét 5. napja: Péntek")
elif nap_szam == 6:
    print("A hét 6. napja: Szombat")
elif nap_szam == 7:
    print("A hét 7. napja: Vasárnap")
else:
    print("Csak 1 és 7 közötti számot adj meg!")
    
#################################################

ev = int(input("Add meg az évet: "))
honap = int(input("Add meg a hónapot (1-12): "))
nap = int(input("Add meg a napot: "))

if 1 <= honap <= 12:
    if honap == 1:
        honap_nev = "január"
    elif honap == 2:
        honap_nev = "február"
    elif honap == 3:
        honap_nev = "március"
    elif honap == 4:
        honap_nev = "április"
    elif honap == 5:
        honap_nev = "május"
    elif honap == 6:
        honap_nev = "június"
    elif honap == 7:
        honap_nev = "július"
    elif honap == 8:
        honap_nev = "augusztus"
    elif honap == 9:
        honap_nev = "szeptember"
    elif honap == 10:
        honap_nev = "október"
    elif honap == 11:
        honap_nev = "november"
    else:
        honap_nev = "december"
    print(f"A megadott dátum: {ev}. {honap_nev} {nap}.")
else:
    print("Hibás hónap érték!")
    
#################################################

dobas = int(input("Dobd a kockát (1-6): "))
print(f"A dobás értéke: {dobas}")

if 1 <= dobas <= 2:
    print("Gyenge!")
elif 3 <= dobas <= 4:
    print("Nem rossz!")
elif dobas == 5:
    print("Jó!")
else:
    print("Kiváló!")
