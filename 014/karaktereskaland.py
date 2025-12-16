import random
kepessegek_hos = ["ütés", "rugás"]
kepessegek_vakmero = ["kardhasítás", "eltűnés"]
def kezdetiAllapot():
    eletero = random.randint(100, 150)
    return eletero

def jatek():
    global hos_hp, vakmero_hp
    hos_hp = kezdetiAllapot()
    vakmero_hp = kezdetiAllapot()

def kiiras():
    print(f"Hős életereje: {hos_hp}, vakmerő életereje: {vakmero_hp}")

def kihivas(nehezsegi_szint):
    global hos_hp, vakmero_hp
    tamadas_hos = random.choice(kepessegek_hos)
    tamadas_vakmero = random.choice(kepessegek_vakmero)
    hos_sebzes = sebzodes(nehezsegi_szint, tamadas_hos)
    vakmero_sebzes = sebzodes(nehezsegi_szint, tamadas_vakmero)
    print (f"Hős használja a(z) {tamadas_hos} képességet és {hos_sebzes} sebzést okoz.")
    print (f"Vakmerő használja a(z) {tamadas_vakmero} képességet és {vakmero_sebzes} sebzést okoz.")
    hos_hp -= vakmero_sebzes
    vakmero_hp -= hos_sebzes

def sebzodes(nehezsegi_szint, kepesseg):
    if kepesseg == "ütés":
        sebzes = 10 * nehezsegi_szint
    elif kepesseg == "rugás":
        sebzes = 15 * nehezsegi_szint
    elif kepesseg == "kardhasítás":
        sebzes = 12 * nehezsegi_szint
    elif kepesseg == "eltűnés":
        sebzes = 8 * nehezsegi_szint
    return sebzes


def main():
    jatek()
    kiiras()
    kihivas(1)

main()