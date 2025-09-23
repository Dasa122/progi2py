import math

nev1 = input("Add meg az első ember nevét: ")
tomeg1 = float(input("Add meg az első ember testtömegét (kg): "))
magassag1 = float(input("Add meg az első ember testmagasságát (m): "))

nev2 = input("Add meg a második ember nevét: ")
tomeg2 = float(input("Add meg a második ember testtömegét (kg): "))
magassag2 = float(input("Add meg a második ember testmagasságát (m): "))

nev3 = input("Add meg a harmadik ember nevét: ")
tomeg3 = float(input("Add meg a harmadik ember testtömegét (kg): "))
magassag3 = float(input("Add meg a harmadik ember testmagasságát (m): "))

atlagmagassag = (magassag1 + magassag2 + magassag3) / 3
print(f"Az átlagmagasság: {round(atlagmagassag, 2)} m")

print(f"Az ossztály tömege: {tomeg1 + tomeg2 + tomeg3} kg")

tti1 = tomeg1 / (magassag1 ** 2)
tti2 = tomeg2 / (magassag2 ** 2)
tti3 = tomeg3 / (magassag3 ** 2)

print(f"{nev1} TTI-je: {round(tti1, 2)}")
print(f"{nev2} TTI-je: {round(tti2, 2)}")
print(f"{nev3} TTI-je: {round(tti3, 2)}")

max_tti = max(tti1, tti2, tti3)
print(f"A legelhízottabb személy TTI-je: {round(max_tti, 2)}")