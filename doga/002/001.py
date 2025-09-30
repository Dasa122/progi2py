import math

favFood = "Pizza"
print(f"A kedvenc ételem: {favFood}. Te is szereted a {favFood}-t?")

#############################

fruit = "alma"
price = 100

total_price = 5 * price
print(f"5 kg {fruit} ára: {total_price} Ft")

money = 10000
kgCanBuy = money // price
remaining = money % price
print(f"10 000 Ft-ból {kgCanBuy} kg {fruit}-t tudsz venni, és {remaining} Ft marad.")

#############################

szam = float(input("Adj meg egy valos számot: "))

print(f"A szám egészre kerekítve: {round(szam)}")
print(f"A szám 3 tizedesjegyre kerekítve: {round(szam, 3)}")
print(f"A szám alsó egész része: {math.floor(szam)}")
print(f"A szám felső egész része: {math.ceil(szam)}")
print(f"A szám törtrésze: {szam % 1}")

##############################

product = input("Add meg a termék nevét: ")
unit_price = float(input(f"Add meg a(z) {product} darabárát (Ft): "))
quantity = int(input(f"Hány darab {product}-t szeretnél venni? "))

total = unit_price * quantity
print(f"{quantity} darab {product} összesen {total} Ft-ba kerül.")

##############################

sugar = float(input("Add meg a kor sugarát (cm): "))

kerulet = 2 * math.pi * sugar
terulet = math.pi * sugar ** 2
print(f"A kör sugara: {sugar} cm")
print(f"A kör kerülete: {kerulet} cm")
print(f"A kör területe: {terulet} cm^2")