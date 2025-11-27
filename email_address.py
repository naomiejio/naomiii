def enter_email():
    email = input("Enter your email address: ")
    return email


def check_symbol1(email):
    if "@" in email and "." in email:
        valid = True
    else: 
        valid = False
    return valid


def main():
    email = enter_email()
    print(email)
    valid = check_symbol1(email)
    print(valid)
  
    
main()
