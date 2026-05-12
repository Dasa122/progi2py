print("1. feladat")

kepregenyneve = input("1.1 Adja meg a képregénybolt nevét! ")

eladott = int(input("1.2 Hány képregényt adtak el? "))

print(f"1.3 A bolt bevétele: {eladott*3200} Forint.")

print(f"1.4 Egy napra átlagosan {round(eladott/7 * 3200, 2)} Forint bevétel jutott.")

if eladott >= 500:
    print("1.5 A heti értékesítés sikeres volt.")
else:
    print("1.5 A heti értékesítés nem volt sikeres.")