def enter_name_amount():
   while True:
        name = input("Enter your name: ")
        if name == float():
            print("Enter a correct name")
           
        else:
            amount = float(input("Enter the amount of money yopu are willing to spend: "))
            if amount == (" "):
                
                print(f"Hello {name} your amont is {amount} ")
                break
            else:
                print("Enter a valid amount")
   return amount
    
    
def snacks(crisp, drink, haribos, chocolate, amount):
    while True:
        ans = amount - crisp
        ans1 = amount - drink
        ans2 = amount - haribos
        ans3 = amount - chocolate
        print(f"Crisps = £{crisp} \n Drink = £{drink} \n Haribos = £{haribos} \n Chocolate = £{chocolate}")
        preference = input("what would you like ")
        preference =  preference.lower()
        if  preference == "crisp":
            if crisp > amount:
                print("You don't have enough money for this item")
            else:
                 print(f"you have puirchased a crisp you haave £{ans} left ")
        elif preference == "drink":
            if drink > amount:
                print("You don't have enough money for this item")
            else:
                print(f"you have £{ans1} left ")
        elif preference == "haribos":
            if haribos > amount:
                print("You don't have enough money for this item")
            else:
                print(f"you have £{ans2} left ")
        elif preference == "chocolate":
            if chocolate > amount:
                print("You don't have enough money for this item")
            else:
                print(f"you have £{ans3} left ")
       

def main():
    crisp = 1.20
    drink = 1.45
    haribos = 2.00
    chocolate = 0.99
    amount = enter_name_amount()
    snacks(crisp, drink, haribos, chocolate, amount)


main()
