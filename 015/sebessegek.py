lista = []
def beolvas():
    f = open("sebessegek.txt")
    for sor in f:
        lista.append(sor.strip())

def leggyorsabb():
    max_sebesseg = 0
    for sebesseg in lista:
        if max_sebesseg < sebesseg:
            max_sebesseg = sebesseg
    print("A leggyorsabb sebesség:", max_sebesseg)

def buntetsesek():
    buntetes = 0
    for sebesseg in lista:
        if sebesseg > 130:
            buntetes += 1
    print("Összes büntetés:", buntetes)

def main():
    beolvas()
    leggyorsabb()
    buntetsesek()
    print(lista)
main()