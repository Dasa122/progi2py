hossz = int(input("Előadás hossza percekben: "))
sor = int(input("Hanyadik sorba szol a jegy: "))

if hossz < 120:
    ar = 4500
else:
    ar = 6000

if sor <= 5:
    ar += 1500

print(f"Fizetendo vegosszeg: {ar} Ft")

if ar > 7000:
    print("Exkluzív páholy jegy!")
else:
    print("Standard jegy.")
