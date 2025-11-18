tajszam = input("Kérem a TAJ-számot: ")
ellenorzoszam = int(tajszam[-1])
print(ellenorzoszam)
print(f"Az ellenőrzőszámjegy: {ellenorzoszam}")
osszeg = 0
for i in range(8):
    
    if ((i+1) % 2) == 1:
        osszeg += int(tajszam[i]) * 3
        #print(i+1, int(tajszam[i]),"3", int(tajszam[i])*3)
      

    else:
        osszeg += int(tajszam[i]) * 7
        #print(i+1, int(tajszam[i]), "7", int(tajszam[i])*7)
        
print(f"A szorzatok összege: {osszeg}")
if (osszeg % 10) == ellenorzoszam:
    print("Helyes a szám!")
else:
    print("Hibás a szám!")

