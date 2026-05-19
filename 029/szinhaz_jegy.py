hossz = int(input("Add meg az eloadas hosszat percekben!"))
sor = int(input("Add meg, hanyadik sorba szol a jegy (1-20)!"))

if hossz < 120:
	alapar = 4500
else:
	alapar = 6000

vegosszeg = alapar

if sor <= 5:
	vegosszeg += 1500

print(f"Fizetendo vegosszeg: {vegosszeg} Ft")

if vegosszeg > 7000:
	print("Exkluzív páholy jegy!")
else:
	print("Standard jegy.")