adatok = []
with open("jeladas.txt", encoding="utf-8") as f:
    for sor in f:
        r, o, p, s = sor.strip().split("\t")
        adatok.append((r, int(o), int(p), int(s)))

print("1. feladat:")
rendszamok = []
for r, o, p, s in adatok:
    if r not in rendszamok:
        rendszamok.append(r)
print(f"A jeladások száma: {len(adatok)}")
print(f"A járművek száma: {len(rendszamok)}")

print("2. feladat:")
utolso = adatok[-1]
print(f"Az utolsó jeladás időpontja {utolso[1]}:{utolso[2]:02d}, a jármű rendszáma {utolso[0]}")

print("3. feladat:")
elso_rendszam = adatok[0][0]
print(f"Az első jármű: {elso_rendszam}")
idopontok = [f"{o}:{p}" for r, o, p, s in adatok if r == elso_rendszam]
print("Jeladásainak időpontjai:", " ".join(idopontok))

print("4. feladat:")
ora = int(input("Kérem, adja meg az órát: "))
perc = int(input("Kérem, adja meg a percet: "))
szam = sum(1 for r, o, p, s in adatok if o == ora and p == perc)
print(f"A jeladások száma: {szam}")

print("5. feladat:")
max_seb = max(s for r, o, p, s in adatok)
max_jarmuvek = []
for r, o, p, s in adatok:
    if s == max_seb and r not in max_jarmuvek:
        max_jarmuvek.append(r)
print(f"A legnagyobb sebesség km/h: {max_seb}")
print(f"A járművek: {' '.join(max_jarmuvek)}")

print("6. feladat:")
keresett = input("Kérem, adja meg a rendszámot: ")
jarmu_adatok = [(o, p, s) for r, o, p, s in adatok if r == keresett]
tavols = 0.0
for i, (o, p, s) in enumerate(jarmu_adatok):
    print(f"{o}:{p} {round(tavols, 1)} km")
    if i + 1 < len(jarmu_adatok):
        ko, kp, ks = jarmu_adatok[i + 1]
        perc_diff = (ko * 60 + kp) - (o * 60 + p)
        tavols += s * perc_diff / 60

print("7. feladat:")
elso = {}
utolso_dict = {}
for r, o, p, s in adatok:
    if r not in elso:
        elso[r] = (o, p)
    utolso_dict[r] = (o, p)
for r in rendszamok:
    eo, ep = elso[r]
    uo, up = utolso_dict[r]
    print(f"{r} {eo} {ep} {uo} {up}")
