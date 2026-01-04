import random

products = ["Tej", "Kenyér", "Tojás", "Cukor", "Só", "Bors", "Rizs", "Liszt", "Vaj", "Zsír",
"Tészta", "Paradicsom", "Hagyma", "Fokhagyma", "Citrom", "Banán", "Alma", "Krumpli", "Sárgarépa",
"Uborka"]

cart = {}
discount_product = None
discount_price = 100

def choose_discount():
    global discount_product
    discount_product = random.choice(products)
    print(f"Napi akcio: {discount_product} - csak {discount_price} Ft!")

def calculate_price(product, quantity):
    if product == discount_product:
        return discount_price * quantity
    
    price = 0
    
    if quantity == 1:
        price = 300 * quantity
    elif quantity == 2:
        price = 250 * quantity
    else:
        price = 200 * quantity
    return price

def display_inventory():
    print("\nKESZLET:")
    print("-" * 40)
    for product in products:
        if product == discount_product:
            print(f"{product}: {discount_price} Ft (AKCIO!)")
        else:
            print(f"{product}: 1. db: 300 Ft, 2. db: 250 Ft, 3+ db: 200 Ft")

def add_to_cart(product, quantity=1):
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

def display_cart():
    print("\nKOSAR TARTALMA:")
    print("-" * 50)
    total = 0
    
    for product, quantity in cart.items():
        price = calculate_price(product, quantity)
        total += price
        mark = " (AKCIO!)" if product == discount_product else ""
        print(f"{product}: {quantity} db * {price // quantity} Ft/db = {price} Ft{mark}")
    
    print("-" * 50)
    print(f"OSSZESEN: {total} Ft")
    return total

def purchase():
    global cart
    total = display_cart()
    print(f"\nFizetendo osszeg: {total} Ft")
    print("Vasarlas veglegesiteve!")
    cart = {}
    choose_discount()

def interactive_shopping():
    print("\nINTERAKTIV VASARLAS")
    print("-" * 50)
    
    while True:
        display_inventory()
        
        print("\nValassz egy terméket a kosarhoz:")
        i = 1
        for product in products:
            print(f"{i}. {product}")
            i += 1
        print("0. Befejezés")
        
        choice = input("\nTermék sorszáma (0-20): ")
        
        if choice == "0":
            break
        
        index = int(choice) - 1
        if 0 <= index < len(products):
            product = products[index]
            quantity = input(f"Hány db {product}? ")
            add_to_cart(product, int(quantity))
        else:
            print("Ervenytelen sorszam!")


def main():
    choose_discount()    
    interactive_shopping()
    display_cart()
    purchase()

main()