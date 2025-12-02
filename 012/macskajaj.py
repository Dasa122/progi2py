import random
def egyeniPontszam():
    return random.randint(1, 5) * 10

def csapatPontszam():
    csapat = []
    for i in range(7):
        csapat.append(egyeniPontszam())
    return csapat

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
        print(f"Az első kört a szuperegerek nyerték")
        return False
    elif csapat2ossz > csapat1ossz:
        print(f"Az első kört a űrmacskák nyerték")
        return True
    else:
        print("Az első kör döntetlen lett")
        return None
def main():
    print(gyoztes())
    
    


main()


