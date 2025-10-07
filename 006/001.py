import math

szam = 5
if szam > 5:
    # akkor fut le ha true a feltétel
    print(f"A {szam} nagyobb mint 5.")
else:
    # akkor fut le ha false a feltétel
    print(f"A {szam} kissebb mint 5.")
    
##########################################################################

tipp = int(input("Adj meg egy számot 1 es 10 között: "))
szam = 5
if szam == tipp:
    print("eltalaltad a szamot")
else:
    print("nem talaltad el a szamot")

##########################################################################

szam = int(input("Adj meg egy egész számot: "))
if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")

###########################################################################

homerseklet = int(input("Adj meg egy hőmérsékletet Celsiusban: "))
if homerseklet < 10:
    print("Hideg az idő.")
elif homerseklet <= 25:
    print("Kellemes az idő.")
else:
    print("Meleg az idő.")
    
###########################################################################

a = int(input("Add meg az első oldal hosszát: "))
b = int(input("Add meg a második oldal hosszát: "))
c = int(input("Add meg a harmadik oldal hosszát: "))

if a + b > c and a + c > b and b + c > a:
    print("A megadott oldalak alkothatnak háromszöget.")
else:
    print("A megadott oldalak nem alkothatnak háromszöget.")
    
###########################################################################

szam = int(input("Adj meg egy számot: "))
if szam >= 0:
    print(f"A(z) {szam} négyzetgyöke: {math.sqrt(szam)}")
else:
    print("Negatív számnak nincs valós négyzetgyöke.")
    
###########################################################################

jegy = int(input("Adj meg egy jegyet (1-5): "))
if jegy == 1:
    print("Elégtelen")
elif jegy == 2:
    print("Elégséges")
elif jegy == 3:
    print("Közepes")
elif jegy == 4:
    print("Jó")
elif jegy == 5:
    print("Jeles")
else:
    print("Érvénytelen jegy")

###########################################################################

szam = int(input("Adj meg egy számot: "))
if szam > 0:
    print("A szám pozitív.")
elif szam < 0:
    print("A szám negatív.")
else:
    print("A szám nulla.")
    
###########################################################################

honap = int(input("Adj meg egy hónap számát (1-12): "))
if honap == 1 or honap == 3 or honap == 5 or honap == 7 or honap == 8 or honap == 10 or honap == 12:
    print("31 napos hónap.")
elif honap == 4 or honap == 6 or honap == 9 or honap == 11:
    print("30 napos hónap.")
elif honap == 2:
    print("28 vagy 29 napos hónap.")
else:
    print("Érvénytelen hónap szám.")
    
###########################################################################

szam = int(input("Adj meg egy számot: "))
if szam % 3 == 0 and szam % 5 == 0:
    print("A szám osztható 3-mal és 5-tel is.")
elif szam % 3 == 0:
    print("A szám osztható 3-mal.")
elif szam % 5 == 0:
    print("A szám osztható 5-tel.")
else:
    print("A szám nem osztható sem 3-mal, sem 5-tel.")

###########################################################################

    eletkor = int(input("Add meg az életkorodat: "))
    if eletkor < 7:
        print("Kisgyermek")
    elif eletkor < 18:
        print("Gyermek")
    elif eletkor < 65:
        print("Felnőtt")
    else:
        print("Nyugdíjas")
        
        
###########################################################################

szam1 = int(input("Add meg az első számot: "))
szam2 = int(input("Add meg a második számot: "))
szam3 = int(input("Add meg a harmadik számot: "))
szam4 = int(input("Add meg a negyedik számot: "))

legnagyobb = szam1
if szam2 > legnagyobb:
    legnagyobb = szam2
if szam3 > legnagyobb:
    legnagyobb = szam3
if szam4 > legnagyobb:
    legnagyobb = szam4

print(f"A legnagyobb szám: {legnagyobb}")

###########################################################################

jelszo = "titkos123"
bekert_jelszo = input("Add meg a jelszót: ")
if bekert_jelszo == jelszo:
    print("Sikeres bejelentkezés.")
else:
    print("Hibás jelszó.")
    
###########################################################################

oldal1 = int(input("Add meg az első oldalt: "))
oldal2 = int(input("Add meg a második oldalt: "))
if oldal1 == oldal2:
    print("Ez egy négyzet.")
else:
    print("Ez egy téglalap.")
    
###########################################################################

pontszam = int(input("Add meg a pontszámot (0-100): "))
if pontszam < 0 or pontszam > 100:
    print("Érvénytelen pontszám.")
elif pontszam < 50:
    print("Elégtelen")
elif pontszam < 60:
    print("Elégséges")
elif pontszam < 70:
    print("Közepes")
elif pontszam < 85:
    print("Jó")
else:
    print("Jeles")
    
    
###########################################################################

irany = input("Adj meg egy irányt (E, D, K, Ny): ")
if irany == "E":
    print("Kelet")
elif irany == "D":
    print("Dél")
elif irany == "K":
    print("Közép")
elif irany == "Ny":
    print("Nyugat")
else:
    print("Ismeretlen irány")
    
###########################################################################

szam = int(input("Adj meg egy egész számot: "))
if szam >= 0:
    print(f"A(z) {szam} négyzetgyöke: {math.sqrt(szam)}")
else:
    print("Negatív számnak nincs valós négyzetgyöke.")
    
###########################################################################

homerseklet = int(input("Adj meg egy hőmérsékletet Celsiusban: "))
if homerseklet <= 0:
    print("A víz szilárd (jég) halmazállapotban van.")
elif homerseklet < 100:
    print("A víz folyékony halmazállapotban van.")
else:
    print("A víz gáz (gőz) halmazállapotban van.")
    
###########################################################################

szam = int(input("Adj meg egy számot: "))
szam = abs(szam)
print(f"A szám abszolút értéke: {szam}")

###########################################################################

szam = int(input("Adj meg egy számot: "))
if -10 < szam < 10:
    print("Egyjegyű szám.")
elif -100 < szam < 100:
    print("Kétjegyű szám.")
else:
    print("Többjegyű szám.")
    
###########################################################################

szam = int(input("Adj meg egy számot: "))
if szam > 0:
    print("A szám pozitív.")
elif szam < 0:
    print("A szám negatív.")
else:
    print("A szám nulla.")

############################################################################

szam = int(input("Adj meg egy számot: "))
if 1 <= szam <= 100:
    print("A szám 1 és 100 között van.")
else:
    print("A szám nincs 1 és 100 között.")