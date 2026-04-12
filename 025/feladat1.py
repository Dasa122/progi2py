nev = input("Kérem a gyógynövény nevét: ")
napi = float(input("Kérem a napi szükséges mennyiséget grammban: "))

napok = int(100 / napi)

print(f"A(z) {nev} összesen {napok} napra elegendő")

if napok >= 30:
    print("Elegendő 30 napra egy dobozzal!")
else:
    print("Egy doboz sajnos nem elegendő a 30 napra!")
