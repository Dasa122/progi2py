from random import uniform

verseny_idok = []


def gyorsasag():
	global verseny_idok
	verseny_idok = [round(uniform(14, 26), 2) for _ in range(12)]


def legnagyobbsebesseg():
	leggyorsabb_ido = min(verseny_idok)
	return 1500 / (leggyorsabb_ido * 60)


gyorsasag()

print("2.1. feladat")
print(*verseny_idok, sep="\t")

print("2.2. feladat")
print(f"A leggyorsabb vitorlás sebessége: {legnagyobbsebesseg():.2f} m/s")

print("2.3. feladat")
maradek = verseny_idok[:]
for helyezes in range(1, 4):
	legkisebb = min(maradek)
	sorszam = maradek.index(legkisebb) + 1
	print(f"{helyezes} helyezett: {sorszam} hajó")
	maradek[sorszam - 1] = 100
