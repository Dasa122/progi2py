class Hajo():
	def __init__(self, indulas, erkezes, ido, keses, utasSzam):
		self.indulas = indulas
		self.erkezes = erkezes
		self.ido = ido
		self.keses = keses
		self.utasSzam = utasSzam

	def __str__(self):
		return f"{self.indulas} {self.erkezes} {self.ido} {self.keses} {self.utasSzam} "


def beolvas():
	hajok = []
	with open("menetrend.csv", encoding="utf-8") as fajl:
		sorok = fajl.readlines()

	for sor in sorok[1:]:
		adatok = sor.strip().split(";")
		if len(adatok) == 5:
			hajok.append(Hajo(adatok[0], adatok[1], int(adatok[2]), int(adatok[3]), int(adatok[4])))
	return hajok


def feladat_31():
	print("3.1. feladat:")
	print("A Hajo osztály beillesztése megtörtént.")


def feladat_32():
	hajok = beolvas()
	print("3.2. feladat.")
	print("Az adatok beolvasása sikeresen megtörtént.")
	return hajok


def utasszam_osszesen(hajok):
	osszeg = 0
	for hajo in hajok:
		osszeg += hajo.utasSzam
	return osszeg


def feladat_33(hajok):
	print("3.3. feladat")
	print(f"Az utasszám adott héten: {utasszam_osszesen(hajok)} fő.")


def indulo_telepulesek(hajok):
	telepulesek = []
	for hajo in hajok:
		if hajo.indulas not in telepulesek:
			telepulesek.append(hajo.indulas)
	return telepulesek


def feladat_34(hajok):
	telepulesek = indulo_telepulesek(hajok)
	print("3.4. feladat")
	print(f"{len(telepulesek)} településről indult hajó a héten:")
	for telepules in telepulesek:
		print(f" {telepules}")


def fajlba_iras(hajok):
	with open("adatok.txt", "w", encoding="utf-8") as fajl:
		for hajo in hajok:
			if hajo.keses == 0:
				fajl.write(f"{hajo.indulas} - {hajo.erkezes}\n")


def feladat_35(hajok):
	fajlba_iras(hajok)
	print("3.5. feladat:")
	print("Az adatok.txt sikeresen létrejött a kívánt tartalommal")


def main():
	feladat_31()
	hajok = beolvas()
	feladat_32()
	feladat_33(hajok)
	feladat_34(hajok)
	feladat_35(hajok)


main()