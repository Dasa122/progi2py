with open("novenyek.txt", encoding="utf-8") as f:
    novenyek = [sor.strip().lower() for sor in f if sor.strip()]

# 2.
for noveny in novenyek:
    print(noveny)

# 3. 
print(f"\nA gyógynövények száma: {len(novenyek)}")

# 4.
def kereses():
    nev = input("Kérem adjon meg egy nevet: ").lower()
    if nev in novenyek:
        print("Szerepel a listában")
    else:
        print("Nem szerepel a listában")

kereses()

# 5.
maganhangzok = "aáeéiíoóöőuúüű"
print("A magánhangzóval kezdődő növények:")
for noveny in novenyek:
    if noveny[0] in maganhangzok:
        print(f"   {noveny}")

# 6.
rendezett = sorted(novenyek)
print("\nA rendezett lista:")
print(", ".join(rendezett))
