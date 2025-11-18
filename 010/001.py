command = input("Kérem a robot parancsait:  ").upper().strip()

Eszak = 0
Del = 0
kelet = 0
nyugat = 0
delprocessed = 0
eszakprocessed = 0
keletprocessed = 0
nyugatprocessed = 0

for i in command:
    if i == "E":
        Eszak += 1
    elif i == "D":
        Del += 1
    elif i == "K":
        kelet += 1
    elif i == "N":
        nyugat += 1
    else:
        print("Ismeretlen parancsot adott meg.")
        
eszakdel = Eszak - Del
keletnyugat = kelet - nyugat

if eszakdel > 0:
    eszakprocessed = abs(eszakdel)
else:
    delprocessed = abs(eszakdel)
    
if keletnyugat > 0:
    keletprocessed = abs(keletnyugat)
else:
    nyugatprocessed = abs(keletnyugat)

print(f"""

for i in comm
E betűk száma: {Eszak}
D betűk száma: {Del}
K betűk száma: {kelet}
N betűk száma: {nyugat}     
""", end="")  
print("Egy legrövidebb út parancsszava: ", end="")
for i in range(delprocessed):
    print("D", end="")
    
for i in range(eszakprocessed):
    print("E", end="")
    
for i in range(keletprocessed):
    print("K", end="")
    
for i in range(nyugatprocessed):
    print("N", end="")
    
print()