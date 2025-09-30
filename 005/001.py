from prettytable import PrettyTable
table = PrettyTable()

A = True
B = not A
print(A)

print(f"\tA\t|\tB\t|\tA and B\t")
print("------------------------------------------------")
print(f"\t{A}\t|\t{B}\t|\t{A and B}\t")
A = True
print(f"\t{A}\t|\t{B}\t|\t{A and B}\t")
A = False
B = True
print(f"\t{A}\t|\t{B}\t|\t{A and B}\t")
A = True
print(f"\t{A}\t|\t{B}\t|\t{A and B}\t")

A = True
B = not A

table.field_names = ["A", "B", "A and B"]
table.add_row([A, B, A and B])
A = True
table.add_row([A, B, A and B])
A = False
B = True
table.add_row([A, B, A and B])
A = True
table.add_row([A, B, A and B])
print(table)

egyikSzam = int(input("Add meg az első számot: "))
masikSzam = int(input("Add meg a második számot: "))

b = egyikSzam > 0 and masikSzam > 0
print("Mindkét szám pozitív:", b)

igazE = egyikSzam < 4 and masikSzam != 6
print("Az első szám kisebb mint 4 és a második nem 6:", igazE)

barmelyikNulla = egyikSzam == 0 or masikSzam == 0
print("Bármelyik szám nulla:", barmelyikNulla)

elso5masiknem4 = egyikSzam == 5 or masikSzam != 4
print("Az első szám 5 vagy a második nem 4:", elso5masiknem4)

elsoNemNagyobb5MasikNemKisebb13 = egyikSzam <= 5 or masikSzam >= 13
print("Az első szám nem nagyobb 5-nél vagy a másik nem kisebb 13-nál:", elsoNemNagyobb5MasikNemKisebb13)

egyikPozitivMasikNegativ = (egyikSzam > 0 and masikSzam < 0) or (egyikSzam < 0 and masikSzam > 0)
print("Az egyik szám pozitív, a másik negatív:", egyikPozitivMasikNegativ)


szam = int(input("Adj meg egy egész számot: "))
maradek = szam % 10
print("A szám 10-zel vett osztási maradéka:", maradek)
if maradek == 0:
    print("A szám osztható 10-zel.")
    
    
    
szamlalo = int(input("Add meg a tört számlálóját: "))
nevezo = int(input("Add meg a tört nevezőjét: "))
if nevezo == 0:
    print("Hiba: a nevező nem lehet nulla!")
if nevezo != 0:
    print(f"A tört: {szamlalo}/{nevezo}")


szam = int(input("Adj meg egy háromjegyű pozitív egész számot: "))
if 100 <= szam <= 999:
    szazas = szam // 100
    tizes = (szam // 10) % 10
    egyes = szam % 10
    osszeg = szazas**3 + tizes**3 + egyes**3
    if osszeg == szam:
        print(f"{szam} Armstrong szám.")
    if osszeg != szam:
        print(f"{szam} nem Armstrong szám.")
if not (100 <= szam <= 999):
    print("Nem háromjegyű pozitív egész számot adtál meg.")
        
        
szam = int(input("Adj meg egy egész számot: "))

if szam == 4:
    print("A megadott szám a 4-es.")
if szam < 10:
    print("A megadott szám kisebb mint 10.")
if szam % 2 == 0:
    print("A megadott szám páros.")
if 0 <= szam <= 10:
    print("A megadott szám a [0,10] intervallumba esik.")
if szam % 3 == 0 and szam % 5 == 0:
    print("A megadott szám osztható 3-mal és 5-tel is.")
if not (10 <= szam <= 20):
    print("A megadott szám nem a [10,20] intervallumba esik.")
  
  
  
    
elso = int(input("Adj meg egy egész számot: "))
masodik = int(input("Adj meg még egy egész számot: "))

if elso == masodik:
    print("A két szám egyenlő.")

if elso % 2 != 0 and masodik % 2 != 0:
    print("Mind a két szám páratlan.")

if elso % 3 == 0 or masodik % 3 == 0:
    print("Legalább az egyik szám osztható hárommal.")

if elso < 0 and masodik < 0:
    print("Mind a két szám negatív.")

if (elso < 0 and masodik > 0) or (elso > 0 and masodik < 0):
    print("Az egyik szám negatív, a másik szám pozitív.")