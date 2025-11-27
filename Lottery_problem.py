import random

def enter_numbers(number):
    ball = 0
    while True:
        ball = int(input(f"Enter your {number} number: "))
        if ball > 0 and ball <= 30:
            break
        else:
            print("Your selection was not between 0 and 30")
    return ball


def match_balls(ball1, ball2, ball3):
    counter = 0
    while True:
        number1 = random.randint(1, 30)
        number2 = random.randint(1, 30)
        number3 = random.randint(1, 30)
        
        if ball1 == number1 and ball2 == number2 and ball3 == number3:
            print(f"Numbers chosen: {ball1},{ball2},{ball3} must match: ball one is {number1} ball two is {number2} ball three is {number3}. It took {counter} weeks to win the jackpot")
            break
        else: 
            counter = counter + 1

def main():
    ball1 = enter_numbers("first") 
    ball2 = enter_numbers("second")
    ball3 = enter_numbers("third")
    match_balls(ball1, ball2, ball3)
    





main()
