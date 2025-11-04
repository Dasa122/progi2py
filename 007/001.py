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

for x in range(5):
    print(f"{x}. Gergo Kovago")

for i in range(1, 10):
    print(i, end=" ")
    
print() 
# i ciklusvaltozo felveszi a rangen levo kezdoerteket vagy a nullat aha nics nincs kezdoertek megadva
for i in range(10, 101, 10):
    print(i, end=" ")
    
