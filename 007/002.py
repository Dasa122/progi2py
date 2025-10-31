import random, math

print(random.randint(0, 10))
print(random.randint(10, 15))
print(random.randint(0, 100))
print(random.randint(-100, 100))

for i in range(10):
    print(random.random())

for i in range(4):
    print(random.uniform(10, 30))

tipp = int(input("A tipped Fej vagy írás? (0/1): "))

eredmeny = random.randint(0, 1)
nevek = {0: "fej", 1: "írás"}

print(f"A pénzfeldobás eredménye: {eredmeny} ({nevek[eredmeny]})")

if tipp == eredmeny:
    print("Gratulálok, jól tippeltél!")
else:
    print("Nem sikerült. Legközelebb fog, játssz újra!")

szam = int(input("Adj meg egy számot 1 és 100 között: "))
tens_exact = {
    10: "tíz", 20: "húsz", 30: "harminc", 40: "negyven", 50: "ötven",
    60: "hatvan", 70: "hetven", 80: "nyolcvan", 90: "kilencven", 100: "száz"
}
tens_prefix = {
    1: "tizen", 2: "huszon", 3: "harminc", 4: "negyven", 5: "ötven",
    6: "hatvan", 7: "hetven", 8: "nyolcvan", 9: "kilencven"
}
units = {
    0: "", 1: "egy", 2: "kettő", 3: "három", 4: "négy",
    5: "öt", 6: "hat", 7: "hét", 8: "nyolc", 9: "kilenc"
}

if not (1 <= szam <= 100):
    print("Hiba: a szám legyen 1 és 100 között.")
else:
    if szam % 10 == 0:
        print(tens_exact[szam])
    else:
        t = szam // 10
        o = szam % 10
        if t == 0:
            print(units[o])
        else:
            prefix = tens_prefix[t]
            print(prefix + units[o])


ertek = int(input("Adj meg egy számot: "))

while input() != "0":
    ertek = ertek * ertek
    print(ertek)

s = "alma"
while True:
    word = input("Adj meg egy szót (üres = befejezés): ")
    if word == "":
       break
    s += word
    print(s)
print("Vége a játéknak. Az összefűzött szavak:", s)


bekertKarakter = input("Adj meg egy karaktert: ")
darab = int(input("Hányszor ismételjük meg? "))
for i in range(darab):
    print(bekertKarakter, end="")


x = int(input("Adj meg egy számot: "))
y = int(input("Adj meg egy másik számot: "))
lepeskoz = int(input("Adj meg egy lépésközt: "))

if x > y:
    for i in range(x, y - 1, -lepeskoz):
        print(i, end=" ")
else:
    for i in range(x, y + 1, lepeskoz):
        print(i, end=" ")


for n in range(15, 1000, 15):
    print(n)

ermekkel = int(input("Adj meg egy összeget 1-1000Ft kozott: "))
if not 1 <= ermekkel <= 1000:
    print("Hiba: az összeg legyen 1 és 1000 Ft között.")
else:
    ketszazas = ermekkel // 200
    ketszazas = math.floor(ketszazas)
    szazas = (ermekkel - ketszazas * 200) // 100
    szazas = math.floor(szazas)
    otvenes = (ermekkel - ketszazas * 200 - szazas * 100) // 50
    otvenes = math.floor(otvenes)
    huszas = (ermekkel - ketszazas * 200 - szazas * 100 - otvenes * 50) // 20
    huszas = math.floor(huszas)
    tizes = (ermekkel - ketszazas * 200 - szazas * 100 - otvenes * 50 - huszas * 20) // 10
    tizes = math.floor(tizes)
    otos = (ermekkel - ketszazas * 200 - szazas * 100 - otvenes * 50 - huszas * 20 - tizes * 10) // 5
    otos = math.floor(otos)
    maradek = ermekkel - ketszazas * 200 - szazas * 100 - otvenes * 50 - huszas * 20 - tizes * 10 - otos * 5
    print(f"Az összeg kifizetése: {ermekkel} Ft")
    print(f"200 Ft-os érmék: {ketszazas} db")
    print(f"100 Ft-os érmék: {szazas} db")
    print(f"50 Ft-os érmék: {otvenes} db")
    print(f"20 Ft-os érmék: {huszas} db")
    print(f"10 Ft-os érmék: {tizes} db")
    print(f"5 Ft-os érmék: {otos} db")
    print(f"Maradék: {maradek} Ft")



a1 = float(input("Add meg az első elemet (a1): "))
d = float(input("Add meg a differenciát (d): "))
n = int(input("Add meg az elemszámot (n): "))

if n <= 0:
    print("Hiba: az elemszám pozitív egész legyen.")
else:
    print("Számtani sorozat:", end=" ")
    for i in range(n):
        elem = a1 + i * d
        if elem.is_integer():
            print(int(elem), end=" ")
        else:
            print(elem, end=" ")
    print()

N = int(input("Adj meg egy pozitív egész számot (N): "))
if N <= 0:
    print("Hiba: N pozitív egész legyen.")
else:
    k = (N + 1) // 2  
    osszeg = k * k  
    print(f"A {N}-nél nem nagyobb pozitív páratlan számok összege: {osszeg}")