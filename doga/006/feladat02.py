import random

vasarlokSzamaNaponta = []
def Generalas(napokSzama):
    for i in range(napokSzama):
        vasarlokSzamaNaponta.append(random.randrange(1, 100))
    print("A vásárlók száma naponta: ", end="")
    print(*vasarlokSzamaNaponta, sep=", ")

def  vasarlokSzama():
    vasalokOsszesen = 0
    for i in vasarlokSzamaNaponta:
        vasalokOsszesen = vasalokOsszesen + i
    print(f"A vasarlok szama osszesen: {vasalokOsszesen} db")


def main():
    Generalas(31) 
    vasarlokSzama()   

main()