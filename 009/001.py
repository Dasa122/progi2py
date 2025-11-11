import random

answ = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]

solve = random.choice(answ)
word = ""
tippek = 0
temp = 0
while solve != word:

    word = input("Kérem a tippet: ")
    if word == "stop":
        break
    if word != "":
        if len(word) != 6 and word != "stop":
            print("A szó hossza nem megfelelő. 6 betűs szót kérek.")
            continue
        tippek += 1
        print("Az eredmény: ", end="")
        for i in solve:
            if i == word[temp]:
                print(i, end="",)
            else:
                print(".", end="")
            temp += 1
        temp = 0
        print()
        
if word != "stop":
    print(f"{tippek} tippeléssel sikerült kitalálni.")
    
        
