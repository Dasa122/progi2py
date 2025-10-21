import random
szam = 0
feldobasokSzama = int(input("Hány dobókockával szeretnél dobni? "))
panni = 0
anni = 0

for i in range(feldobasokSzama):
    dobokocka1 = random.randint(1, 6)
    dobokocka2 = random.randint(1, 6)
    dobokocka3 = random.randint(1, 6)
    osszeg = dobokocka1 + dobokocka2 + dobokocka3
    if osszeg < 10:
        print(f"Panni nyert! A dobott értékek: {dobokocka1}, {dobokocka2}, {dobokocka3}. Összeg: {osszeg}")
        panni += 1
    elif osszeg > 10:
        print(f"Anni nyert! A dobott értékek: {dobokocka1}, {dobokocka2}, {dobokocka3}. Összeg: {osszeg}")
        anni += 1
    else:
        print(f"Döntetlen! A dobott értékek: {dobokocka1}, {dobokocka2}, {dobokocka3}. Összeg: {osszeg}")
        anni += 1
        panni += 1

print(f"\nJáték vége! Panni nyert: {panni} alkalommal, Anni nyert: {anni} alkalommal.")

