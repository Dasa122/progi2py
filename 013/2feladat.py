import random
generalaslist = []
mecseredmenyek = []
def generalas(napokszama):
    for i in range(napokszama):
        generalaslist.append(random.randint(50, 200))
    print(generalaslist)

def legnagyobb():
    max = generalaslist[0]
    for i in range(len(generalaslist)):
        if generalaslist[i] > max:
            max = generalaslist[i]
    print(f"A legnagyobb: {max}")
    return max

def generalas1(mecsekszama):
    for i in range(mecsekszama):
        mecseredmenyek.append(random.randint(0, 1))
    print(mecseredmenyek)

def statisztika():
    for i in range(len(mecseredmenyek)):
        if mecseredmenyek[i] == 1:
            nyeres += 1
            return nyeres
        else:
            pass

def main():
    #napokszama = int(input("Add meg a napok számát: "))
    #generalas(napokszama)
    #legnagyobb()
    generalas1(7)

main()