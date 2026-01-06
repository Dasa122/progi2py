lista = [100, 120, 140, 110, 160]
torpek = []
def fajlbeiras():
    f = open("storpek.txt", "w", encoding="utf-8")
    for item in lista:
        s = f"{item}\n"
        f.write(s)
    f.close()

def beolvasas():
    with open("storpek.txt", "r", encoding="utf-8") as f:
        for sor in f:
            torpek.append(sor.strip())
    print(*torpek, sep=", ")
def main():
    fajlbeiras()
    beolvasas()


main()