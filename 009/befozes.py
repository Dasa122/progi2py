uvegDl = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]
print("2. feladat")
index = 0
allindex = 0
legnagyobbUveg = 0
lekvarDl = int(input("Mari néni lekvárja (dl):"))
for i in uvegDl:
    if i > legnagyobbUveg:
        legnagyobbUveg = i
        index += 1
print(f"A legnagyobb üveg: {legnagyobbUveg} dl és {allindex - index}. a sorban.")

for i in uvegDl:
    lekvarDl -= i
    
if lekvarDl < 0:
    print("3. feladat")
    print("Elegendő üveg volt.")
else:
    print("3. feladat")
    print(f"Maradt lekvar")
