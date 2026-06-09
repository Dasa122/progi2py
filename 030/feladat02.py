halfajtak = [
    "Lazac",
    "Tőkehal",
    "Hering",
    "Makréla",
    "Lepényhal",
    "Szivárványos pisztráng",
    "Vörös álsügér",
    "Fekete tőkehal",
    "Foltos tőkehal",
    "Szardínia"
]

def halfajtak_kiirasa():
    print(" 1. feladat: a halfajták kiíratása:")
    temp = 1
    for i in halfajtak:
        print(f"{temp}. {i}")
        temp += 1

def halfajta_keresese(keresett):
    print("2. feladat ")
    if keresett in halfajtak:
        print("A halfajta szerepel a listában.")
    else:
        print("A halfajta nem szerepel a listában.")

def leghosszabb_nevu_halfajta():
    print("3. feladat ")
    temp = 0
    for i in halfajtak:
        if len(i) > temp:
            temp = len(i)
    for i in halfajtak:
        if temp == len(i):
            return i





def main():
    halfajtak_kiirasa()
    keresett = input("Kérem adjon meg egy halfajtát: ")
    halfajta_keresese(keresett)
    print(f"A leghosszabb nevű halfajta: {leghosszabb_nevu_halfajta()}")

main()