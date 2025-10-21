import random
szam = random.randint(1, 10)
tipp = int(input("Gondoltam egy számra 1 és 10 között. Melyik az? "))
eltalata = False

while not eltalata:
    if tipp < szam:

        print("Túl alacsony!")
        tipp = int(input("Próbáld újra: "))
    elif tipp > szam:
        print("Túl magas!")
        tipp = int(input("Próbáld újra: "))
    else:
        eltalata = True
        print("Gratulálok, eltaláltad a számot!")