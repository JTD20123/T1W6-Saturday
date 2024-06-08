#guessing game      

guess_num = 5

user_guess = None

while user_guess != guess_num:
    user_guess = int(input("Whats your guess (between 1 and 10)"))


print("correct")

#make it better
#give user hints

while user_guess != guess_num:
    user_guess =int(input("whats your guess (between 1 to 10)"))

    if user_guess < guess_num:
        print("too low")
    elif user_guess > guess_num:
        print("Too high")
    else: 
        print ("Correct")