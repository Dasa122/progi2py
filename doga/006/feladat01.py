def main():
    boltNev = input("Kérem adja meg a bolt nevét (pl.: ABC):")
    termekEladva = ("Kérem adja meg hány terméket értékesítettek az elmúlt hónapban: ")
    print(f"{boltNev} havi bevétele: 1200000 {termekEladva * 1200}")
    if (termekEladva * 1200) > 2000000: 
        print(f"A(z) {boltNev} bolt sikeres.") 
    else: 
        print(f"A(z) {boltNev} bolt sikertelen") 

main()