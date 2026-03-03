class Domain:
    def __init__(self, domainName, ipCim):
        self.domainName = domainName
        self.ipCim = ipCim

    def __str__(self):
        return f"Domain: {self.domainName}, IP: {self.ipCim}"
    

def beolvasas():
    global domainek
    with open("csudh.txt", "r", encoding="utf-8") as file:
        domainek = []
        file.readline()  
        for i in file:
            parts = i.strip().split(";")
            domainek.append(Domain(parts[0], parts[1]))
    print(f"3. feladat: Domainok szama: {len(domainek)}")



def main():
    beolvasas()
    

main()