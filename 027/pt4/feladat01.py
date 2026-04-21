print("1. feladat")
etteremneve = input("1.1 Adja meg az étterem nevét!")
menudb = int(input("1.2 Hány menüt értékesítettek? "))
print(f"1.3 Az étterem bevétele: {menudb * 1800} Forintot.")
print(f"1.4 Egy napra átlagosan {round(((menudb * 1800)/7), 2)} Forint bevétel jutott.")
if menudb < 1000:
    print("A heti ertekesites veszteseges volt")
else:
    print("A heti ertekesites nyereseges volt")
