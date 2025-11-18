hetek = int(input("Hetek száma="))
testomegcel = float(input("Elérni kívánt testtömeg (kg)="))
hetekadat = []
elerte = 0
nott = 0

for i in range(hetek):
    hetekadat.append(float(input(f"{i+1}. heten=")))
    if hetekadat[i] <= testomegcel:
        if elerte == 0:
            elerte = i+1
    if hetekadat[i-1] < hetekadat[i]:
        nott += 1

if elerte != 0:
    print(f"Mari néni a(z) {elerte}. héten érte el a célt.")
else:
    print("Sajnos Mari néni nem érte el a célját.")
    
print(f"A tömege {nott} esetben nőtt egyik hétről a másikra.")