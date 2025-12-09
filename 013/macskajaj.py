import random
def egyeniPontszam():
    return random.randint(1, 5) * 10

def csapatPontszam():
    csapat = []
    for i in range(7):
        csapat.append(egyeniPontszam())
    return csapat

def jatek():
    urmacskak = 0
    szuperegerek = 0   
    for i in range(7):
        if gyoztes() is True:
            urmacskak += 1
        elif gyoztes() is False:
            szuperegerek += 1
        else:
            szuperegerek += 1
            urmacskak += 1
        
    if szuperegerek > urmacskak:
        print("A játéknak a szuperegerek lettek a győztesei")
    elif urmacskak > szuperegerek:
        print("A játéknak a űrmacskák lettek a győztesei")
    else:
        print("A játéknak döntetlen lett az eredménye")


def pontOsszesites(pontszamok:list):
    return sum(pontszamok)

def gyoztes():
    csapat1 = csapatPontszam()
    csapat2 = csapatPontszam()
    csapat1ossz = pontOsszesites(csapat1)
    csapat2ossz = pontOsszesites(csapat2)
    print("űrmacskák:", *csapat1, "->", csapat1ossz)
    print("szuperegerek:", *csapat2, "->", csapat2ossz)
    if csapat1ossz > csapat2ossz:
        print(f"Ezt a kört a szuperegerek nyerték")
        return False
    elif csapat2ossz > csapat1ossz:
        print(f"Ezt a kört a űrmacskák nyerték")
        return True
    else:
        print("Ez a kör döntetlen lett")
        return None
def main():
    jatek()
    
    


main()


