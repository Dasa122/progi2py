import datetime

class Player:
    def __init__(self, line):
        parts = line.strip().split(";")
        self.name = parts[0]
        date_format = "%Y-%m-%d"
        self.first = datetime.datetime.strptime(parts[1], date_format)
        self.last = datetime.datetime.strptime(parts[2], date_format)
        self.weight = int(parts[3])
        self.height = int(parts[4])
    def __str__(self):
        return f"{self.name} first: {self.first} last: {self.last} weight: {self.weight} height: {self.height}"

players = []

def read_file():
    f = open("balkezesek.csv", encoding="utf-8")
    f.readline() 
    for line in f:
        players.append(Player(line))
    f.close()
    for item in players: 
        print(item)

def task04():
    print("4. feladat:")
    for item in players: 
        if item.last.year == 1999 and item.last.month == 10:
            print(f"{item.name} {item.height * 2.54:.1f} cm")

def task05():
    print("5. feladat:")
    while True:
        year = int(input("Adj meg egy evet 1990 es 1999 kozott: "))
        if 1990 <= year <= 1999:
            break
        print("Ervenytelen adat!", end = " ")
    total = 0
    count = 0
    for item in players: 
        if item.first.year <= year and item.last.year >= year:
            total += item.weight
            count += 1
    avg = round(total / count, 2)
    print(f"Atlagos suly: {avg} font")

def main():
    read_file()
    print(f"3. feladat: {len(players)}")
    task04()
    task05()

main()