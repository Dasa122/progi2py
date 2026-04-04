import math

uticel = input("Kérem adja meg az úticélt: ")
tavolsag = int(input(f"Kérem adja meg {uticel} távolságát: "))
print(f"Szegedre {tavolsag*120} Forintba kerül eljutnia.")
if tavolsag * 120 > 25000:
    print(f"Az Önnél lévő pénz nem elegendő az útra.")
else:
    print(f"Az Önnél lévő pénz elegendő az útra.")

piheno = math.floor(tavolsag / 50) * 5

print(f"{piheno} perc pihenőre lesz szüksége.")