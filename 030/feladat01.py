print("feladat 01.")
kg = int(input("kerem a kifigott halak szamat"))
napok = int(input("kerem a tengerben toltott napok szamat"))
atlag = kg/napok
print(f"Az átlagos napi fogás: {atlag}")
if atlag >= 500 and napok >= 5:
    print("A halászat kiemelkedően eredményes volt!")
else:
    print(" A halászat nem volt kiemelkedően eredményes!")
