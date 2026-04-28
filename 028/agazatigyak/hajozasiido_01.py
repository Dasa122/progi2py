ideje = int(input(f"""1.1. feladat
Kérem, adjon meg egy repülési időt percben: """))

perc = ideje %  60

print(f"""
1.2. feladat
A repülőút hossza {int(ideje / 60)} óra {perc} perc.""")

if ideje > 120:
    print(f"""\n1.3. feladat
Az utasok kaptak melegételt: igen""")
else:  
    print(f"""1.3. feladat
Az utasok kaptak melegételt: nem""")