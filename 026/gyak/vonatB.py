idklist = []

def feltoltes():
    with open("30a.txt", "r", encoding="UTF-8") as f:
        for i in f:
            idklist.append(i.strip())
    print("A 30A útvonal beolvasása sikeresen megtörtént")

def megalloKereses(megallo):
    count = 0
    for i in idklist:
        count = count + 1
        if megallo.upper() == i.upper():
            return True, count


def main():
    feltoltes()
    megallonev = input("Kérek, adj meg egy megállóhelyet: ")
    kereses = megalloKereses(megallonev)
    if kereses == None:
        print("Nincs ilyen nevű megálló az útvonalon")
    else:
        print(f"Van ilyen nevű megálló az útvonalon, a {kereses[1]}. helyen")

main()