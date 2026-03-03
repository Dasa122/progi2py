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
    file.close()
    print(f"3. feladat: Domainok szama: {len(domainek)}")

def domain2(dnev, szint):
    szintek = []
    vissza = ""
    szintek = dnev.split(".")
    if szint > len(szintek):
        vissza = "nincs"
    else:
        vissza = szintek[-1*szint]
    return vissza

def otfeladat():
    print(f"5. feladat: A elso domain felepitese:")
    print(f"\t1. szint: {domain2(domainek[0].domainName, 1)}")
    print(f"\t2. szint: {domain2(domainek[0].domainName, 2)}")
    print(f"\t3. szint: {domain2(domainek[0].domainName, 3)}")
    print(f"\t4. szint: {domain2(domainek[0].domainName, 4)}")
    print(f"\t5. szint: {domain2(domainek[0].domainName, 5)}")

def kiiratas():
    fejlec = f"""
    <table> 
    <tr>
    <th style='text-align: left'>Ssz</th>
    <th style='text-align: left'>Host domain neve</th> 
    <th style='text-align: left'>Host IP címe</th>
    <th style='text-align: left'>1. szint</th>
    <th style='text-align: left'>2. szint</th>
    <th style='text-align: left'>3. szint</th> 
    <th style='text-align: left'>4. szint</th>
    <th style='text-align: left'>5. szint</th> 
    </tr>
    """
    lablec = "</table>"
    with open("table.html", "w", encoding="utf-8") as f:
        f.write(fejlec)
        for i in range(len(domainek)):
            f.write(f"""
            <tr>
            <th style='text-align: left'>{i+1}.</th>
            <td>{domainek[i].domainName}</td>
            <td>{domainek[i].ipCim}</td>
            <td>{domain2(domainek[i].domainName, 1)}</td>
            <td>{domain2(domainek[i].domainName, 2)}</td>
            <td>{domain2(domainek[i].domainName, 3)}</td>
            <td>{domain2(domainek[i].domainName, 4)}</td>
            <td>{domain2(domainek[i].domainName, 5)}</td>
            </tr>
            """)
        f.write(lablec)
    f.close()



def main():
    beolvasas()
    otfeladat()
    kiiratas()


main()