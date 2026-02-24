lista = []

def beolvas():
    f = open("zene.txt")
    for sor in f:
        lista.append(sor.strip())
    print(lista)
    f.close()