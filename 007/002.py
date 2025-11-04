szam = int(input("Kérem adjon meg egy számot 1 és 10 között: "))

szolas = "Egy fecske nem csinál nyarat."

if 1 <= szam <= 10:
    for i in range(1, szam + 1):
        print(f"{i}. {szolas}")
else:
    print("A megadott szám nincs 1 és 10 között!")
    
    
################################################

szam = int(input("Kérem adjon meg egy számot 1 és 10 között: "))

if 1 <= szam <= 10:
    for i in range(1, szam + 1):
        print(f"Megmondtam már {i}-szer, hogy semmit sem mondok el kétszer!")
else:
    print("A megadott szám nincs 1 és 10 között!")
    
################################################

n = int(input("Kérem adjon meg egy pozitív egész számot (N): "))

if n > 0:
    for i in range(n):
        chars = 2 * i + 1
        spaces = n - i - 1
        print(" " * spaces + "#" * chars)
else:
    print("A megadott szám nem pozitív egész!")

#################################################

n = int(input("Kérem adjon meg egy pozitív egész számot (N): "))

if n > 0:
    # Felső, fejjel lefelé álló piramis
    for i in range(n-1):
        chars = 2 * (n - i) - 1
        spaces = i
        print(" " * spaces + "#" * chars)
    
    # Alsó, normál helyzetű piramis
    for i in range(n):
        chars = 2 * i + 1
        spaces = n - i - 1
        print(" " * spaces + "#" * chars)
else:
    print("A megadott szám nem pozitív egész!")

#################################################

n = int(input("Hány piramisból álljon a fenyőfa? (pozitív egész): "))
if n <= 0:
    print("A megadott szám nem pozitív!")
else:
    base_height = n + 1
    base_width = 2 * base_height - 1

    for level in range(1, n + 1):
        height = level + 1
        for row in range(height):
            chars = 2 * row + 1
            spaces = (base_width - chars) // 2
            print(" " * spaces + "#" * chars)

    trunk_width = n if n % 2 == 1 else n + 1
    trunk_height = max(1, n // 2)
    trunk_spaces = (base_width - trunk_width) // 2
    for _ in range(trunk_height):
        print(" " * trunk_spaces + "|" * trunk_width)

#################################################

texto = input("Kérem adjon meg egy rövid szöveget: ")
reversed_text = ""
for ch in texto:
    reversed_text = ch + reversed_text
print(reversed_text)

