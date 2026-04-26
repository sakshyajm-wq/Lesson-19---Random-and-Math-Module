import random
playing = True
number = str(random.randint(0,9))
print("I will generate a number from 0 to 9, and you will have to guess the number one digit at a time")
print("The game ends when you guess the number")
while playing:
    guess = input("Give me your BEST GUESS\n")
    if number == guess:
        print("You win the game!!!")
        print("The number was", number)
        break
    
    else:
        print("Yout guess isn't quite right please try again.\n")