def main():
    gyujt = input("mire gyujtessz?")
    dog = int(input("hany kutyat setaltatsz a hetvegen"))
    walkTime = 20 * dog
    hour = walkTime // 60
    minute = walkTime - (walkTime // 60) * 20
    print(f"{hour}:{minute}") 
    
    pinz = dog * 700
    if pinz >= 5000:
        print(f"Anna {dog} kutyát sétáltatott {hour} óra {minute} perc alatt, ezért {pinz} Ft-ot kapott. Ez még nem elég! {gyujt} :(.")
    else:
        print(f"Anna {dog} kutyát sétáltatott {hour} óra {minute} perc alatt, ezért {pinz} Ft-ot kapott. Ez mar elég! {gyujt} :).")

main()