tavolsag = int(input("Mekkora távolságra utazik (Km)?"))
penz = int(input("Mennyibe került az utazás?"))
print(f"Az út egy kilométere {round((penz/tavolsag), -1)} Ft-ba került.")
auto = tavolsag * 36
if auto > penz/tavolsag:
    print("Az út vonattal olcsóbb.")
elif auto < penz/tavolsag:
    print("Az út autóval olcsóbb.")
else:
    print("Egyenlo!")

