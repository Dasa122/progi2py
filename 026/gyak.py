szotar = {"nulla": 0, "egy": 1, "kettő": 2, "három": 3, "négy": 4, "öt": 5, "hat": 6, "hét": 7, "nyolc": 8, "kilenc": 9}
print(szotar)
print(szotar["három"])
szotar["tíz"] = 11
print(szotar)
print(len(szotar))
kulcsok = szotar.keys()
print(kulcsok)
ertekek = szotar.values()
print(ertekek)
for kulcs in szotar:
    print(kulcs, szotar[kulcs])

szotar.pop("tíz")
print(szotar)