import random

lista = [0, 0, 0, 0, 0]
for i in range(5):
    lista[i] = int(input(f"Adja meg a(z) {i+1}. egész számot: "))
            
print("A lista:", lista)


logikai_lista = [0,0,0,0,0,0,0]
for i in range(7):
    logikai_lista[i] = random.choice([True, False])

print("A logikai lista:", logikai_lista)

for i in range(len(logikai_lista)):
    if logikai_lista[i] == False:
        print("Hamis")
    else:
        print("Igaz")



nums = [random.randint(5, 25) for i in range(10)]

print("\n10 elemű lista:", nums)


print("Fordított sorrend:")
for i in range(len(nums)-1, -1, -1):
    print(nums[i])

print("c) Minden második elem:")
for i in range(1, len(nums), 2):
    print(nums[i])
    
lista11 = [random.randint(0, 100) for i in range(2)]
lista12 = [random.randint(0, 100) for i in range(6)]
lista13 = [0]

print("Lista 1.:", lista11)
print("Lista 2.:", lista12)

lista13[0] = sum(lista11) + sum(lista12)


print("\nEredeti lista:", nums)

if nums:
    jobbra = [nums[-1]] + nums[:-1]
else:
    jobbra = nums[:]
print("Jobbra léptetve:", jobbra)

if nums:
    balra = nums[1:] + [nums[0]]
else:
    balra = nums[:]
print("Balra léptetve:", balra)

N = int(input("Adja meg N értékét: "))
listaN = [0] * N
for i in range(N):
    listaN[i] = random.randint(1, 100)

print("Eredeti lista:", listaN)
megforditott = listaN[::-1]
print("Megfordított lista:", megforditott)




