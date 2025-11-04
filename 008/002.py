print(ord('a'))
print(chr(65))
print(chr(1))



#n = 0

#while True:
#    n += 1
#    print(chr(n), end=" ")

szo = "Tizedik d osztály"

print(len(szo))

for i in range(len(szo)):
    print(f"{i}. karakter: {szo[i]}")
    
print(szo[0:7])

for i in szo:
    print(i, end="; ")
    
# elso elofordulas
print(szo.index('d'))

print(szo.split('z'))

print(szo.split(' '))

nevek = ["Kati", "Peti", "Gabor", "Dora"]