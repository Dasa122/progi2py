class Postit:
    def __init__(self, background_color: str, szerzo: str, text: str):
        self.background_color = background_color
        self.text = text
        self.szerzo = szerzo
    def __str__(self):
        return f"Postit(background_color={self.background_color}, szerzo={self.szerzo}, text={self.text})"

def uzenetekIrasa():
    pstit1 = Postit("rozsaszin", "Jancsi", "Ne felejts el venni tejet!")
    print(pstit1)
    pstit2 = Postit("sarga", "Juliska", "Holnap suli van.")
    print(pstit2)
    pstit3 = Postit("narancssarga", "Gergő", "Ma van a szulinapom.")
    print(pstit3)
    lista.append(pstit1)
    lista.append(pstit2)
    lista.append(pstit3)
lista = []

def legmagasabbUzenet():
    leghosszab = lista[0]
    for i in lista:
        if len(i.text) > len(leghosszab.text):
            leghosszab = i
    print("Leghosszabb uzenet:")
    print(leghosszab)
    print(f"Hossza: {len(leghosszab.text)} karakter")



def main():
    uzenetekIrasa()
main()