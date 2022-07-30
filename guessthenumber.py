import random

compnum = random.randint(1,10)
guessedright = False

while guessedright == False:
    usernum = input("Guess a number between 1 and 10: ")
    try: usint = int(usernum)
    except:
        print("Please enter a number")
        continue
    if usint == compnum:
        print("Wow! You got it!")
        guessedright = True
    else:
        print("Sorry! Try again")