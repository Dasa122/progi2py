
nev = str(input("Kérem adja meg a nevét: "))
ev = int(input("Kérem adja meg a születési évét: "))
print(f"Kedves {nev}! {ev} évben születtél!")
kor = 2025 - ev
print(f"Kedves {nev}! {kor} éves vagy!")

##########################

szam1 = int(input("Kérlek add meg az első számot: "))
szam2 = int(input("Kérlek add meg a második számot: "))
print(f"A két szám összege: {szam1 + szam2}")
print(f"A két szám különbsége: {szam1 - szam2}")

###########################

szam = float(input("Kérem adjon meg egy valós számot: "))
print(f"A szam tizszerese: {szam * 10}")

###########################

tavolsag = float(input("Kérlek add meg a megtett távolságot (km): "))
ido = float(input("Kérlek add meg az időt (óra): "))
print(f"Az atlagsebesség: {tavolsag / ido} km/h")

###########################

alap = float(input("Kérem adja meg a háromszög alapját (cm): "))
magassag = float(input("Kérem adja meg a háromszög magasságát (cm): "))
print(f"A háromszög területe: {alap * magassag / 2} cm²")  

###########################

egeszSzam = int(input("Kérem adjon meg egy egész számot: "))
print(f"A szám kétszerese: {egeszSzam * 2}")

###########################

egeszSzam = int(input("Kérem adjon meg egy egész számot: "))
print(f"A szám négyzete: {egeszSzam ** 2}  A szám köbe: {egeszSzam ** 3}")

###########################

fok = float(input("Kérem adja meg a hőmérsékletet Celsius-fokban: "))
print(f"A hőmérséklet Fahrenheit-fokban: {fok * 9/5 + 32}")

###########################

alap = float(input("Kérem adja meg az alapot: "))
kitevő = float(input("Kérem adja meg a kitevőt: "))
print(f"Az eredmény: {alap ** kitevő}")

###########################

szam1 = int(input("Kérem adja meg az első egész számot: "))
szam2 = int(input("Kérem adja meg a második egész számot: "))
eredmeny = szam1 * 2 + szam2 / 2
print(f"Az eredmény: {eredmeny}")

############################

tavolsag = float(input("Kérem adja meg a távolságot kilométerben (pozitív szám): "))
fogyasztas = float(input("Kérem adja meg a fogyasztást liter/km-ben (pozitív szám): "))
uzemanyag_szukseglet = tavolsag * fogyasztas
print(f"A szükséges üzemanyag: {uzemanyag_szukseglet} liter")

############################

oradij = float(input("Kérem adja meg az óradíjat (pozitív szám): "))
munkaido = float(input("Kérem adja meg a munkaidőt órában (pozitív szám): "))
fizetes = oradij * munkaido
print(f"A fizetés összege: {fizetes} Ft")

############################

korSugar = float(input("Kérem adja meg a kör sugarát (pozitív szám): "))
kerulet = 2 * 3.14 * korSugar
terulet = 3.14 * korSugar ** 2
print(f"A kör kerülete: {kerulet} cm, területe: {terulet} cm²")

############################

eletkor = int(input("Kérem adja meg az életkorát (pozitív egész szám): "))
atlagos_alvas = float(input("Kérem adja meg az átlagos napi alvásszükségletét órában (pozitív szám): "))
alvas_havonta = atlagos_alvas * 30
print(f"Átlagosan {alvas_havonta} órát tölt álomban havonta.")

############################

nev = str(input("Kérem adjon meg egy nevet: "))
gyujt = str(input("Kérem adjon meg hogy mire gyűjt: "))
ar = float(input("Kérem adja meg a gyűjtés célárát (pozitív szám): "))
hetiZsebpenz = int(input("Kérem adja meg a heti zsebpénzét (pozitív szám): ")) 
hetiKiadas = int(input("Kérem adja meg a heti kiadását (pozitív szám): "))
print(f"{nev} {gyujt}-ra gyűjt. A célár {ar} Ft. Heti zsebpénze {hetiZsebpenz} Ft, heti kiadása {hetiKiadas} Ft. Es a targy {ar / (hetiZsebpenz - hetiKiadas)} het mulva lessz meg.")

############################

magassag_cm = int(input("Kérem adja meg a magasságát (cm): "))
testsuly_kg = int(input("Kérem adja meg a testsúlyát (kg): "))
magassag_m = magassag_cm / 100
bmi = testsuly_kg / (magassag_m ** 2)
print(f"A testtömegindexe (BMI): {bmi}")

############################

alomsuly = float(input("Kérem adja meg az álomsúlyt (kg): "))
fogyas = (testsuly_kg - alomsuly) / 350
print(f"1. hét végére elérendő súly: {testsuly_kg - fogyas * 1} kg\n"
    f"2. hét végére elérendő súly: {testsuly_kg - fogyas * 2} kg\n"
    f"3. hét végére elérendő súly: {testsuly_kg - fogyas * 3} kg")

############################


eletkor = int(input("Kérem adja meg az életkorát (pozitív egész szám): "))
szuletesi_ev = int(input("Kérem adja meg a születési évét (pozitív egész szám): "))
szemuvegKeret = float(input("Kérem adja meg a szemüveg keret árát (Ft): "))
lencseAr = float(input("Kérem adja meg a lencse árát (Ft): "))
osszesen = szemuvegKeret + lencseAr
print(f"""Ön a szemüvegkeret árából, ami {szemuvegKeret} Ft, {eletkor}% kedvezményt kap! Ami {szemuvegKeret * (eletkor / 100)} Ft kedvezményt jelent.
A szemüveglencse ára: {lencseAr} Ft
----------------------------
Szemüvege vételára: {(szemuvegKeret * (1 - eletkor / 100)) + lencseAr} Ft""")