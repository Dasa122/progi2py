import random as rd
import inflect
europai_orszagok = [    "Albánia", "Andorra", "Ausztria", "Belgium", "Bosznia-Hercegovina", "Bulgária", "Ciprus",
    "Csehország", "Dánia", "Észtország", "Finnország", "Franciaország", "Görögország",
    "Hollandia", "Horvátország", "Írország", "Izland", "Lengyelország", "Lettország",
    "Liechtenstein", "Litvánia", "Luxemburg", "Észak-Macedónia", "Málta", "Moldova",
    "Monaco", "Montenegró", "Németország", "Norvégia", "Olaszország", "Portugália",
    "Románia", "San Marino", "Spanyolország", "Svájc", "Svédország", "Szerbia",
    "Szlovákia", "Szlovénia", "Ukrajna", "Magyarország", "Egyesült Királyság",
    "Oroszország", "Fehéroroszország"]

afrikai_orszagok = [    "Algéria", "Angola", "Bissau-Guinea", "Botswana", "Burkina Faso", "Burundi",
    "Comore-szigetek", "Csád", "Dél-Afrika", "Dél-Szudán", "Dzsibuti", "Egyiptom",
    "Elefántcsontpart", "Eritrea", "Etiópia", "Gabon", "Gambia", "Ghána", "Guinea",
    "Kamerun", "Kenya", "Kongói Demokratikus Köztársaság", "Kongói Köztársaság", "Lesotho",
    "Libéria", "Líbia", "Madagaszkár", "Malawi", "Mali", "Marokkó", "Mauritánia", "Mauritius",
    "Mozambik", "Namíbia", "Niger", "Nigéria", "Ruanda", "São Tomé és Príncipe", "Szenegál",
    "Seychelles", "Sierra Leone", "Szomália", "Szudán", "Szváziföld", "Tanzánia", "Togo",
    "Tunézia", "Uganda", "Zambia", "Zimbabwe", "Közép-afrikai Köztársaság", "Benin",
    "Guinea-Bissau", "Egyenlítői-Guinea"]
test = "asdf"
def tobb():
    if len(europai_orszagok) > len(afrikai_orszagok):
        print("Europaban található több ország.")
    else:
        print("Afrikában található több ország.")

def legNagyobb(kontinens, lista):
    leghosszabb = ""
    for i in lista:
        if len(leghosszabb) < len(i):
            leghosszabb = i
    print(f"{kontinens} leghosszabb nevű országa: {leghosszabb}")

def europaAjanlo():
    print(f"Ajánlott úti cél: {rd.choice(europai_orszagok)}")

def elsoUtolso():
    print(*europai_orszagok[0:5], *europai_orszagok[-5:], sep=" - ")

def elvalasztva():
    elvalasztvaOrszagok = 0
    for i in europai_orszagok:
        if " " in i or "-" in i:
            elvalasztvaOrszagok += 1
    print(f"{elvalasztvaOrszagok} ország neve van elválasztva.")


def main():
    tobb()
    legNagyobb("Europa", europai_orszagok)
    europaAjanlo()
    elsoUtolso()
    elvalasztva()

main()