dobasok = [3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4]
pos = 0
letra = 0
print("2. feladat")
for dobas in dobasok:
    pos += dobas
    if pos % 10 == 0:
        pos -= 3
        letra += 1
    print(pos, end=" ")
    if pos >= 45:
        print("\n3. feladat")
        print(f"A játék során {letra} alkalommal lépett létrára.")
        print("4. feladat")
        print("A játékot befejezte.")
        break