urtartalom = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]
print("2. feladat")
fozottlekvar = int(input("Mari neni lekvarja (dl): "))
while fozottlekvar < 1 or fozottlekvar > 200:
    print("Hibás adat! (1-200 dl)")
    fozottlekvar = int(input("Mari neni lekvarja (dl): "))

print("3. feladat")
temp = 0
temp2 = 0
for i in urtartalom:
    if i > temp:
        temp = i
for i in urtartalom:
    temp2 += 1
    if i == temp:
        break
print(f"A legnagyobb uveg: {temp} dl es {temp2}. a sorban")
print("4. feladat")
for i in urtartalom:
    if fozottlekvar <= 0:
        break
    fozottlekvar -= i
if fozottlekvar <= 0:
    print(f"Elegendo uveg volt.")
else:
    print("Nem volt elegendo uveg")
