import random 
# Creates variables for random numbers 
odd_number = random.randint(1,10)
tries = 1
 # Users will input their name to play a game
name = input("Hi, Tell me your Name ")
 
print("Hello", name+",", )
 
question = input("Would you Like Play a Number Guessing Game ? [Y/N] ")
 
if question == "n":
    print("no worries") 
 # Creates loop for the main game
if question == "y":
    print("Say A Number Between 1 & 10")
    guess = int(input("Do you want to give a try : "))
    if guess > odd_number:
        print("Guess Lower than ", guess)
    if guess < odd_number:
        print("Guess Higher than ", guess)
   # Do while loop that continues to check for the correct answer
    while guess != odd_number:
        tries += 1
        guess = int(input("Try Again : ")) 
        if guess == odd_number:
            print("Yay, correct! It Was", odd_number, "and it only", tries, "tries!")
