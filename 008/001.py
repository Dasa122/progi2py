szam = 5

while True:
    tipp = int(input("Tippelj egy számot 1 és 10 között: "))
    if tipp == szam:
        print("Helyes válasz!")
        break
    else:
        print("Helytelen válasz, próbáld újra!")
        
print("A játék véget ért.")