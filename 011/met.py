import random, math
def feladat01():
    kocka1 = random.randint(1, 10)
    kocka2 = random.randint(1, 10)
    print(f"A két kocka értéke: {kocka1} és {kocka2}")
    if kocka1 > kocka2:
        print("Az első kocka értéke nagyobb.")
    elif kocka1 < kocka2:
        print("A második kocka értéke nagyobb.")
    else:
        print("A két kocka értéke egyenlő.")

def feladat02(elemekSzama):
    print("\n--------------------------------\n")
    lisat = []
    for i in range(elemekSzama):
        lisat.append(random.randint(1, 100))
    print(*lisat,sep=", ")
    osszeg = sum(lisat)
    print(osszeg)
    

def feladat03(num):
    print(math.pow(num, 2))
    print(math.pow(num, 3))
    print(math.pow(num, 4))
    
def feladat04(szoveg):
    print(szoveg.capitalize())
    print(szoveg.upper())
    print(szoveg.lower())
    
def feladat05(szoveg:str):
    for i in szoveg:
        print (f"{i} ", end="")
    print()
        
def feladat06(szoveg:str):
    for i in szoveg:
        print (f"{i} ")
    print()
        





def main():
    #feladat01()
    #feladat02(10)
    #feladat02(5)
    #feladat02(8)
    #feladat02(345)
    #feladat03(2)
    #feladat04("vDFFlklDskSskdn")
    feladat05("HelloWorld!")
    feladat06("HelloWorld!")

    
main()