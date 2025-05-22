import random


secret_number = random.randint(1, 100)
guess= int(input("Guess a number between 1 and 100: "))


while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
        guess = int(input("Try again:"))


        print("Congrats!!!you guessed it right.")
        
