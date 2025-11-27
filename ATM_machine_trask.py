def ask_pin(correct_pin, balance):
    counter = 1 #made that variable so the while loop cxan ask three times and not multiple
    while True:#while loop
        pin = int(input("Enter the pin: "))
        if pin == correct_pin:
            amount = int(input("How much do you want to withdraw?"))
            if amount <= 100:
                print("Transaction approved, have a good day")
                break#put the break there before the else so it stops there if the person meets the condition
            else:
                print("Insufficient funds")
        else:
            print("Incorrect pin")
            counter += 1#added 1 to it so it can ask again and again
            if counter == 3:#equaled it to 3 so if it asks three times
                print("Your account has been locked.")
                break#kich the person out and lock the account

    #you don't have to return pin because no other function needs it



def main():
    correct_pin = 2468
    balance = 100
    ask_pin(correct_pin, balance)#main does'nt care about pin = ask_pin because no other function after this function needs pin



main()
