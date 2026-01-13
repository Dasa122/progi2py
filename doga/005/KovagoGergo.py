gergo = ["alma", "banan", "cseresznye", "dinnye", "helikopter"]

def beolvas():
    f = open("KovagoGergo.txt", "w", encoding="utf-8")
    for i in gergo:
        f.write(f"{i}\n")
    f.close()

def kiir():
    f = open("KovagoGergo.txt", "r", encoding="utf-8")
    for sor in f:
        print(sor.strip())
    f.close()

def main():
    beolvas()
    kiir()

main()
