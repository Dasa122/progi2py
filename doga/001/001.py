print("Szintaktikai hiba:Azt jelenti hogy a te kódod nem felel meg a Python nyelv leírási stilusának szabályainak.")

###############

favfood = "pizza"
print(f"A kedvenc ételem {favfood}! \n Te is szereted a {favfood}-t?")

###############

celsius = 36.5
fahrenheit = celsius * 1.8 + 32
print(f"A(z) {celsius} C pontosan {fahrenheit} F!")

###############

gyumi = "mango"
kg_price = 1000

print(f"""
      5 kg {gyumi} {kg_price * 5} Ft.
10 000 Ft-ból 6 kg {gyumi}-t tudok venni és még 
marad {10000 - kg_price * 6} Ft-om
      """
    
)
