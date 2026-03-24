class Eladas:         
    def __init__(self, TermékID, BoltNeve, Darabszám, Bevétel):
            self.TermékID = TermékID
            self.BoltNeve = BoltNeve
            self.Darabszám = Darabszám
            self.Bevétel = Bevétel
    def __str__(self):
        return f"TermékID: {self.TermékID} BoltNeve: {self.BoltNeve} Darabszám: {self.Darabszám} Bevétel: {self.Bevétel}"
eladasok = []
boltok = []
def beolvasas():
    f = open("eladasok.txt", "r", encoding="UTF-8")
    f.readline()
    for l in f:
        splittedline = l.strip().split(";")
        eladasok.append(Eladas(*splittedline))
    f.close

def kiiratas(): 
    for i in eladasok:
        print(i)
        
def elsoeladas():
    print("Az elso eladas bolt:", eladasok[0].BoltNeve, "Termek:", eladasok[0].TermékID )
        
def legmagasabb():
    legnagyobb = 0
    for i in eladasok:
        if int(i.Bevétel) > legnagyobb:
            legnagyobb = int(i.Bevétel)
    for i in eladasok:
        if legnagyobb == int(i.Bevétel):
            print(f"A legnagyobb bevetel: {i}")
            
def boltokneve():
    for i in eladasok:
        if i.BoltNeve not in boltok:
            boltok.append(i.BoltNeve)
    print("Boltok: ", end="")
    print( *boltok, sep=", ")


        
    
        

def main():
    beolvasas()
    kiiratas()
    elsoeladas()
    legmagasabb()
    boltokneve()
main()

