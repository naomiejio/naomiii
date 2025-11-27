def enter_pound():
    pound = float(input("Enter the amount you want to convert: "))
    return pound



def other_currency(pound):
    curr = print("Do you want to convert", pound, "to USD, Euro, Yuan or Yen?: ")
    currency = input()
    return currency


def calculate(pound):
    usd = pound * 1.35
    euro = pound * 1.15
    yuan = pound * 9.59
    yen = pound * 199.79
    return usd, euro, yuan, yen



def converter(pound, currency, usd, euro, yuan, yen):
    if currency == "USD":
        money = print(pound,"GBP = ", usd,"USD")
    elif currency == "EURO":
        money = print(pound,"GBP = ", euro,"Euro")
    elif currency == "YUAN":
        money = print(pound,"GBP = ", yuan,"Yuan")
    else:
        money = print(pound,"GBP = ", yen,"Yen")
        return money




def main():
    pound = enter_pound()
    currency = other_currency(pound)
    currency = currency.upper()
    usd, euro, yuan, yen = calculate(pound) 
    money = converter(pound, currency, usd, euro, yuan, yen)
    



main()
